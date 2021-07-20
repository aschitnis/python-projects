
def finde_person_mit_dem_groessten_gehalt(person_gehaelts_liste):

    aktuelle_max_gehalt = 0
    top_verdienende_mitarbeiter = ""

    for (mitarbeiter, gehalt) in person_gehaelts_liste:
        if gehalt > aktuelle_max_gehalt:
            aktuelle_max_gehalt = gehalt
            top_verdienende_mitarbeiter = mitarbeiter
        else:
            pass

    return(top_verdienende_mitarbeiter, aktuelle_max_gehalt)


def get_city_population(city, *args, **kwargs):
    if city in kwargs:
        i = 0
        while i < len(args[0]):
            plz1,plz2 = (args[0][i])[0], (args[0][i])[1]
            print(f"Postleitzahl: {plz1}  {plz2}")
            i += 1

        #for k in args:
        #    print("PLZ. {} {} LEN:{}".format(k[0], k[1], len(k)) )
        return city, kwargs[city]


def test(str):
    new_string = ""
    index = 0
    while index < len(str):
        character = (str[index])
        if index % 2 == 0:  # gerade
            new_string += character.upper()
        else:
            new_string += character.lower()
        index += 1
    return new_string


string_new = test("AnthrophoMorphism")
print(string_new)

# tuple unpacking
person_gehaelts_liste = [("hans",1642), ("peter",1181), ("janik",1212), ("robert", 2100), ("pavel", 1132)]
person, gehalt = finde_person_mit_dem_groessten_gehalt(person_gehaelts_liste)
# print(f"{person} - {gehalt}")

d = {"wien":50000, "salzburg":1920, "dobrovnik":24953}

eingabe1 = "salzburg"
wert = get_city_population("salzburg", [(5020, 5023),(5028, 5033), (5019, 5400), (7081, 7077)], salzburg=400000)
print( wert )



