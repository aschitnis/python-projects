import numpy as np

meine_liste = [1,2,3]
print(meine_liste)

# liste in einem numpy array umwandeln
print( "numpy array: {}".format(np.array(meine_liste)) )

# matrix mit verschiedene listen erstellen
matrix = [ [1,2,3], [4,5,6] ]

# matrix in einem numpy matrix-array umwandeln
print( "numpy matrix-array: {}".format( np.array(matrix) ) )

# numpy matrix-array mit 5 zeilen & 5 spalten aus zero werte
print( np.zeros( (5, 5)) )

np.linspace( 0, 100, 4 )






