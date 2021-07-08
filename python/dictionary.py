import re

list_orte = []
list_alle_orte = []

plz_ortsteile = {}
plz_ortsteile["5020"] = data = ["Alpensiedlung","Altstadt","Elisabeth-Vorstadt","Gaisberg","Gneis"]
plz_ortsteile["5400"] = data = ["Adneter Riedl","Au","Burgfried","Gamp","Greis","Hallein"]
plz_ortsteile["5280"] = data = ["Braunau Neustadt","Braunau am Inn","Gasteig","Haiden","Haselbach","Höft"]
plz_ortsteile["5023"] = data = ["Gnigl","Salzburg Heuberg","Langwied","Koppl Heuberg","Koppl Guggenthal"]

def suche_orte_unter_postleitzahl(sOrtanfangsbuchstaben,sPlz):
 list_orte = plz_ortsteile.get(sPlz)
 r = re.compile(sOrtanfangsbuchstaben +".*")
 lines_orte = [line for line in list_orte if r.match(line)]
 if lines_orte:
  for name in lines_orte:
   print(name)
 else:
  print("keine Orte gefunden");  

def suche_orte_nach_anfangsbuchstaben(sOrtanfangsbuchstaben):
 for key in plz_ortsteile: 	# loop over each key in the dictionary 
  orte = plz_ortsteile.get(key) # get the values i.e. the List 
								# from the dictionary which are associated
								# with this key.
								
  for ortschaft in orte:	# loop over each value in the List
   list_alle_orte.append(ortschaft + " - " + key)
   
 r = re.compile(sOrtanfangsbuchstaben +".*")
 lines_orte = [line for line in list_alle_orte if r.match(line)]
 if lines_orte:
  for name in lines_orte:
   print(name)
 else:
  print("keine Orte gefunden");
  
def suche_alle_orte():
 suchwort = input("Ortssuche: bitte erste 2 Buchstaben eingeben: ") 
 suche_orte_nach_anfangsbuchstaben(suchwort)
  
schleife_verlassen = "n";
#check if dictionary is empty
sind_daten_vorhanden = bool(plz_ortsteile)

if sind_daten_vorhanden == True:
 while schleife_verlassen == "n":	
  strPlz = input("Ihr Plz. eingeben: ")
  
  if strPlz in plz_ortsteile.keys():
   orte = plz_ortsteile.get(strPlz)
   for ortschaft in orte:
    print(strPlz," - ",ortschaft)
  else:
   print("Dieser Postleitzahl ist bei uns noch nicht gespeichert worden")
   
  schleife_verlassen = input("Anfrage beenden(j/n): ")
  if schleife_verlassen == "j":
   break;
  else: continue   
 else: 
  print("...Anfrage beendet")	# anzeige nach Ende der while-schleife
else:
 print("keine Daten vorhanden")

print("------ Ortssuche ---------------") 
suche_alle_orte();

