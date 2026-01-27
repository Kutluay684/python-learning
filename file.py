F=open("test.txt")

print(F.read())
F.seek(0)
list=F.readlines()
print(list[0])