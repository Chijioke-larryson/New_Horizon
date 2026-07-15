import json


employee = {
    "Name " : "John Doe",
    "Age" : 30,
    "Department" : "IT",
    "Skills" : ["Python", "JavaScript", "SQL"]
}
file_path = "employee1.json"


with open (file_path, "w") as file:
    json.dump(employee, file, indent=4)
print(f"Employee data has been written to {file_path}")