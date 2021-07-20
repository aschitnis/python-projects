
# fill a list with tuples
liste = [ ("v1", 12.99), ("v2", 67.81), ("v3", 9.45), ("v4", 1.964),("v5", 11.0459) ]
# display using list comprehension syntax
for (t1, t2) in [t for t in liste]:
    print(f"{t1} - {t2}")
print("\n")

# string in a list einlesen
my_String = "Hallo"
liste = [c for c in my_String]
print(liste)
print("\n")

# jeder wert in einem range mal 2 multiplizieren & ausgeben
print("multiply by 2")
liste = [v*2 for v in range(1,12,2)]
print(liste)
print("\n")

# nur die gerade werte ausgeben
print("nur die gerade werte ausgeben")
liste = [i for i in range(17) if i % 2 == 0]
print(liste)
print("\n")

print("die gerade/ungerade werte ausgeben")
liste = [ i if i % 2 == 0 else f"ungerade - {i}" for i in range(17) ]
print(liste)
print("\n")

# euro in rupee umwandeln
euroliste = [12,8,51,10]
rupeeliste = [e*85.11 for e in euroliste]
print(rupeeliste)
print("\n")
