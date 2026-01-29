import random
words = ["locomotiv","spoofing","spotify","fuck","my","life","im","tired",]
lenght=len(words)
indexofWord= random.randint(0,lenght)

wordLen=len(words[indexofWord])
word=list(words[indexofWord])
emptyList=["_"]*wordLen
name = str(input("Say your name..:"))
print("Welcome  ",name)

for i in range(wordLen*2):
 
 print(*emptyList)
 
 enteredChar = ""
 while len(enteredChar) != 1:
     enteredChar = str(input("Guess the character...:"))
     if len(enteredChar) != 1:
         print("Pls enter char")
 
 for a in range(wordLen): 
  if enteredChar in word[a]:
   emptyList[a]=enteredChar
 if emptyList==word:
  print("u won")
  print(*emptyList)
  break

 
  
  
 
   
 
    
     
 
 
 
    
    

