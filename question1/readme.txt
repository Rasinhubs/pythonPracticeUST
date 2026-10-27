#Student Marks Management System:
Problem Statement:
Develop a python program to manage student marks with student details, results, grades and identify highest scoring student.

Logic used:
1. Store sutdent info using list of dict.
2. Accept stud id, name, python marks, sql marks and ai marks.
3. calcualte totalmarks, average marks, grade
4. Determing pass or fail based on average marks.
5. Use a function to calculate grades.
6. Display individual student results.
7. Use max() function with lambda expression for finding highest scoring student.
8. Use a list comprehension to find students who is greater and display summary report.

How to run the program:
1. Open terminal and save the program run using the command python after going to the question1 folder run main.py

Sample input and output:
Enter number of students:2

 Enter details for Student 1
Student id: 271240
Student Name: Ragu
Python Marks: 50
SQL Marks: 40
AI Marks: 30

 Enter details for Student 2
Student id: Varan
Student Name: Varan
Python Marks: 30
SQL Marks: 20
AI Marks: 10

------Student Result------
Student id:  271240
Name:  Ragu
Total:  120
Average:  40.0
Grade:  C
Result:  PASS

------Student Result------
Student id:  Varan
Name:  Varan
Total:  60
Average:  20.0
Grade:  F
Result:  FAIL

 ----Summary-----
Highest Scoring Student:  Ragu
Highest Average:  40.0
Students above 75 Average:  