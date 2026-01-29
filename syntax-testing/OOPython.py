

class bankacc:
    def __init__(self,owner,balance,ownerID):
        self.owner=owner
        self.balance=balance
        self.ownerID=ownerID
        self.money=0
        
    def deposit(self,money):
        if money is not 0:
            self.balance=self.balance+money
        
        else:
            print("Enter higher than 0")
            return self.balance
        
    def witdraw(self,money):
        
        if self.balance - money < 0:
            print("U dont have enough money")
            return self.balance
            
        else:
            self.balance=self.balance-money
            
        
    def showBalance(self):
        
        print(self.ownerID)
        print(self.owner)
        print(self.balance)
        
        

ownerIDC=input("Please enter your ID..:")
owner=input("Enter your name..:")
     
client1 = bankacc(owner,0,ownerIDC)

client1.showBalance()
print(f"Deposited money..: {client1.deposit(100)}")
print(f"Withdrawed money..: {client1.witdraw(80)}")