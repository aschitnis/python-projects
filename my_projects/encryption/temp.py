import re
import pycountry as py
import mysqlconnectormodule as c
import json
import time
import requests as reqs 		# to use a requests package in the program
import tzlocal
from pytz import timezone
from datetime import datetime, timedelta
from timeloop import Timeloop
import threading, signal
from threading import Timer
from datapackage import Package


import pytz


# cryptography module link:
# https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
# 06.05.2020 10:00 abhijit
# a) run get-pip.py to install pip  {C:\Users\Mustermann\AppData\Local\Programs\Python\Python38-32\get-pip.py}
# b) run "pip install cryptography" to install cryptography module . 

# getAge is used to call a lambda function
getAge = lambda p: ageFunction(p)

def ageFunction(c):
 return 2020 - c

def FindAge(getAge):
 result = getAge
 print(result)

def GetListOfCountriesWithIsoCode():
 package = Package('https://datahub.io/core/country-list/datapackage.json')
 for resource in package.resources:
  if resource.descriptor['datahub']['type'] == 'derived/csv':
   print(len(resource.read()))
   data = resource.read()
   print("Total list of countries", len(data))
   for i in data:
    print(i[1], " - ", i[0])

def GetCountryCodesList():
 totalcountries = len(py.countries)
# alpha_2='DE', alpha_3='DEU', name='Germany', numeric='276', official_name='Federal Republic of Germany
 print("Total countries: ",totalcountries)
 countrylist = []
 countrylist = py.countries
 count = 1
 for country in countrylist:
  print(country.alpha_2,"-",country.name) 
  count = count + 1
  if count > 5:
   break
  else:   
   continue

def suche_orte_wie(ortsliste, wildcard):
 r = re.compile(wildcard +".*")
 gesuchteOrtsListe = list(name for name in ortsliste if r.match(name))
 return gesuchteOrtsListe 

def timeout(firstname, city=None):
 print("Die Parametern sind firstname: {},city: {}".format(firstname,city))

def signal_handler(signum, frame):
 raise ProgramKilled
# ********************************************************
# **************  main program  **************************
# ********************************************************

if __name__ == "__main__":
#result = sum(25)
#print(result)

 signal.signal(signal.SIGTERM, signal_handler)
 signal.signal(signal.SIGINT, signal_handler)
 
 GetCountryCodesList()
 oweatherdata = c.CWeatherDb()
 oweatherdata.cmysqlconnection.connectToDB()
 if oweatherdata.cmysqlconnection.connection_success == True:
  print("connetion success")
  oweatherdata.GetCityTabledata()
  if oweatherdata.city_details_dictionary:
   for key in oweatherdata.city_details_dictionary:
    print(key, " - ", oweatherdata.city_details_dictionary[key]) 
   # GetListOfCountriesWithIsoCode()
    
 else:
 	print("Database not available!!!")
 
 FindAge(getAge(1971))
 listnum = list(x for x in range(10) if x%2 == 0)
 ortsliste = ["salzburg","saalfelden","ebenau","sankt gilgen","eugendorf","salzburg aigen","salzburg flughafen"]
 resultliste = suche_orte_wie(ortsliste,"sa")
 print(resultliste)
 
 staedteliste = ["Salzburg","Dhaka","New Orleans"]
 # self.oMySqlConnector = c.CMySqlConnection()


 #t = Timer(60,timeout,args=["abhijit"], kwargs={"city":"mumbai"})
 #t.start()
 #t.join()




