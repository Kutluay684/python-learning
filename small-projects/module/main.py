import methods as m
name=input("Enter device name...:")
price=input("Enter device price...:")
m.deviceAdd(name,price)

m.deviceGet()
name=input("Select device name for update...:")
price=input("Enter device price for update...:")

m.deviceUpdate(name,price)
m.deviceGet()