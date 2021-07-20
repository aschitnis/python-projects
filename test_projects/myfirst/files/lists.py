

liste = [436506514370, "erentrudisstr 23/1", 5020, 341.978, "S"]
print(liste)
print("1 strasse: %s" %(liste[1]))
print("2 Alles ohne tel. Nr: %s" %(liste[1:]))

print("---- append  -------")
liste = liste + ["Österreich"]  # hinzufügen
liste.append("EU")              # hinzufügen
print("3  {}".format(liste))

print("4 ---- pop ------")
pop = liste.pop(1) #strassenname aus der liste löschen
print(pop)

# listwert abändern
liste[3] =  liste[3] + "- 451.54"
print(liste[3])

liste.reverse()
print("5    - Reihenfolge ändern -  %s" %(liste) )

liste2 = [4,9,1,4,7,3,9,5,3]
liste2.sort()
print("5 sort:    {}".format(liste2))

list_1 = [1,9,2]
list_2 = [7,5,3]
list_3 = [8,6,4]
matrix = [list_1,list_2,list_3]
print("6    matrix- Zeile 2, Element 2:  %s" %(matrix[1][1]))

#erste Element aus jeder zeile des matrixes
erste_spalte = [zeile[0] for zeile in matrix]
print(erste_spalte)
