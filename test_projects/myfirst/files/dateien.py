import os

print(os.path.abspath("."))
d = open("testdaten.txt")

print("--- First read ---")
print("%s" %(d.read()) )

print("-- reading all lines --")
d.seek(0)
liste = d.readlines()
# inhalt ändern
liste[0] = "stadt salzburg" + "- 5020\n"

# datei in schreibmodus aufmachen und überschreiben
d = open("testdaten.txt", "w")
d.write(( "{}{}{}".format(liste[0],liste[1],liste[2]) ))
d.close()

#dateiinhalt lesen / iterieren & ausgeben
print("Iterating file / display file data")
for zeile in open("testdaten.txt"):
    print(zeile)





