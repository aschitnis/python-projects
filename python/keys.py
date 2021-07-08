
import pygame
pygame.init()

def Interpret_Key_To_End_Loop(event):
 if event.dict['unicode']:
  byteValue = event.dict['unicode'].encode('utf-8')
  for x in byteValue:
   ByteToStringValue = bin(x)
   if str(ByteToStringValue) == '0b11011':
    integerValueFromBytesValue = int(ByteToStringValue, 2)
  return True
 else:
  return False

# ********************************************************
# **************  main program  **************************
# ********************************************************

if __name__ == "__main__":
 

 




