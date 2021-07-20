for i in range(1,11):
 a=12
 a=a*i
 print("...outer loop")
 print(a)
 print("...inner loop")
 for x in range(2,4):
  z=a/x
  if z==4:
   pass #no output to be executed/displayed
  else:
   print(z)
 print("...END of inner loop")
else:
 print("table finished") 