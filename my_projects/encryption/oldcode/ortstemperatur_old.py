import requests as reqs 		# to use a REST requests package in the program
# import temperaturmessung as t

def GetOrtWetterdaten(city):
 dictWetterdatenfuerOrt = {}	# declare a Dictionary for storing the weather data for the city

 response = reqs.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&lang=de&appid=98ec98ab7c0f616ddae7a6c4be445e58")
  
 jsonRes = response.json()
 dictWetterdatenfuerOrt["Ort"] = jsonRes["name"]
 dictWetterdatenfuerOrt["Latitude"] = jsonRes["coord"]["lat"]
 dictWetterdatenfuerOrt["Longitude"] = jsonRes["coord"]["lon"]

 dictWetterdatenfuerOrt["beschreibung"] = jsonRes['weather'][0]['description'] 	# description z.b. Ein paar wolken usw...
 
 faktuelletemperatur = t.KelvinToCelcius(jsonRes['main']['temp'])		# präfix 'f' bedeutet ein float-wert
 saktuelletemperatur = "{:4.2f}".format(faktuelletemperatur)
 saktuelletemperatur = saktuelletemperatur + "°C"
 dictWetterdatenfuerOrt["aktuelletemperatur"] = saktuelletemperatur

 ffuehltemperatur = t.KelvinToCelcius(jsonRes['main']['feels_like'])		# präfix 'f' bedeutet ein float-wert
 sfuehltemperatur = "{:4.2f}".format(ffuehltemperatur)
 sfuehltemperatur = sfuehltemperatur + "°C"
 dictWetterdatenfuerOrt["fuehltemperatur"] = sfuehltemperatur
 
 fmintemperatur = t.KelvinToCelcius(jsonRes['main']['temp_min'])		# präfix 'f' bedeutet ein float-wert
 smintemperatur = "{:4.2f}".format(fmintemperatur)
 smintemperatur = smintemperatur + "°C"
 dictWetterdatenfuerOrt["minimumtemperatur"] = smintemperatur
 
 fmaxtemperatur = t.KelvinToCelcius(jsonRes['main']['temp_max'])		# präfix 'f' bedeutet ein float-wert
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
 sunrise_time = t.GetSonnenZeit(sunrise,utcTimeHoursMin)
 dictWetterdatenfuerOrt["sonnenaufgang"] = sunrise_time.strftime("%Y-%m-%d %H:%M:%S")

 intSunset = jsonRes['sys']['sunset']
 sunset_time = t.GetSonnenZeit(intSunset,utcTimeHoursMin)
 dictWetterdatenfuerOrt["sonnenuntergang"] = sunset_time.strftime("%Y-%m-%d %H:%M:%S")
 
 ortszeit = t.GetCurrenttime(utcTimeHoursMin)
 dictWetterdatenfuerOrt["ortszeit"] = ortszeit.strftime("%Y-%m-%d %H:%M:%S")

 return dictWetterdatenfuerOrt

# -------- PROGRAM BEGIND HERE  ------------------------------------------
ortsname = input("Ortsname eingeben: ")
weatherdata = GetOrtWetterdaten(ortsname)
sLatLon = "latitude:"
for key in weatherdata:
 if key == "Latitude":
  sLatLon =sLatLon + str(weatherdata[key])
 elif key == "Longitude":
  sLatLon = sLatLon + " - longitude:" + str(weatherdata[key])
  print(sLatLon)
 else:
  print(key,"--> ",weatherdata[key]) 

#print(" ------------------ SALZBURG  --------------------- ")
#tz_SBG = timezone("Europe/Moscow")
#datetime_Salzburg = datetime.now(tz_SBG)
#print(datetime_Salzburg.strftime("%H:%M:%S"))

#print(' '.join(pytz.country_timezones['au']))
#listtimezonesforcountry = pytz.country_timezones['au']
#print(listtimezonesforcountry[3])

