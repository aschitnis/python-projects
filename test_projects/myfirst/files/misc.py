import sys

dictGeradeUndUngeradeZahlen = {"geradezahlenliste": [], "ungeradezahlenliste": []}
zahlenliste = [77, 32, 67, 21, 82, 90, 451, 81, 36, 71, 33]


def findeAlleGeradeUndUngeradeZahlenAusderListe(liste):
    geradezahlenliste = []
    ungeradezahlenliste = []
    for number in zahlenliste:
        if number % 2 == 0:
            geradezahlenliste.append(number) # add even numbers to the list
        else:
            ungeradezahlenliste.append(number)  # add odd numbers to the list

    dictGeradeUndUngeradeZahlen["geradezahlenliste"].append(geradezahlenliste) # add even nos. list as value to even-number Key
    dictGeradeUndUngeradeZahlen["ungeradezahlenliste"].append(ungeradezahlenliste) # add odd nos. list as value to odd-number Key
    return dictGeradeUndUngeradeZahlen


findeAlleGeradeUndUngeradeZahlenAusderListe(zahlenliste)
print( "Even Numbers {}".format(dictGeradeUndUngeradeZahlen["geradezahlenliste"]) )
print( "Odd Numbers {}".format(dictGeradeUndUngeradeZahlen["ungeradezahlenliste"]) )

str = "macdonald"
print(f"{str[::-1]}")
print(f"{str[0:3]}")
print(f"{str[3::]}")

def read_data_from_file():
    f = open("books.txt")
    liste = f.readlines()
    f.close()
    return liste

# variables just point to objects (they hold no memory)
# objects are shared between instances

# ------------------------------  MUTABILITY USW  -----------
liste2 = [2,3,4,5,6,7]              # a List is mutable
liste1 = liste2

string1 = "abhijit"                 # a String is immutable
string2 = string1

i = "a"
print("SIZE: {}".format(sys.getsizeof(i)) )

def change_liste2():
    liste2[1] = 55
    string1 = "elfriede"
    return 0

change_liste2()
print("{} --  {}".format(liste2, string1))

