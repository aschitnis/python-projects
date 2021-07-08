import threading, time, signal
import httpweathermodule as w
import mysqlconnectormodule as c
import csv
import os
import time
from datetime import datetime
import xml.etree.ElementTree as ET
from timeloop import Timeloop
from datetime import timedelta

# List of countries & their ISO codes.
# Link: https://pypi.org/project/pycountry/#description
# pip install pycountry
import pycountry

# this package is used to get the country-codes through a REST-http request.
# pip install datapackage
# Dokumentation: https://datahub.io/core/country-list#python
from datapackage import Package 

PROCESS_WAIT_TIME_SECONDS = 0  # every call to the Wetter WebService.
MAX_PROCESS_RUNNING_TIME_IN_MINUTES = 0

MAX_COUNTER_LIMIT = 1
START_COUNTER_VALUE = 1

class ProgramKilled(Exception):
 pass

#**** CLASS csv file create/read/write *********
#***********************************************
class WetterDatenCSV:
 is_csv_vorhanden = False
 dictWetterdatenCsv = {}	# declare a Dictionary for storing the weather data in a CSV file
 CSVFILE = "weatherdata.csv"

 def __init__(self):
  self.is_csv_vorhanden = False

 def check_exists_CSVFile(self):
  if os.path.exists(self.CSVFILE) == True:
   self.is_csv_vorhanden = True
  else:
   print("weatherdata csv file not found")
   self.is_csv_vorhanden = False

 def append_to_CSV(self):
  if os.path.exists(self.CSVFILE) == True:
   print("csv file is present")
   with open(self.CSVFILE,'a+',newline='') as file:     
    writer = csv.writer(file)
    print("..... writing to csv file")
    writer.writerow([datetime.now(None), self.dictWetterdatenCsv["Ort"], self.dictWetterdatenCsv["Beschreibung"], self.dictWetterdatenCsv["Aktuelletemperatur"]])
  else:
   self.is_csv_vorhanden = False
   print("csv file could not be opened")  


# **** CLASS xml file reading ********
# ************************************
class XmlReader:
 dictOrtsnamen = {} # key is <id> 
                    # value is a List[] i.e. [<name>,<country>]. See Xml file ortefuerwetterabfragen.xml.
 is_xml_loaded = False
 xmlnode_wartezeitproprozessdurchlauf_stunden = 0 
 xmlnode_wartezeitproprozessdurchlauf_minuten = 0
 xmlnode_prozesslaufzeit_stunden = 0 
 xmlnode_prozesslaufzeit_minuten = 0
 XMLQUERYFILE = "weatherdataquery.xml"  

 def __init__(self):
  self.is_xml_loaded = False
 
  # a dictionary with Key of type String and Value of type List[].
  # e.g. Key=1 and Value=['salzburg','austria']
  self.dictOrtsnamen = {} 
  self.loadXml()

 # load and parse the Xml file.
 # save the values of the Rootnode '<ort>' node-elements in a dictionary.
 # save the values of the Rootnode '<zeitablauf>' node-elements in class variables.
 def loadXml(self):
  if os.path.exists(self.XMLQUERYFILE) == True:
   tree = ET.parse(self.XMLQUERYFILE)
   self.is_xml_loaded = True
    
   root = tree.getroot()
   ortElements = list(e for e in root.iter("ort") )
   for ort in ortElements:	# ort.tag == "ort"
    self.dictOrtsnamen[ort[0].text] = [ort[1].text,ort[2].text]	  # ort[0].tag = 'id'.   e.g. ort[0].text = '1' (this is the KEY)
                                                                  # ort[1].tag = 'name'. e.g. ort[1].text = 'salzburg' (this is the VALUE)
  																  # ort[2].tag = 'country'. e.g. ort[2].text = 'austria' (this is the VALUE)
   wartezeitElements = list(e for e in root.iter("wartezeitproprozessdurchlauf") )
   for wartezeit in wartezeitElements: 
    if wartezeit[0].text == None: 	# Element <stunden> hat keinen Wert 
     self.xmlnode_wartezeitproprozessdurchlauf_stunden = 0
    else:
     self.xmlnode_wartezeitproprozessdurchlauf_stunden = int(wartezeit[0].text)

    if wartezeit[1].text == None: 	# Element <minuten> hat keinen Wert
     self.xmlnode_wartezeitproprozessdurchlauf_minuten = 0
    else:
     self.xmlnode_wartezeitproprozessdurchlauf_minuten = int(wartezeit[1].text)

   prozesslaufzeitElements = list(e for e in root.iter("prozesslaufzeit") )
   for prozesslaufzeit in prozesslaufzeitElements: 
    if prozesslaufzeit[0].text == None: 	# Element <stunden> hat keinen Wert 
     self.xmlnode_prozesslaufzeit_stunden = 0
    else:
     self.xmlnode_prozesslaufzeit_stunden = int(prozesslaufzeit[0].text)

    if prozesslaufzeit[1].text == None: 	# Element <minuten> hat keinen Wert
     self.xmlnode_prozesslaufzeit_minuten = 0
    else:
     self.xmlnode_prozesslaufzeit_minuten = int(prozesslaufzeit[1].text)
  else:                                                           
   self.is_xml_loaded = False
# ************************************
# END **** CLASS xml file reading *******

# **** CLASS country codes through http request ********
# ************************************
class CountryCodes:
 countrycodeList = None
 httpApi = None
 totalcountries = None

 def __init__(self):
  self.httpApi = 'https://datahub.io/core/country-list/datapackage.json'  
  self.countrycodeList = []
  self.totalcountries = 0
  self.GetCountryCodesList()

# delivers a List[] of countries & their codes (2-stellig)  
# e.g [['Washington','United States'],['Salzburg','Austria'] ]
# https://datahub.io/core/country-list#python
 def HttpGetCountryCodesList(self):
  package = Package(self.httpApi)
  for resource in package.resources:
   if resource.descriptor['datahub']['type'] == 'derived/csv':
    self.countrycodeList = resource.read()
    for country in self.countrycodeList:
     print(country[0]," - ",country[1]) 
 

 # uses the pycountry modules
 # https://pypi.org/project/pycountry/#description
 def GetCountryCodesList(self):
  totalcountries = len(pycountry.countries)
  # alpha_2='DE', alpha_3='DEU', name='Germany', numeric='276', official_name='Federal Republic of Germany
  self.countrycodeList = pycountry.countries

# ************************************
# END **** CLASS country codes through http request *******


# **** CLASS timer counter ********
# *********************************
class ProgramSteuerungszaehler:
 
 counter = 1
 
 def __init__(self):
  self.counter = START_COUNTER_VALUE

 def zaehlerErhoehen(self):
  self.counter = self.counter + 1
 
 def zaehlerAnzeigen(self):
  print("Counter: ", self.counter)
# ************************************
# END **** CLASS timer counter *******

# **** CLASS Program execution Start *******
# ******************************************
class CMainExecution:
 oProgramControl = None
 objXmlReader    = None
 MAX_COUNTER_LIMIT = 1
 # MAX_PROCESS_RUNNING_TIME_IN_MINUTES = 120

 oMySqlConnector = None
 oWeatherDb      = None
 oCountryCodes   = None 
 oWetterDatenCSV = None
 startTime_in_seconds       = None

 def Initialize(self):
  self.oProgramControl    = ProgramSteuerungszaehler()
  self.objXmlReader       = XmlReader()
  self.oCountryCodes      = CountryCodes() # die Ländercodes & andere details werden geholt und die Liste befüllt worden.
  self.oWetterDatenCSV    = WetterDatenCSV()
  self.startTime_in_seconds          = time.time()

  if self.objXmlReader.is_xml_loaded == True:
   self.MAX_COUNTER_LIMIT = len(self.objXmlReader.dictOrtsnamen)
   # len(self.objXmlReader.dictOrtsnamen.keys())
   #self.oMySqlConnector = c.CMySqlConnection(None)
  else:
   self.MAX_COUNTER_LIMIT = 1

  # self.CalculateTotalProcessWaitingTimeInSeconds()
  self.CalculateTotalProcessRunningTimeInMinutes()
 
 def CalculateTotalProcessWaitingTimeInSeconds(self):
  if self.objXmlReader.xmlnode_wartezeitproprozessdurchlauf_stunden > 0:
   process_waiting_time_in_seconds = (self.objXmlReader.xmlnode_wartezeitproprozessdurchlauf_stunden*60)*60
  else:
   process_waiting_time_in_seconds = 0
   
  if self.objXmlReader.xmlnode_wartezeitproprozessdurchlauf_minuten > 0:
   process_waiting_time_in_seconds = process_waiting_time_in_seconds + (self.objXmlReader.xmlnode_wartezeitproprozessdurchlauf_minuten*60) 
  
  return process_waiting_time_in_seconds  #PROCESS_WAIT_TIME_SECONDS 


 def CalculateTotalProcessRunningTimeInMinutes(self):
  if self.objXmlReader.xmlnode_prozesslaufzeit_stunden  > 0:
   process_running_time_in_minutes = (self.objXmlReader.xmlnode_prozesslaufzeit_stunden*60)
  else:
   process_running_time_in_minutes = 0

  if self.objXmlReader.xmlnode_prozesslaufzeit_minuten  > 0:
   process_running_time_in_minutes = process_running_time_in_minutes + self.objXmlReader.xmlnode_prozesslaufzeit_minuten

  return process_running_time_in_minutes

 def __init__(self):
  self.Initialize()
  #self.oMySqlConnector  = c.CMySqlConnection()
  #self.oMySqlConnector.connectToDB()
  #self.oWeatherDb = c.CWeatherDb()   # create_engine is called & a engine object is initialized. 

  #if self.oWeatherDb.cmysqlconnection.connection_success == True:
   #print("DbWetter database engine initialization successful")
   #isTblCountryEmpty = self.oWeatherDb.IsCountryTableEmpty()
   
   #if isTblCountryEmpty == True:
    #self.oWeatherDb.InsertDataIntoTblCountry(self.oCountryCodes.countrycodeList) 
  #else:
   #print("Datenbank Verbindung fehlgeschlagen!")

# **********************************************
# **** END CLASS Program execution Start *******


objMain = CMainExecution()	

def ausfuehren():
 objMain.oProgramControl.zaehlerAnzeigen()
 if objMain.objXmlReader.is_xml_loaded == False:
  ort = "Salzburg"
 else:
  if objMain.oProgramControl.counter > objMain.MAX_COUNTER_LIMIT:
   objMain.oProgramControl.counter = 1
  # dictOrtsnamen Value is of type List[]
  # e.g. dictOrtsnamen[0] --> ['salzburg','austria']
  namecountrylist = objMain.objXmlReader.dictOrtsnamen[str(objMain.oProgramControl.counter)] 
  ort = namecountrylist[0] # e.g. ['Salzburg','Austria'] --> Salzburg

 weatherdata = []
 weatherdata = w.GetOrtWetterdaten(ort)
 
 objMain.oWetterDatenCSV.dictWetterdatenCsv = {}
 objMain.oWetterDatenCSV.check_exists_CSVFile()

 sLatLon = "latitudes:"
 for key in weatherdata:
  if key == "Latitude":
   sLatLon =sLatLon + str(weatherdata[key])
  elif key == "Longitude":
   sLatLon = sLatLon + " - longitude:" + str(weatherdata[key])
   print(sLatLon)
  else:
   print(key,"--> ",weatherdata[key])
   if objMain.oWetterDatenCSV.is_csv_vorhanden:
    if key == "Ort":
     objMain.oWetterDatenCSV.dictWetterdatenCsv["Ort"] = weatherdata[key]
    #self.oWetterDatenCSV.delimitedStringWeatherData = self.oWetterDatenCSV.delimitedStringWeatherData + weatherdata[key] + ";"
    elif key == "beschreibung":
   	 objMain.oWetterDatenCSV.dictWetterdatenCsv["Beschreibung"] = weatherdata[key]
    #self.oWetterDatenCSV.delimitedStringWeatherData = self.oWetterDatenCSV.delimitedStringWeatherData + weatherdata[key] + ";"   
    elif key == "aktuelletemperatur":
     objMain.oWetterDatenCSV.dictWetterdatenCsv["Aktuelletemperatur"] = weatherdata[key]
    #self.oWetterDatenCSV.delimitedStringWeatherData = self.oWetterDatenCSV.delimitedStringWeatherData + weatherdata[key] 
 
 if objMain.oWetterDatenCSV.is_csv_vorhanden:
  objMain.oWetterDatenCSV.append_to_CSV()

 objMain.oProgramControl.zaehlerErhoehen()

 #if objMain.oMySqlConnector.connection_success == True:
 # print("Datenbank Verbindung ist offen") 
 del weatherdata

def signal_handler(signum, frame):
 raise ProgramKilled
    
class Job(threading.Thread):

 def __init__(self, interval, execute, *args, **kwargs):
  threading.Thread.__init__(self)
  self.daemon = False
  self.stopped = threading.Event()
  self.interval = interval
  self.execute = execute
  self.args = args
  self.kwargs = kwargs

 def stop(self):
  self.stopped.set()
  self.join()	# wait for the time completion
    
 def run(self):
  while not self.stopped.wait(self.interval.total_seconds()):
   self.execute(*self.args, **self.kwargs)
            
if __name__ == "__main__":
 signal.signal(signal.SIGTERM, signal_handler)
 signal.signal(signal.SIGINT, signal_handler)
 
 PROCESS_WAIT_TIME_SECONDS = objMain.CalculateTotalProcessWaitingTimeInSeconds()
 MAX_PROCESS_RUNNING_TIME_IN_MINUTES = objMain.CalculateTotalProcessRunningTimeInMinutes()
 # PROCESS_WAIT_TIME_SECONDS = 8
 job = Job(interval=timedelta(seconds=PROCESS_WAIT_TIME_SECONDS), execute=ausfuehren)
 job.start()

 while True:
  try:
   time.sleep(2)
   current_time_in_seconds = time.time()
   elapsed_time_in_seconds = current_time_in_seconds - objMain.startTime_in_seconds
   elapsed_time_in_minutes = elapsed_time_in_seconds/60
   
   # MAX_PROCESS_RUNNING_TIME_IN_MINUTES = 2
   if elapsed_time_in_minutes >= MAX_PROCESS_RUNNING_TIME_IN_MINUTES:
    print("Die Programlaufzeit von " + MAX_PROCESS_RUNNING_TIME_IN_MINUTES + " minuten ist abgelaufen.")
    print(".....Program wird beendet")
    job.stop()
    break 

   #if objMain.oProgramControl.counter > objMain.MAX_COUNTER_LIMIT:
    #print("Program-Counter limit has reached: running cleanup code")
    #job.stop()
    #break
  except ProgramKilled:
   print ("Program killed: running cleanup code")
   job.stop()
   break
