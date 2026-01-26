
def display_user(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
        
display_user(username="Ahmad")
display_user(username="MAHMAD",email="mahmad@email.com")


def myFunc(a,b,c,*args,**kwargs):
    print(a)
    print (b)
    print (c)
    print (args)
    print (kwargs)
    
myFunc(10,20,30,40,50,60,"ahmad",username="Mehmed")