phone_no = {}
print(type(phone_no))
# print(type(phone_no))
# print(type(phone_no))

phone_no3 = dict({"james": "123-456-7890", "susan": "987-654-3210", "michael": "555-555-5555", "henry": "111-222-3333", "lisa": "444-555-6666", "James" : "123-456-7890"})
# print(phone_no3["james"])

#get()

# print(dir(phone_no3))
# print(phone_no3.get("james"))
# phone_no3["james"] = [2344, 420, 2222]
# print(phone_no3)
# print(phone_no3["james"][-2])
phone_no3["michael"] = {"home": "525-355-11555","work": "555-125-5556", "village": "555-555-5557"}
print(phone_no3["michael"]["home"])



nested dict in Dictionary

student_data = {
    "henry": {"age": 20, "grade": "A", "subjects": ["Math", "Science","History"]},
    "lisa": {"age": 22, "grade": "B", "subjects": ["English", "History"]},
    "michael": {"age": 21, "grade": "A", "subjects": ["Math", "Computer Science"]},
# }
student_data["henry"]["subjects"].append("Geography")
print(student_data["henry"].update({"age": 21}))
print(student_data["henry"]["age"])
#print(student_data["henry"]["subjects"][0])

travel_info = [{
    
    "name": "Alice","age": 30,"destination": "Paris","activities": ["sightseeing", "shopping", "dining"]
},{
    "name": "Bob","age": 25,"destination": "Tokyo","activities": ["temple visits", "food tours", "shopping"]
}]

print(travel_info[0])


students_mark = {
    "joy" : 94, 
    "michael": 88,
    "susan": 92,
    "henry": 85,
    "lisa": 95,
    "Luke": 60,
    "James": 78,
    "judas": 45,
    "mary": 55,
}
students_grades = {}
for students in students_mark:
    marks = students_mark[students]
    if marks >= 90:
        students_grades[students] = "A+"
    elif marks >= 80 and marks <= 89:
        students_grades[students] = "A"
    elif marks >= 70 and marks <= 79:
        students_grades[students] = "B"
    elif marks >= 60 and marks <= 69:
        students_grades[students] = "C"
    elif marks >= 50 and marks <= 59:
        students_grades[students] = "D"
    elif marks >= 40 and marks <= 49:
        students_grades[students] = "E"
    else:
        students_grades[students] = "F"
print(students_grades)



# def add(a, b):
#     return a + b

# addition = add(5,10)   
# print(addition
# )


# def sub(c, d ):
#     return c - d

# SUBSCRACTION = sub(10, 5)   
# print(SUBSCRACTION)  






def leap_year(year):

    if ( year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

year = int(input("Enter a year: "))

if not leap_year(year):
    print(f"{year} is not a leap year.")
else:
     print(f"{year} is a leap year.")



    