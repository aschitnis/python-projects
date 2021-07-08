import requests as reqs 		# to use a REST requests package in the program

# Install-Manager exec path : C:\Users\Mustermann\AppData\Local\Programs\Python\Python38-32
# Install-Manager		  : aktuelle pip version 20.1 am 22.05.2020
# Upgrade Install-Manager : pip install --upgrade pip


# current time of a timezone module link:
# http://pytz.sourceforge.net/ 
# 06.05.2020 10:00 abhijit
# a) run get-pip.py to install pip  {C:\Users\Mustermann\AppData\Local\Programs\Python\Python38-32\get-pip.py}
# b) run "pip install pytz" to install timezone-times module .
from datetime import datetime, timedelta
from pytz import timezone
from pytz import common_timezones	# common_timezones is a list of useful, current timezones 
from pytz import all_timezones 		# all_timezones is the exhaustive list of the timezone names that can be used
from pytz import country_timezones	# country_timezones is a list of timezones used by a particular country. 
import pytz
import time

# REST Schnittstelle 
# ********** https://openweathermap.org/current#data
# username: aschitnis@hotmail.com 
# password: elfriede 

# Sonnenauf/untergang Zeiten berechnet mit Bezug auf UTC-time)
# zeitInSekunden : Sonnenaufgang oder Sonnenuntergang Zeit in Sekunden
def GetSonnenZeit(zeitInSekunden, utcVomOrt):
 utcOesterreich = 2	# UTC Österreich ist +2 Stunden
 utcDifferenz =  utcVomOrt - utcOesterreich
 
 timestamp = zeitInSekunden
 # Umwandlung Sekunden in Datum-Uhrzeit Format (Objekt)
 dt_object = datetime.fromtimestamp(timestamp) + timedelta(hours=utcDifferenz)
 return dt_object

def GetCurrenttime(utcVomZielOrt):
 utcOesterreich = 2	# UTC Österreich ist +2 Stunden
 utcDifferenz =  utcVomZielOrt - utcOesterreich
 
 # Umwandlung Sekunden in Datum-Uhrzeit Format (für Österreich)
 dt_object = datetime.fromtimestamp(time.time()) + timedelta(hours=utcDifferenz)
 return dt_object

def KelvinToCelcius(kelvin):
 return kelvin - 273.15

def GetOrtWetterdaten(city):
 dictWetterdatenfuerOrt = {}	# declare a Dictionary for storing the weather data for the city

 response = reqs.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&lang=de&appid=98ec98ab7c0f616ddae7a6c4be445e58")
  
 jsonRes = response.json()
 dictWetterdatenfuerOrt["Ort"] = jsonRes["name"]
 dictWetterdatenfuerOrt["Latitude"] = jsonRes["coord"]["lat"]
 dictWetterdatenfuerOrt["Longitude"] = jsonRes["coord"]["lon"]

 dictWetterdatenfuerOrt["beschreibung"] = jsonRes['weather'][0]['description'] 	# description z.b. Ein paar wolken usw...
 
 faktuelletemperatur = KelvinToCelcius(jsonRes['main']['temp'])		# präfix 'f' bedeutet ein float-wert
 saktuelletemperatur = "{:4.2f}".format(faktuelletemperatur)
 saktuelletemperatur = saktuelletemperatur + "°C"
 dictWetterdatenfuerOrt["aktuelletemperatur"] = saktuelletemperatur

 ffuehltemperatur = KelvinToCelcius(jsonRes['main']['feels_like'])		# präfix 'f' bedeutet ein float-wert
 sfuehltemperatur = "{:4.2f}".format(ffuehltemperatur)
 sfuehltemperatur = sfuehltemperatur + "°C"
 dictWetterdatenfuerOrt["fuehltemperatur"] = sfuehltemperatur
 
 fmintemperatur = KelvinToCelcius(jsonRes['main']['temp_min'])		# präfix 'f' bedeutet ein float-wert
 smintemperatur = "{:4.2f}".format(fmintemperatur)
 smintemperatur = smintemperatur + "°C"
 dictWetterdatenfuerOrt["minimumtemperatur"] = smintemperatur
 
 fmaxtemperatur = KelvinToCelcius(jsonRes['main']['temp_max'])		# präfix 'f' bedeutet ein float-wert
 smaxtemperatur = "{:4.2f}".format(fmaxtemperatur)
 smaxtemperatur = smaxtemperatur + "°C"
 dictWetterdatenfuerOrt["maximumtemperatur"] = smaxtemperatur

 iluftdruck = jsonRes['main']['pressure']
 sluftdruck = str(iluftdruck) + " hPa"		# liefert ein integer-wert. 
 											# Mit 'str' wird er im String umgewandelt
 dictWetterdatenfuerOrt["luftdruck"] = sluftdruck
 if jsonRes.get('visibility'):
  svisibility = str(jsonRes['visibility']) + " meter"
 else:
  svisibility = "n.v."
 dictWetterdatenfuerOrt["sicht"] = svisibility
 
 shumidity = str(jsonRes['main']['humidity']) + " %"
 dictWetterdatenfuerOrt["luftfeuchtigkeit"] = shumidity
 
 windspeedInkms = jsonRes['wind']['speed'] / 1000 
 swind =  str("{:8.5f}".format(windspeedInkms))
 swind = swind + " km/s"
 dictWetterdatenfuerOrt["wind"] = swind
 
 # [timezone] Wert ist in sekunden. 
 # Deswegen die entsprechende Umwandlung.
 utcTimeHoursMin = (jsonRes['timezone'] / 60) / 60 
 if utcTimeHoursMin < 0:
  stimezone = "UTC " + str(utcTimeHoursMin)
 else:
  stimezone = "UTC +" + str(utcTimeHoursMin) 
 dictWetterdatenfuerOrt["utcZeitzone"] = stimezone
 
 sunrise = jsonRes['sys']['sunrise']
 sunrise_time = GetSonnenZeit(sunrise,utcTimeHoursMin)
 dictWetterdatenfuerOrt["sonnenaufgang"] = sunrise_time.strftime("%Y-%m-%d %H:%M:%S")

 intSunset = jsonRes['sys']['sunset']
 sunset_time = GetSonnenZeit(intSunset,utcTimeHoursMin)
 dictWetterdatenfuerOrt["sonnenuntergang"] = sunset_time.strftime("%Y-%m-%d %H:%M:%S")
 
 ortszeit = GetCurrenttime(utcTimeHoursMin)
 dictWetterdatenfuerOrt["ortszeit"] = ortszeit.strftime("%Y-%m-%d %H:%M:%S")

 return dictWetterdatenfuerOrt   