# Employee File Management System:

Develop a python app to manage employee records using file handling.

Logic used:
1. Create an employee class with employeeid,name,role,salary.
2. Include a method display_details() to get employee info
3. create functions add_employee,read_employee,find_highest_salar,find_employees_by_role to get info.
4. Store employee info in employees.txt
5. use with open for file operations
6. Handle filenotfound error using exception handling.
7. Display all employees, high paid employee, employee cound by role.

How to Run:
1. Save the program as main.py under question2 folder and run program using python main.py in terminal using vs code.

Sample input and output:
----Employee Details-----
101 -  Rahul -  Python Developer - $50000
102 -  Anjali -  Tester - $45000
103 -  John -  Developer - $60000
104 -  Priya -  Tester - $48000

-----Employees with salary > 50000-----
 John - $60000

Highest Paid Employee: 
 John - $60000

Employee count by role: 
 Python Developer: 1
 Tester: 2
 Developer: 1