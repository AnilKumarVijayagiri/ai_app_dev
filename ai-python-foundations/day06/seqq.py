student=["kiran","anil","aditya"]
age=[10,23,56]
mixed=["hello","hi",True,23]
print(mixed[3])
mixed[3]="Ravi"
print(mixed[3])
mixed.append("Sneha")
print(mixed)
mixed.insert(1,"Ramesh")
print(mixed)
mixed.remove("hi")
print(mixed)
mixed.pop(2)
print(mixed)
print(len(mixed))
for i in mixed:
    print(i)
for i in range(len(mixed)):
    print(i,mixed[i])