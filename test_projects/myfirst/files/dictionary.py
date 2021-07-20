
# Dictionary, Tuples & Dictionary_COMPREHENSION
# Tuple unpacking

d1 = {"strasse" : "erentrudisstrasse 23", "plz" : 5020, "land" : "österreich", "bereiche" : [12,"5A",974, "B4ZW"],
      "teilbereich" : "OAQWW", "jahresgehalt":36000, "gehalt":0.0  }

# Overwriting a Value for a KEY
#monatsgehalt berechnen. Der ursprungliche monatsgehalt (wert) wird überschrieben.
d1["gehalt"] += (d1["jahresgehalt"]/12)
# ausgabe

print("Plz und Bereich {} - {} - Teilbereich: {} Land: {} Gehalt: {}".
        format(d1["plz"], d1["bereiche"][2], d1["teilbereich"][1], d1["land"].upper(),
                d1["gehalt"]) )
# ------------------------------------------------------------------------------------------------------
# methoden
print("Alle Keys: %s" %(d1.keys()))
print("Alle Values: %s\n" %(d1.values()))

# Looping over a Dictionary with Tuple unpacking
d3 =  {"k5020":"salzburg stadt", "k5023":"salzburg gnigl", "k5021":"aigen salzburg",
       "k5051":"wals siezenheim", "k5059":"anif", "k5182":"golling" }

# This is called tuple unpacking on a dictionary.
for k, v in d3.items():
    print("{} - {}".format(k, v))
print("\n")

# wenn du nur die Werte brauchst und nicht die Schlüsseln
# for wert in d.values():
for _, v in d3.items():
    print("values: {}".format(v))
print("\n")


#-------------------------------------- TUPLES  sind unveränderlich.  -----------------------
t = ("name",49,"chitnis",43, "gkk", "sbg", "name", "sbg")
print("tuple value for index 2: %s\n tuple index for value 'chitnis': %s" %(t[2], t.index("chitnis")))
# wieviele male es vorkommt
print("Sbg repeated : {} times in the Tuple.".format(t.count("sbg")) )
for x in t:
    print("{}".format(x))

# Tuples in a List
# loop over the List
# display each of the Tuple values
liste = [ (14.5,12.99), (2.09,67.81), (5.5,9.45), (18.0,1.964),(4.66,11.0459) ]

# This is called tuple unpacking on a list of tuple values.
for (t1, t2) in liste:
    print("Tuple value {}  {}".format(t1,t2))


# --------------------------------  DICTIONARY COMPREHENSIONS ------------------------------
d1 = {x: x+2 for x in range(50)}   # initialize using tuple unpacking

# a dictionary of a List with Sets
liste_von_sets = [("abhijit",3100), ("elfi",1700), ("andi",2300), ("robert",1701), ("laura",1456) ]
d1 = dict(liste_von_sets)
for (k, v) in d1.items():
    print(f"{k} - {v}")

d2 = { k:v for (k, v) in d1.items() if v > 1700 }
d2.items()