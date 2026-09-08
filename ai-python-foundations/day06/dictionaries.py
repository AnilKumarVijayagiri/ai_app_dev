#student=["Anil",22,"CSE",8.9]
student={
    "name":"Anil",
    "age":22,
    "branch":"CSE",
    "cgpa":8.9
}
print(student["name"])
print(student["age"])
student["age"]=23
print(student["age"])
del student["cgpa"]
print(student)

students={
    101:{"name":"Anil","age":22,"branch":"CSE"},
    102:{"name":"Kiran","age":23,"branch":"CSE"},
    103:{"name":"Aditya","age":21,"branch":"CSE"}
}
print(students[102]["name"])