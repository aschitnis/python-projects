# a simple pygame
# https://realpython.com/pygame-a-primer/
import pygame
pygame.init()

# Check if the KeyDown event has occured & if it is the ESC key, then end the loop
def FindKey(event,keyIntegerValue):
 if event.dict['unicode']:
  byteValue = event.dict['unicode'].encode('utf-8')  # From Key\Value pair Dictionary: 'unicode' key's byteValue should be  b'\x1b' if the ESC key was pressed.  
  for x in byteValue:
   ByteToStringValue = bin(x)    # convert  
   if str(ByteToStringValue) == '0b11011' and event.dict['key'] == keyIntegerValue:
    integerValueFromBytesValue = int(ByteToStringValue, 2) # convert byteString to integer value
    return True
   else:
    return False
 else:
  return False

#create a tuple
screen = pygame.display.set_mode([500,500])


running = True
while running:
 for event in pygame.event.get():
  
  #print(event.dict)
  #print(pygame.event.event_name(event.type))
  
  if event.type == pygame.KEYDOWN:
   escape_key = FindKey(event,27)
   if escape_key == True:
    running = False 

  if event.type == pygame.QUIT:
   running = False

 screen.fill((255,255,255))
 pygame.draw.circle(screen, (0, 0, 255), (150, 350), 40)
 pygame.display.flip()