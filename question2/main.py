class Employee:
    def __init__(self, employee_id, name, role, salary):
        self.employee_id = employee_id
        self.name = name
        self.role = role
        self.salary = salary

    def display_details(self):
        print(f"{self.employee_id} - {self.name} - {self.role} - ${self.salary}")

# Function to add employee details to file
def add_employee(employee):
    with open("employees.txt", "a") as file:
        file.write(f"{employee.employee_id}, {employee.name}, {employee.role}, {employee.salary}\n")

# Function to read employee details from the file
def read_employees():
    employees = []

    try:
        with open("employees.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")

                employee = Employee(data[0], data[1], data[2], int(data[3]))
                employees.append(employee)
    except FileNotFoundError:
        print("Error: employees.txt file does not exist.")
    return employees
# Function to find highest salary employee
def find_highest_salary(employees):
    return max(employees, key=lambda emp:emp.salary)

# Function to find employee by role
def find_employees_by_role(employees):
    role_count = {}
    for emp in employees:
        if emp.role in role_count:
            role_count[emp.role] += 1
        else:
            role_count[emp.role] = 1
    return role_count

# Create employee objects
emp1 = Employee(101,"Rahul","Python Developer",50000)
emp2 = Employee(102,"Anjali","Tester",45000)
emp3 = Employee(103,"John","Developer",60000)
emp4 = Employee(104,"Priya","Tester",48000)

# Create/overwrite file and store data
with open("employees.txt","w") as file:
        file.write("")

add_employee(emp1)
add_employee(emp2)
add_employee(emp3)
add_employee(emp4)

# Read employee data
employees = read_employees()

# Display all employees
print("\n----Employee Details-----")
for emp in employees:
    emp.display_details()

# Employees with salary > 50000
print("\n-----Employees with salary > 50000-----")
for emp in employees:
    if emp.salary > 50000:
        print(f"{emp.name} - ${emp.salary}")

# Highest paid employee
highest_paid = find_highest_salary(employees)
print("\nHighest Paid Employee: ")
print(f"{highest_paid.name} - ${highest_paid.salary}")

# Count employees by role
print("\nEmployee count by role: ")
role_count = find_employees_by_role(employees)

for role, count in role_count.items():
    print(f"{role}: {count}")
