# Sets sind einzigartigen Elemente die nur einmal vorkommen dürfen. Sets sind unveränderlich
s = set()
s.add(341.99)
s.add(311.55)
s.add(582.01)

# eine liste erzeugen und an einen Set übergeben. Die dopplte Elemente werden entfernt
liste = [43, 21, 59, 11, 21, 96, 32, 67, 43, 97]
s2 = set(liste)
print(s2)

setBundeslaender = {"salzburg", "kärnten", "wien", "salzburg", "oö", "kärnten"}

reduceresult = 0
def addfunction(a,b):
    return a+b

from functools import reduce
reduceList = [2,4,3,5]
reduceresult = reduce(addfunction, reduceList)
print(reduceresult)