import threading, time, signal
import httpweathermodule as w
import requests as reqs
import os
import xml.etree.ElementTree as ET
from timeloop import Timeloop
from datetime import timedelta

WAIT_TIME_SECONDS = 5
MAX_COUNTER_LIMIT = 1
START_COUNTER_VALUE = 1

class ProgramKilled(Exception):
 pass

class XmlReader:
 dictOrtsnamen = {}
 is_xml_loaded = False

 def __init__(self):
  self.is_xml_loaded = False
  self.dictOrtsnamen = {}
  self.loadXml()

 def loadXml(self):
  if os.path.exists("orte.xml") == True:
   tree = ET.parse("orte.xml")
   self.is_xml_loaded = True
    
   root = tree.getroot()
   ortElements = list(e for e in root.iter("ort") )
   for ort in ortElements:	# ort.tag == "ort"
    self.dictOrtsnamen[ort[0].text] = ort[1].text	# ort[0].tag = 'id'
                                                    # ort[1].tag = 'name'


class ProgramSteuerungszaehler:
 
 counter = 1
 
 def __init__(self):
  self.counter = START_COUNTER_VALUE

 def zaehlerErhoehen(self):
  self.counter = self.counter + 1
 
 def zaehlerAnzeigen(self):
  print("Counter: ", self.counter)

class CMainExecution:
 oProgramControl = None
 objXmlReader    = None
 MAX_COUNTER_LIMIT = 1

 def Initialize(self):
  self.oProgramControl = ProgramSteuerungszaehler()
  self.objXmlReader = XmlReader()
  if self.objXmlReader.is_xml_loaded == True:
   self.MAX_COUNTER_LIMIT = len(self.objXmlReader.dictOrtsnamen.keys())
  else:
   self.MAX_COUNTER_LIMIT = 1

 def __init__(self):
  self.Initialize()

objMain = CMainExecution()	

def ausfuehren():
 objMain.oProgramControl.zaehlerAnzeigen()
 if objMain.objXmlReader.is_xml_loaded == False:
  ort = "salzburg"
 else:
  ort = objMain.objXmlReader.dictOrtsnamen[str(objMain.oProgramControl.counter)]

 weatherdata = {}
 weatherdata = w.GetOrtWetterdaten(ort)
 sLatLon = "latitudes:"
 for key in weatherdata:
  if key == "Latitude":
   sLatLon =sLatLon + str(weatherdata[key])
  elif key == "Longitude":
   sLatLon = sLatLon + " - longitude:" + str(weatherdata[key])
   print(sLatLon)
  else:
   print(key,"--> ",weatherdata[key])

 objMain.oProgramControl.zaehlerErhoehen()  
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

 job = Job(interval=timedelta(seconds=WAIT_TIME_SECONDS), execute=ausfuehren)
 job.start()

 while True:
  try:
   time.sleep(1)
   if objMain.oProgramControl.counter > objMain.MAX_COUNTER_LIMIT:
    print("Program-Counter limit has reached: running cleanup code")
    job.stop()
    break
  except ProgramKilled:
   print ("Program killed: running cleanup code")
   job.stop()
   break
