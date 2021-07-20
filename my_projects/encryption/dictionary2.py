import re

import re

data = ["Alpensiedlung","Altstadt","Elisabeth-Vorstadt","Gaisberg","Gneis","Adneter Riedl","Au","Burgfried"
		,"Gamp","Greis","Hallein","Braunau Neustadt","Braunau am Inn","Gasteig","Haiden",
		"Haselbach","Höft","Gnigl","Salzburg Heuberg","Langwied","Koppl Heuberg",
		"Koppl Guggenthal"]
		
r = re.compile('Ha.*')
lines_to_log = [line for line in data if r.match(line)]
for name in lines_to_log:
 print(name)

