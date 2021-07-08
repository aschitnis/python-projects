# abhijit 28.05.2020 salzburg 09:33 AM
# for installation of mysql refer to readme.txt under "C:\My_Journal\freecodecamp\python\mysql_dbapi"
# tutorial link : https://pynative.com/python-mysql-tutorial

# Dokumentation: https://pynative.com/python-mysql-database-connection/
# pip install mysql-connector-python
import mysql.connector	
from mysql.connector import Error

# List of countries & their ISO codes.
# Link: https://pypi.org/project/pycountry/#description
# pip install pycountry
import pycountry
import time

# Dokumentation: https://docs.sqlalchemy.org/en/13/core/connections.html#
# pip install SQLAlchemy
from sqlalchemy import create_engine 

class CMySqlConnection:
 
 mysqlengine = None
 # The Connection object returned by the create_engine method
 connectionobject = None # used with the sqlalchemy module
 connectionstring = None # used as param to create_engine(param) method.

 connection_success = False

 connection = None # used with the mysql.connector module
 dbbaeumerconfig = None
 dbwetterconfig = None

 def __init__(self, connString = None):
  self.connection_success = False
  if connString != None:
   self.connectionstring = connString

  self.dbbaeumerconfig = {
           'user':'root',
           'password':'Elfriede51',
           'host':'localhost',
           'database':'dbbaeumertransactions'    
          }
  self.dbwetterconfig = {
           'user':'root',
           'password':'Elfriede51',
           'host':'localhost',
           'database':'dbwetter'    
          }

 # https://docs.sqlalchemy.org/en/13/core/connections.html#
 # uses the sqlalchemy/create_engine module.
 def CreateEngine(self):
  self.mysqlengine = create_engine(self.connectionstring)

  # If a mySQLdb operational error is thrown, please run the following command in MySql-Workbench.
  # e.g. ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Elfriede51'
  self.connectionobject = self.mysqlengine.connect()
  if self.connectionobject.closed == False:
   self.connection_success = True
  else:
   self.connection_success = False
  
  
# uses the mysql.connector module. 
# This method is only used to check if a connection to the DB can be established or not.
# All other Queries to the DB are run using the sqlalchemy module.
 def connectToDB(self):  
  self.connection_success = False
  try:
   self.connection = mysql.connector.connect(**self.dbwetterconfig)
 # host='localhost',database='dbwetterconfig',user='root',password='Elfriede51',connection_timeout=1000
   if self.connection.is_connected():
    self.connection_success = True
  #db_Info = connection.get_server_info()
  # print("Connected to MySql Server version ",db_Info)
  #cursor = connection.cursor()
  #result = cursor.execute("select * from tblcustomer;")
  #record = cursor.fetchall()
  # for row in records
  except Error as e:
   self.connection_success = False
   print("Connection has failed - ", e)
  finally:
   if self.connection_success == True:
    if self.connection.is_connected():
     #cursor.close()
     self.connection.close()



# 'mysql://root:Elfriede51@localhost/dbwetter'
class CWeatherDb:
 cmysqlconnection = None
 city_details_dictionary = {} 	 # Key:city Value:Id aus der tabelle tblcity
 country_details_dictionary = {} # Key: (tblcountry.column)country_Id & Value: (tblcountry.column)alpha_2 aus tblcountry 

 def __init__(self): 
  self.cmysqlconnection = CMySqlConnection('mysql://root:Elfriede51@localhost/dbwetter')
  self.cmysqlconnection.CreateEngine()
 
 def IsCountryTableEmpty(self):
  istableempty = True
  if self.cmysqlconnection.connectionobject.closed == False:
   self.cmysqlconnection.connection_success = True
   result = self.cmysqlconnection.connectionobject.execute("select country_Id, alpha_2 from tblcountry")
   if result.rowcount > 0:
    istableempty = False
    #for row in result:
    # self.country_details_dictionary[row['country_Id']] = row['alpha_2']  # e.g. country_Id:1, alpha_2:DE 
  else:
   self.cmysqlconnection.connection_success = False
   print("Die Verbindung ist geschlossen. Abfrage kann nicht durchgeführt werden.")
  return istableempty     
 
 def InsertDataIntoTblCountry(self, countriesDetailsList):
  if self.cmysqlconnection.connectionobject.closed == True:
   self.cmysqlconnection.connectionobject = self.cmysqlconnection.mysqlengine.connect()  
  
  incrementalCount = 1
  with self.cmysqlconnection.connectionobject.begin():	# opens a transaction
   for country in countriesDetailsList:
   	# alpha_2='DE', alpha_3='DEU', name='Germany', numeric='276', official_name='Federal Republic of Germany
    #self.cmysqlconnection.connectionobject.execute("INSERT INTO tblcountry (country_Id, nameEN, officialname, alpha_2, alpha_3) VALUES (%s,%s,%s,%s,%s)", incrementalCount, country.name, country.official_name, country.alpha_2, country.alpha_3) 
    incrementalCount = incrementalCount + 1
     

 def GetCityTabledata(self):
  if self.cmysqlconnection.connectionobject.closed == False:
   self.cmysqlconnection.connection_success = True
   result = self.cmysqlconnection.connectionobject.execute("select city_id,country_id,name,citydescription,latitude,longitude from tblcity")
   if result.rowcount > 0:
    for row in result:
     self.city_details_dictionary[row['city_id']] = row['name']
  else:
   self.cmysqlconnection.connection_success = False
   print("Die Verbindung ist geschlossen. Abfrage kann nicht durchgeführt werden.")      