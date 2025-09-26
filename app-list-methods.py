customers=["sadıkturan","ahmetyilmaz","cinarturan","yigitbilgi"]
order_totals=[12000,13000,5000,15000]

#app1

customers.append("sadıkturan")
order_totals.append(5000)


#app2


customers.pop(-1)
order_totals.pop(-1)

#app3

print(f"Customer name is {customers[0]} total order price is {order_totals[3]+order_totals[0]} ")

#app4

customers.sort()

#app5

order_totals.sort()
order_totals.reverse()

#app6

print(min(order_totals))

#app7

final=customers.count("sadıkturan")

print(final)

#app8


customers.remove("ahmetyilmaz")

print(customers)
print(order_totals)


#app9

customers.clear()

print(customers)
print(order_totals)


#app10



customers.append(input("Enter Customer Name...: "))


order_totals.append(input("Enter total price..: "))

print(customers)
print(order_totals)


