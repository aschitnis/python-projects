import time
import os
import xml.etree.ElementTree as ET
from datetime import datetime, timezone


# **** CLASS xml file reading ********
# ************************************
class XmlReader:
 dictOrtsnamen = {} # key is <id> 
                    # value is a List[] i.e. [<name>,<country>]. See Xml file ortefuerwetterabfragen.xml.
 xmlFileName = None

 def __init__(self):
  self.xmlFileName = "weatherdataquery.xml" 
 
 def loadXml(self):
  FUNCTION_EXECUTION_WAITINGTIME_IN_SECONDS = None

  if os.path.exists(self.xmlFileName) == True:
   tree = ET.parse(self.xmlFileName)
   self.is_xml_loaded = True
   
   total_wait_time_in_seconds = 0
   wait_time_in_minutes = 0

   root = tree.getroot()
   zeitElements = list(e for e in root.iter("zeitablauf") )
   for zeit in zeitElements:
    if zeit[0].text == None:
     print("Stunden sind nicht angegeben worden")
     total_wait_time_in_seconds = 0
    else:
     total_wait_time_in_seconds = (int(zeit[0].text) * 60)*60
     print("stunden: ",zeit[0].text)

    if zeit[1].text == None:
     print("Minuten sind nicht angegeben worden")
    else:
     total_wait_time_in_seconds = total_wait_time_in_seconds + int(zeit[1].text) * 60       
     print("minuten: ",zeit[1].text)

   print("Total waiting time (seconds) -", total_wait_time_in_seconds)       
    #else:
     #print("Sunden sind nicht angegeben worden")
    
    #self.dictOrtsnamen[ort[0].text] = [ort[1].text,ort[2].text]	  # ort[0].tag = 'id'.   e.g. ort[0].text = '1' (this is the KEY)
                                                                  # ort[1].tag = 'name'. e.g. ort[1].text = 'salzburg' (this is the VALUE)
  else:                                                           # ort[2].tag = 'country'. e.g. ort[2].text = 'austria' (this is the VALUE)
   print("Error reading XMl file!")


oXmlRead = XmlReader()
oXmlRead.loadXml()
#utcTimeHoursMin = (timezone / 60) / 60 
#print("today's time: ", datetime.now(None))
#print("UTC time: ", datetime.now(timezone.utc))

#start_time = time.time()

#minutes = 1

#while True:
 #current_time = time.time()
 #elapsed_time_in_seconds = current_time - start_time
 #elapsed_time_in_minutes = elapsed_time_in_seconds/60
 #if elapsed_time_in_minutes > minutes:
 # print("Finished iterating in: " + str(int(elapsed_time_in_minutes))  + " seconds")
 # break
 #else:
 # print("minuten: ", elapsed_time_in_minutes)
  