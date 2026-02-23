# 2️⃣ namedtuple – Lightweight Data Records
# 🧾 Exercise: Employee Management System

# Create an Employee record with:

# id

# name

# department

# salary

# ✅ Requirements:

# Create 5 employees.

# Print all employees in HR department.

# Calculate average salary.

# Give a 10% raise to all employees (remember: namedtuple is immutable).

# Sort employees by salary.

# 🔥 Real-world relevance:

# Used when you want structured records without full classes (like database rows).

from collections import namedtuple
from operator import attrgetter


def sort_display(employees):
    sorted_by_salary = sorted(
        employees, key=attrgetter('salary'), reverse=True)

    for emp in sorted_by_salary:
        print(f"{emp.name} : {emp.salary}")


def av_salary(employees):
    # salary_sum = 0
    # for item in employees:
    #     salary_sum += item.salary
    salary_sum = sum(emp.salary for emp in employees)  # list comprehension

    print(f"The Average Salary is {salary_sum/len(employees)}")


Employee = namedtuple('Employee', 'id,name,department,salary')

employees = [
    Employee(101, "John Smith", "Human Resources", 55000),
    Employee(102, "Sarah Johnson", "Finance", 68000),
    Employee(103, "Michael Brown", "IT", 75000),
    Employee(104, "Emily Davis", "Marketing", 62000),
    Employee(105, "David Wilson", "Operations", 70000)]

for item in employees:
    if item.department == "Human Resources":
        print(f"-> Name: {item.name} -> Department: {item.department}")


av_salary(employees)
sort_display(employees)

print()

for i, item in enumerate(employees):
    updated_emp = item._replace(salary=(item.salary+(item.salary*0.10)))
    employees[i] = updated_emp


av_salary(employees)
sort_display(employees)
