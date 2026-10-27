# Function to calculate grade
def calculate_grade(avg):
    if avg >=75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "F"

# Function to display student details
def display_student(student):
    print("\n------Student Result------")
    print("Student id: ", student["id"])
    print("Name: ", student["name"])
    print("Total: ", student["total"])
    print("Average: ", round(student["average"], 2))
    print("Grade: ", student["grade"])
    print("Result: ", student["result"])

students = []

n = int(input("Enter number of students:"))

# Input student details
for i in range(n):
    print(f"\n Enter details for Student {i + 1}")

    student_id = input("Student id: ")
    name = input("Student Name: ")
    python_marks = int(input("Python Marks: "))
    sql_marks = int(input("SQL Marks: "))
    ai_marks = int(input("AI Marks: "))

    total = python_marks + sql_marks + ai_marks
    average = total/3

    grade = calculate_grade(average)
    result = "PASS" if average >= 40 else "FAIL"

    student = {
        "id": student_id,
        "name": name,
        "python": python_marks,
        "sql": sql_marks,
        "ai": ai_marks,
        "total": total,
        "average": average,
        "grade": grade,
        "result": result
    }

    students.append(student)

# Display all student results:
for student in students:
    display_student(student)

# Student with highest average
highest_student = max(students, key=lambda s: s["average"])

print("\n ----Summary-----")
print("Highest Scoring Student: ", highest_student["name"])
print("Highest Average: ", round(highest_student["average"], 2))

# Student with average > 75
top_students = [student["name"] for student in students if student["average"] > 75]

print("Students above 75 Average: ", ",".join(top_students))