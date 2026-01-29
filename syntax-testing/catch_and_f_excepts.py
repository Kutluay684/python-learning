
def factorial(x,y):
    x=x/y
    print(x)


while True:
    
    try:
     x=int(input("Enter X..:"))
     y=int(input("Enter Y..:"))
     factorial(x,y)    
    except ZeroDivisionError:
        print("0 indivisible")
    except ValueError:
        print("Please enter integer value")
        
    except Exception as e:
        print("something worng",e)
    
    else:
        break


    



