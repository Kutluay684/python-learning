notes= {}

def enterID():
 global studentNumber
 studentNumber=int(input("ENTER Student ID:"))
 choice()

def gradeAdd():   
    
     midterm=int(input("Midterm:"))
     final=int(input("Final:"))
     if not (0 <= midterm <= 100 and 0 <= final <= 100):
      print("Invalid grade")
      gradeAdd()
      
     notes[studentNumber]={
         "Midterm":midterm,
         "Final":final
     }
     choice()
     
     
def showMedian():
     student = notes.get(studentNumber)
     if not student or not student.get("Midterm") or not student.get("Final"):
        print("Please firstly enter some fucking notes")
        gradeAdd()
     midtermMedian=((float(notes[studentNumber]["Midterm"])*40)/100)
     finalMedian=((float(notes[studentNumber]["Final"])*60)/100)
     median=finalMedian+midtermMedian
     print(f"Median:{median}")
     if median >=90 and median <=100:
         print("AA") 
     elif median >=85 and median <=89:
         print("BA")
     elif median >= 80 and median <= 84:
        print("BB")
     elif median >= 75 and median <= 79:
        print("CB")
     elif median >= 70 and median <= 74:
        print("CC")
     elif median >= 65 and median <= 69:
        print("DC")
     elif median >= 60 and median <= 64:
        print("DD")
     elif median >= 50 and median <= 59:
        print("FD")
     else:
        print("FF")
     choice()

def save():
    student = notes.get(studentNumber)
    if not student or not student.get("Midterm") or not student.get("Final"):
        print("Please firstly enter some fucking notes")
        gradeAdd()
    else:
     with open("Grades.txt","a") as file:
         file.write(f"Student ID:{studentNumber}\n Midterm Note:{notes[studentNumber]["Midterm"]}\n Final Note:{notes[studentNumber]["Final"]}\n")
    choice()
def choice():
    print(f"\n STUDENT ID:{studentNumber}")
    choices=int(input("\n 1-Add Grade \n 2-Show Median\n 3-Enter ID\n 4-Save\n Make decisions..: "))
    if choices not in(1,2,3,4):
        print("Please enter correctly")
        choice()
    
    match choices:
     case 1:
        gradeAdd()
     case 2:
       showMedian()
     case 3:
         enterID()
     case 4:
         save()

        
studentNumber=input("ENTER Student ID:")
choice()

    

    