import random
number= random.randint(1,100)
flag = False
Timer=0
while flag == False: 
 guessesNum = int(input("Guess Number..:"))
 Timer += 1
 if guessesNum < number:
   print("Higher")

 elif guessesNum > number:
   print("Lower")
 else:
   print("FINDED",str(Timer),"Times Tryed")
   break  
   
