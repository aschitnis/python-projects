import os
import xml.etree.ElementTree as ET

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

# **** CLASS xml file reading ********
# ************************************
class XmlReader:
 dictBookNames = {} # key is <id> 
                    # value is a List[] i.e. [<name>,<country>]. See Xml file ortefuerwetterabfragen.xml.
 is_xml_loaded = False
 XMLQUERYFILE = "books.xml"  

 def __init__(self):
  self.is_xml_loaded = False
 
  # a dictionary with Key of type String and Value of type List[].
  # e.g. Key=1 and Value=['salzburg','austria']
  self.dictBookNames = {} 
  self.loadXml()

 # load and parse the Xml file.
 # save the values of the Rootnode '<ort>' node-elements in a dictionary.
 # save the values of the Rootnode '<zeitablauf>' node-elements in class variables.
 def loadXml(self):
  if os.path.exists(self.XMLQUERYFILE) == True:
   tree = ET.parse(self.XMLQUERYFILE)

   root = tree.getroot()
   bookElements = list(e for e in root.iter("book") )
   for book in bookElements:	# book.tag == "book"
    self.dictBookNames[book[0].text] = [book[1].text,book[2].text,book[3].text]	  # book[0].tag = 'id'.   e.g. book[0].text = '1' (this is the KEY)
                                                                  # book[1].tag = 'name'. e.g. book[1].text = 'tulsi saheb ki shabdavali' (this is the VALUE)
  																  # book[2].tag = 'author'. e.g. book[2].text = 'tulsi saheb' (this is the VALUE)
                                                                  # book[3].tag = 'information'. e.g. book[3].text = 'part 1 and 2' (this is the VALUE)
   self.is_xml_loaded = True
  else:                                                           
   self.is_xml_loaded = False
# ************************************
# END **** CLASS xml file reading *******


# **** CLASS Program execution Start *******
# ******************************************
class CMainExecution:
 objXmlReader    = None
 bookData = []

 def Initialize(self):
  self.objXmlReader       = XmlReader()
 
 def SearchBooksByAuthor(self,author):
  for index, key in enumerate(self.objXmlReader.dictBookNames):
   bookData = self.objXmlReader.dictBookNames[key]
   if bookData[1].startswith(author) == True:
    strResult = "Name: "+bookData[0]+" author: "+bookData[1]
    if bookData[2]:
     strResult = strResult + "  information: " + bookData[2]
     print(strResult)
    else:
     print(strResult)
    # print("Name: "+bookData[0]+" author: "+bookData[1] )
    #if bookData[2]:
    # print("information: " + bookData[2])
    print(" -------------------------------------------------------- ")    
  
 def __init__(self):
  self.Initialize()

# **********************************************
# **** END CLASS Program execution Start *******


objMain = CMainExecution()	

def ausfuehren():
 if objMain.objXmlReader.is_xml_loaded == False:
  print("..... error reading xml file: searchbooks.xml")  
  #ort = "Salzburg"
 else:
  searchParameter = input("1 ")
  objMain.SearchBooksByAuthor(searchParameter)

  # dictBookNames Value is of type List[]
  # e.g. dictBookNames[0] --> ['tulsi saheb ki shabdavali','tulsi sahib','part 1 and 2']
  #bookData = objMain.objXmlReader.dictBookNames['1']
  #print(bookData)  
  
ausfuehren()