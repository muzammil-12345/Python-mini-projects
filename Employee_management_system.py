'''
Day 24: Employee Management System Using Inheritence
Topics Covered:
1. What is Inheritance?
2. Types of Inheritance
3. Uisng the super() function
4. Method overriding
5. Project: Employee Managemnt System
'''
# What is Inheritance?
'''Inheritance allows a class to inherit properties
and methods from another class. It promotes code
reuseability and reduces redundancy.'''

# # Example of basic inheritance
# class Animal: # Parent class
#     def sound(self):
#       print("Animal makes a sound")

# class Dog(Animal):# Child class
#    def sound(self):
#       print("Dog barks")

# class Cat(Animal): # Another child class
#    def sound(self):
#       print("Cat meows")

# dog = Dog()
# dog.sound()

# # Types of Inheritance
# # - Single Inheritance (Onechild inherit from on parent)   
# class Parent:
#    def display(self):
#       print("I am a parent class")

# class Child(Parent):
#    pass 
      
# child = Child()
# child.display()

# # - Multiple Inheritance (Child Class can inherit from Multiple parent classes)
# class A:
#    def method_a(self):
#       print("I am method A")

# class B:
#    def method_b(self):
#       print("I am method B")

# class C(A, B):
#    pass

# obj = C()
# obj.method_a()
# obj.method_b()

# # - Multilevel Inheritance (A child class inherits from another child class. Forming a chain)
# class GrandParent:
#    def display(self):
#       print("I am Grand parent class")

# class Parent(GrandParent):  
#    pass

# class Child(Parent):
#    pass

# child = Child()
# child.display()

# # Using super() Function (it allows you to call method from the parent class)
# class Animal:
#    def __init__ (Self):
#       print("Animal Created")

# class Dog(Animal):
#    def __init__(self):
#       super().__init__()
#       print("Dog created")

# dog = Dog()


# # Method Overriding
# class Vehicle:
#     def fuel_type(self):
#         print("Fuel type is petrol/diesel")

# class ElectricCar(Vehicle):
#     # Child class overrides the parent method
#     def fuel_type(self):
#         print("Fuel type: Electric")

# car = ElectricCar()
# car.fuel_type()

# --- Project: Employee Management System ---
'''The goal here is to build an Employee management system
that:
1. Manages Regular empoyees and managers
2. displays Employee details and salaries
3. Implements Inheritance to reuse functionality.'''

# Base Class: Employee
class Employee:
   def __init__(self, name, emp_id, salary):
      self.name = name
      self.emp_id = emp_id
      self.salary = salary

   def display_info(self):
      print("--- Employee Details ---")
      print(f"Name: {self.name}")
      print(f"Epmloyee ID: {self.emp_id}")
      print(f"Salary: {self.salary}")
    
   def calculate_bonus(self):
      return self.salary * 0.1 

# Derived Class (Child class) : Manager
class Manager(Employee):
   def __init__(self, name, emp_id, salary, department):
      super().__init__(name, emp_id, salary)
      self.department = department

   def display_info(self):
      super().display_info()
      print(f"Department: {self.department}")

   def calculate_bonus(self):
      return self.salary * 0.2
   
# Derived class: Developer
class Developer(Employee):
   def __init__(self, name, emp_id, salary, programming_language):
      super().__init__(name, emp_id, salary)
      self.programming_language = programming_language

   def display_info(self):
      super().display_info()
      print(f"Programming Language: {self.programming_language}")

   def calculate_bonus(self):
      return self.salary * 0.15

# Main Program
employees = []

def add_employee():
    print("\n--- Choose Employee Type ---")
    print("1. Regular Employee")
    print("2. Manager")
    print("3. Developer")
    choice = input("Enter your choice: ").strip()

    name = input("Enter Employee Name: ").strip()
    emp_id = input("Enter Employee ID: ").strip()
    salary = float(input("Enter Employee Salary: ").strip())

    if choice == '1':
       employees.append(Employee(name, emp_id, salary))
    elif choice == '2':
       department = input("Enter Department: ").strip()
       employees.append(Manager(name, emp_id, salary, department))
    elif choice == '3':
       programming_langauge = input("Enter Programming Language: ").strip()
       employees.append(Developer(name, emp_id, salary, programming_langauge))
    else:
       print("Invalid choice. Please select (1-3).")

def display_all_employees():
    print("\n--- All Employees ---") 
    for employee in employees:
       employee.display_info()     
       print(f"Bonus: {employee.calculate_bonus()}") 
          
# Main Menu
while True:
   print("\n--- Employee Managemnt System ---")
   print("1. Add Employee")
   print("2. Display All Employees")
   print("3. Exit")
   choice = input("Enter your choice (1-3): ").strip()

   if choice == '1':
      add_employee()
   elif choice == '2':
      display_all_employees()
   elif choice == '3':
      print("Exiting the program.")
      break
   else:
      print("Invalid Choice. Please Enter (1-3)")
