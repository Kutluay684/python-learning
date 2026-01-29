numbers=[0,1,2,3,4,5,6]
names=["Halil","Mouhammed","Kutluay"]

final=min(numbers)
final=max(numbers)

numbers.append(4)
names.append("AM")
numbers.insert(0,100)
numbers.insert(len(numbers),99)

numbers.pop(0)

numbers.remove(2)
names.remove("AM")

numbers.sort()
names.sort()
names.reverse()

counter=numbers.count(1)


print(counter)
print(final)
print(numbers)
print(names)

