import json
student={
    "name": "Dishum",
    "age": 20, 
    "course": "AI Python Foundations",
}
with open("student1.json", "w") as file:
    json.dump(student, file,indent=4)