
liste = [5020, 5071, 5081, 5300, 5026, 5082, 5101 ]
liste_gerade_zahlen_verdoppelt = []

for i in liste:
    if i % 2 == 0:
        liste_gerade_zahlen_verdoppelt.append(i*2)
    else:
        pass

# the above for-loop using list comprehension
# 1. copy the expression  (i*2)
# 2. copy the for loop excluding final :
# 3. copy the if statement line, excluding the :
liste_gerade_zahlen = [i*2 for i in liste if i % 2 == 0]
print(liste_gerade_zahlen)

# nested-loop comprehension
liste = [5020, 5071, 5081, 5300, 5026, 5082, 5101 ]
liste2 = [4020, 4030, 4040, 4048, 4050, 4052, 4053 ]
liste3 = [8000, 8010, 8020, 8036, 8041, 8042, 8011 ]
matrix = [liste,liste2,liste3]
neue_liste = []

# unconditional loop
for row in matrix:
    for n in row:
        neue_liste.append(n)

# comprehension
neue_liste.clear()
neue_liste = [n for row in matrix for n in row]
print("unconditional loop {}".format(neue_liste))

# conditional loop
neue_liste.clear()
for row in matrix:
    for n in row:
        if n % 2 == 0:
            neue_liste.append(n*2)
        else:
            pass

# comprehension
neue_liste.clear()
neue_liste = [n*2 for row in matrix for n in row if n % 2 == 0]
print("conditional loop {}".format(neue_liste))

# -------------------------------------------------------------------------------------
# SET COMPREHENSION
# -------------------------------------------------------------------------------------
my_set = {"XE4234", "WB75A", "AAH4823", "QGWQ8", "ZP5734","AR64823", "VS432", "H0L54", "C75CCP", "HUL905"}
new_set = set()
for word in my_set:
    if word[0] in ("H","A"):
        new_set.add(word)

# comprehension
new_set.clear()
new_set = {
    word
    for word in my_set
    if word[0] in ("H","A")
}
print(f" SET comprehension: {new_set}")

# -------------------------------------------------------------------------------------
# DICTIONARY COMPREHENSION
# -------------------------------------------------------------------------------------
my_dictionary = {4:37,9:42,51:93,52:87,47:110,54:92,56:97,44:12,59:473,213:888}
new_dictionary = {}
# comprehension
new_dictionary = {
    key: value * 2
    for key, value in my_dictionary.items()
    if value % 2 == 0
}
print(f" DICTIONARY comprehension: {new_dictionary}")