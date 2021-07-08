# um eine XML-Datei zulesen/parsen
# https://docs.python.org/3/library/xml.etree.elementtree.html
import xml.etree.ElementTree as ET 
                                   
import re   # regex module
import os   # Datei lesen/schreiben

# cryptography module link:
# https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
# 06.05.2020 10:00 abhijit
# a) run get-pip.py to install pip  {C:\Users\Mustermann\AppData\Local\Programs\Python\Python38-32\get-pip.py}
# b) run "pip install cryptography" to install cryptography module . 
from cryptography.fernet import Fernet

# topic_userData_dictionary = {} 

# **************************  Methods / functions (Encryption & Decryption)
def write_key():
 if os.path.exists("key.key") == True:
  delete_file("key.key")
 else:
  print("key.key Datei nicht vorhanden. Eine neue Key-Datei wird generiert")

 key = Fernet.generate_key()
 with open("key.key", "wb") as key_file:
  key_file.write(key) 

def load_key():
 return open("key.key", "rb").read()

def encrypt(normalfilename,encryptedfilename, key):
 f = Fernet(key)
 with open(normalfilename, "rb") as file:
  #read all the file data
  file_data = file.read()
  #encrypt the file data
  encrypted_data = f.encrypt(file_data) 
  # write the encrypted file
  with open(encryptedfilename, "wb") as file:
   file.write(encrypted_data)   

def decrypt(encryptedfilename, decryptedfilename, key):
 f = Fernet(key)
 with open(encryptedfilename, "rb") as file:
 # read the encrypted data
  encrypted_data = file.read()
 # decrypt data
  decrypted_data = f.decrypt(encrypted_data)
 # write the original file
  with open(decryptedfilename, "wb") as file:
   file.write(decrypted_data)
# ***************************************************************************

# ******************************  Methods 
def delete_file(filepath):
 if os.path.exists(filepath):
  os.remove(filepath)
 else:
  print("File not found in the directory")

def get_topics():
 root = tree.getroot()
 for topics in root:
  for topic in topics:
   print(topic.tag,topic.attrib)

def get_all_subelements_in_root():
 root = tree.getroot()
 selements = [elem.tag for elem in root.iter()]
 for name in selements:
  print(name)

def demozweck(topicvalue):
 root = tree.getroot()
 r = re.compile(topicvalue +".*")
 topicElements = list(t for t in root.iter("topic") if r.match(t.attrib.get("name") )  )
 listelementtopics = list(elem for elem in topicElements)
 listelementusers = list(user for user in listelementtopics if user.tag == "user")
 listelementsecuritydata = list(sec for sec in listelementusers if sec.tag == "securitydata")

 for topicelement in listelementtopics:
  print("-------------------------------------------------------------------")
  print(topicelement.attrib.get("name"))
  users = list(u for u in topicelement if u.tag == "user" and (u.attrib.get("name") or u.attrib.get("password") ) )
  # prüf ob die ElementListe "users" nicht leer ist
  if users: 
   print("Benutzer: " + users[0].attrib.get("name"))
   print("Password: " + users[0].attrib.get("password"))

# ----------------------  Element Securitydata (gehört zum Child-Element vom user)  -----------------------------

   for user in users:
    for sec in user:
     if sec.tag == "securitydata":
      if sec.text:
       print("**** Security data: ", sec.text)
       #print(sec.text)
       #break
      else:
       print("Security-data nicht vorhanden")
       #break
     if sec.tag == "addtdata":
      if sec.text:
       print("zusätz. Daten: ", sec.text)
      else:
       print("zusätz. daten nicht vorhanden")
     if sec.tag == "contractnumber":
      if sec.text:
       print("Contract-Number: ", sec.text)
      else:
       print("Contract-Number daten nicht vorhanden")
     if sec.tag == "pin":
      if sec.text:
       print("PIN: ", sec.text)
      else:
       print("PIN nicht vorhanden")
     if sec.tag == "web":
      if sec.text:
       print("web link: ", sec.text)
      else:
       print("web-link nicht vorhanden") 
     if sec.tag == "weblogin":
      if sec.text:
       print("web login: ", sec.text)
      else:
       print("web login daten nicht vorhanden")
     if sec.tag == "debitcard":
      print("**** DEBITKARTE DETAILS ******** ")
      for debitcarddetails in sec:
       if debitcarddetails.tag == "number":
        if debitcarddetails.text:
         print("debitcard Nummer: ", debitcarddetails.text)
        else:
         print("Debitkartennummer nicht vorhanden")
       if debitcarddetails.tag == "cvv":
        if debitcarddetails.text:
         print("debitcard CVV: ", debitcarddetails.text)
        else:
         print("Debitkarten-CVV Nummer nicht vorhanden")
       if debitcarddetails.tag == "pin":
        if debitcarddetails.text:
         print("debitcard PIN: ", debitcarddetails.text)
        else:
         print("Debitkarten-PIN Nummer nicht vorhanden")
      print("**** DEBITKARTE DETAILS ENDE ******* ", sec.text)
     if sec.tag == "branchDetails":
      print("*****BRANCH DETAILS ******")
      for branchdetail in sec:
       if branchdetail.tag == "branchPhone":
        if branchdetail.text:
         print("Telefon: ", branchdetail.text)
        else:
         print("Branch-telefon nicht vorhanden")
       if branchdetail.tag == "branchCode":
        if branchdetail.text:
         print("branch code: ", branchdetail.text)
        else:
         print("branch code daten nicht vorhanden")
       if branchdetail.tag == "branchName":
        if branchdetail.text:
         print("branch Name: ", branchdetail.text)
        else:
         print("branch-name daten nicht vorhanden")
       if branchdetail.tag == "branchAddress":
        if branchdetail.text:
         print("branch.address: ", branchdetail.text)
        else:
         print("branch-address ist nicht vorhanden")
      print("*****BRANCH DETAILS ENDE ******")                    
     if sec.tag == "accountDetails":
      print("*****ACCOUNT DETAILS ******")
      for accountdetail in sec:
       if accountdetail.tag == "accountType":
        if accountdetail.text:
         print("A/c type: ", accountdetail.text)
        else:
         print("A/c type nicht vorhanden")
       if accountdetail.tag == "accountNumber":
        if accountdetail.text:
         print("A/c number: ", accountdetail.text)
        else:
         print("A/c number nicht vorhanden")
       if accountdetail.tag == "accountProductType":
        if accountdetail.text:
         print("A/c product-type: ", accountdetail.text)
        else:
         print("A/c product-type nicht vorhanden")
      print("*****ACCOUNT DETAILS ENDE ******")
     else:                           
      continue      
      #print("Security-data nicht vorhanden")
      #break
# ---------------------- ENDE Securitydata ---------------------------------

   #listsecuritydata = list(user for user in users for sec in user if sec.tag == "securitydata")
   #for s2 in listsecuritydata:
   # print("*** Securitydata: ")
   # print(s2.tag)

  
  

# search & get all topic elements where 
#the value of the topic-attribute 'name' is %topicvalue% 
def get_topics(topicvalue):

 root = tree.getroot()
 r = re.compile(topicvalue +".*")				# set regex search-string 
												                # for <topic name="xxxxx"> 
												                # e.g.'hdf.*' as search-string 
												                # will find <topic name="hdfc bank"> 

 # loop over the list of all child <topic> elements in the <topics> element  
 for topic in root.iter("topic"):				
  topicElement_attribute_value = topic.attrib.get("name")	# get the value of the 'name' attribute 
												                      # of the <topic> element. e.g. <topic name="xxx">
    
  if r.match(topicElement_attribute_value):
   list_topicSubElements =[elem for elem in topic.iter()] # get the <topic> element &
                                                          # all the direct child-elements 
														                              # belonging to the <topic> element. 

   strTopicName =  list_topicSubElements[0].attrib.get("name")	# <topic name="xxxxx">
   print("Topic: " + strTopicName)	

   # get the <user> element & all it's sub-elements
   userElement = [elemSub for elemSub in list_topicSubElements if elemSub.tag == "user"]

   # the name & password attribute belonging to the <user> element.
   # <user name="xxx" password="****">
   if userElement[0].attrib.get("name") and userElement[0].attrib.get("password"):  # if name & password are not empty
    print("Benutzer: "+userElement[0].attrib.get("name"))
    print("Kennwort: "+userElement[0].attrib.get("password"))     
   else:
    print("Benutzer und Kennwortdaten sind nicht vorhanden")     
    
   # loop over the child-elements of the <user/> element. 
   for usrChildElementslist in userElement:   # usrChildElementslist is a List of all child-elements 
                                              # belonging to the <user> element.

    # loop over the List of all child-elements belonging to the <user> element	  
    print("------ Sicherheitsdaten ------------------------")
    for userChildElement in usrChildElementslist:
     if userChildElement.tag == "securitydata":
      if userChildElement.text:	  
       print(userChildElement.text)
       print("----------------------------------------------------------")
      else: 
       print("sicherheitsdaten nicht vorhanden")
       print("----------------------------------------------------------")
       break
     else:
      pass	   
    break; # for usrChildElementslist in userElement
     # ---- delete code 	 
    #else:
    # print("Benutzer, Kennwort & Sicherheitsdaten sind nicht vorhanden") 
     # ----- end of delete code
  else:		# if regex-match for the value 
            # of topic-attribute 'name' was not found
   continue  


# *****************************************************************   
# ************  program starts from here **************************
# *****************************************************************  
encryptfile = input("wollen Sie die Datei neu verschlüsseln ? j/n: ")
if encryptfile == "j":
 write_key()
 newkey = load_key()
 encrypt("what.xml","what.txt",newkey)
else:
 if os.path.exists("what.xml") == True:
  delete_file("what.xml")

 key = load_key()
 decrypt("what.txt","what.xml",key)
 tree = ET.parse("what.xml")
 delete_file("what.xml")
 topicname = input("Name eingeben: ")
 demozweck(topicname)

createdecryptedFile = input("Wollen Sie die Datei entschlüsseln und beibehalten ? j/n: ")
if createdecryptedFile == "j":
 key = load_key()
 decrypt("what.txt","what.xml",key)
else:
 print("program wird beendet.....")  
#get_topics(topicname)


  






