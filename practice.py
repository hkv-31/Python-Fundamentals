'''
Student Management System

1. Add student
2. View students
3. Calculate average marks
4. Find top student
5. Show pass/fail status
'''

students = [
    {"name": "Hetanshi", "grade": "A", "course": "AI ML", "math": 95, "ml":93, "coa": 85.6},
    {"name": "Prisha", "grade": "A+", "course": "CSE", "math": 92, "ml":85.4, "coa": 90},
    {"name": "Riddhima", "grade": "O", "course": "ECE", "math": 87, "ml":90, "coa": 92},
    {"name": "Divya", "grade": "A", "course": "AI ML", "math": 97, "ml":89, "coa": 86}
]

for i in students:
    print(i)

students.append(
    {"name": "Dhvani", "grade": "B", "course": "AI ML", "math": 75, "ml":82, "coa": 74}
)

print(students[4])

math = sum(i["math"] for i in students)
average = math / len(students)
print(average)

max = 0
top_student = ""

for i in students:
    score = i["math"] + i["ml"] + i["coa"]
    if score > max:
        max=score
        top_student = i["name"]
print(top_student)

def pass_fail(students):
    for i in students:
        if i["grade"] in ["O", "A+", "A"]:
            print("Pass")
        else:
            print("Fail")

def show_student_count():
    print(f"Total students: {len(students)}")

if __name__ == "__main__":
    pass_fail(students)