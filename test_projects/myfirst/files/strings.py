
# ***************************   Strings
input1 = "tinker!"
print("1 " + input1[2])     # indexierung index 2 ist 'n'
print("2 " + input1[1:4])  # index 1 ist 'i' und index 4 ist 'e'. D.h. alles von index 1 ('i') bis alles vor index 4 ('e').

# Strings Rückwärts Indizierung
print("3 rückwärts indizierung: \t" + input1[-1] )
print("4 rückwärts indizierung: \t" + input1[:-1] ) # alle elemente ab anfang an bis zum Vorletzten.
print("5 " + input1[::2])                                # Ausgabe ist jede zweite Buchstabe.
print("6 rückwärts ausgabe: \t" + input1[::-1])

#
s = "A"
print( "7   %s" %(s * 10) )                                     # ausgabe verzehnfachen
print("8 %s is split at Char 'n':  %s" %(input1, input1.split('n')) )                          # ausgabe splitten

# FORMATTIERUNGEWN STRINGS
name = "Abhijit Chitnis"
print("9    Mein Name: %s" %(name.upper()))
print("10   Mein Name : {}".format("Abhijit Chitnis"))

zinsprozent = 13.4582
print("11   Zinssatz der EU: %1.6f" %(zinsprozent))
print("12   Zinssatz der EU: %s für %s" %(zinsprozent,"Abhijit"))
print("13   Zinssatz der EU: %r für %r" %(zinsprozent,"Abhijit"))
# Format Funktion
print("14   Zinssatz mit Format Funktion: {zins}".format(zins=13.534) )
print("15   Zinssatz mit Format Funktion: {zins} für {person} im {jahr}".format(zins=13.534, person="Abhijit", jahr=2021) )
# Tuple Übergabe
print("16   Zinssatz der EU: %s für %s im Jahr %s" %( (2.453,"Caroline",2021) ))