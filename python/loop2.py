x = 1
while x < 12:
 if x > 10:
  break
 elif x == 3:
  x = x + 1
# the entire execution-code is
# skipped from this point onwards   
  continue	
 else:		
  a=2*x
  print(a)
  x = x + 1
else: print("Table multiplication finished")  