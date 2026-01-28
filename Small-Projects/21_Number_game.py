import random
import sys
currentNum=0
botFlag=False
playerFlag=False
array: list[int] = []
def choices(value:str): 
    global playerFlag
    global botFlag
    if value.lower()=="y":
       print("Enter 'F' to take first chance")
       print("Enter 'S' to take second chance")
       chance=input('> ')
       choices(chance)
    elif value.lower()=="n": 
       return False 
    else:
      return "Please enter Y or N"
    if chance.lower()=="s":
       playerFlag=True
       start()
    elif chance.lower()=="f":
       botFlag=True
       start()
    else:
       return "Enter F/S"
    



def start():
   while currentNum <= 21 and botFlag==True:
      playerturn()
      print("Order of inputs after ur turn:")
      print(array)
      botturn()
      print("Order of inputs after computer's turn is:")
      print(array)
      
   while currentNum <=21 and playerFlag==True:
      botturn()
      print("Order of inputs after computer's turn is:")
      print(array)
      playerturn()
      print("Order of inputs after ur turn:")
      print(array)
  


def botturn():
 global currentNum
 botVal=(random.randint(1,3))
 for _ in range(botVal):
  currentNum+=1  
  array.append(currentNum)
  if currentNum >= 21:
       print("Player Win oOOoOOoOooOooOOoOOo")
       endoftheGame()
       
  
  
   
   


def playerturn():
   global currentNum
   playerVal=int(input("How many numbers do you wish to enter..:"))
   if playerVal not in [1, 2, 3]:
    print("Enter 1,2 or 3 idiot")
    playerturn()
    
   else:
    for _ in range(playerVal):
     currentNum+=1  
     array.append(currentNum)
     if currentNum >= 21:
       print("Player Lose oOOoOOoOooOooOOoOOo")
       endoftheGame()
   
def endoftheGame():
       sys.exit()
     
 
yesornot=(input("Do u want to start game Y/N   :"))
choices(yesornot)


