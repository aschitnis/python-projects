
# -------------  ENUMERATE, RANGE, ZIP, IN functions  -------------------------------
# --------------- MIN, MAX, RANDOM, INPUT ------------------------------------------

# range function
print( list(range(1,10,2)) )
print( list(range(1,10)) )
for i in range(10,100,10):
    print(f"{i}")

# ENUMERATE function on string. enumerate() is a list of tuple
s = "wer"
print("ENUMERATE function with Tuple unpacking on String")
for index, zeichen in enumerate(s):    # using tuple unpacking
    print(f"{index} - {zeichen}")

# enumerate function on List
liste = ["fortis", "abacus", "beyond meat", "goldmann sachs"]
print("ENUMERATE function with Tuple unpacking on List")
for index, wert in enumerate(liste):
    print(f"{index} - {wert}")
print("\n")

# enumerate function on a Dictionary
d3 =  {"k5020":"salzburg stadt", "k5023":"salzburg gnigl", "k5021":"aigen salzburg",
       "k5051":"wals siezenheim", "k5059":"anif", "k5182":"golling" }
print("ENUMERATE function with Tuple unpacking on Dictionary")
for index, dictItem in enumerate(d3.items()):
    print(f"{index} - {dictItem[0]} : {dictItem[1]}")
print("\n")

# ZIP Function : making a tuple out of 2 different Lists & display the Tuple
bezeichnungsliste = [2135, 7754, 6433, 65345]
namensliste = ["fortis", "abacus", "beyond meat", "goldmann sachs"]
listeVonTuple = list(zip(bezeichnungsliste,namensliste))
print("ZIP function with Tuple unpacking")
for (t1, t2) in listeVonTuple:
    print(f"{t1} - {t2}")
print("\n")

# IN Function on a dictionary
d =  {"k5020":"salzburg stadt", "k5023":"salzburg gnigl", "k5021":"aigen salzburg",
       "k5051":"wals siezenheim", "k5059":"anif", "k5182":"golling" }
# Check if the Key is existing. If it exists then display the value
searchKey = "k5051";
if searchKey in d:
    print( f"{searchKey}: {d[searchKey]}\n" )
else:
    print(f"KEY- {searchKey} not found\n")

# MIN, MAX, RANDOM, SHUFFLE, INPUT  etc
liste = [12,53,534]
from random import shuffle
print(liste)
shuffle(liste)
print(f"Nach shuffling: {liste}")

from random import randint
print(f"random number: {randint(0,110)}\n" )

wert = input("Gib hier ein Wert ein: ")
print(f"Eingabewert ist {wert}")