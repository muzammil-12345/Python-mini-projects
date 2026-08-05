'''
  Day 13: Student Grades Manager project using List Comprehensions
  Topics covered:
    1. What are List Comprehensions
    2. Basic syntax and examples
    3. Filtering with list comprehensions
    4. Using conditional statements
    5. Mini-project: Student Grades Manager
'''

# Basic Syntax of List Comprehensions
# [expression for item in iterable if condition] 

# Example 1: Create a list of squares of numbers from 0 to 9
Squares = [x**2 for x in range(10)]
print(Squares)  

# Example 2: Create a list of number that doubles
numbers = [1,2 ,3 ,4 ,5]
doubled = [x*2 for x in numbers]
print(doubled)

# Example 3: Create a list of even numbers from a given list
numbers = [1, 2, 3, 4, 5, 6]
even = [x for x in numbers if x % 2 == 0]
print(even)

# Example 4: Create a list of names with length less than 5 characters
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
short = [name for name in names if len(name)<5]
print(short) # This is how to filter with list comprehensions

# Example 5: Create a list of odd or even numbers from a given list using conditional statements
numbers = [1, 2, 3, 4, 5, 6]
label = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print(label) # This is how to use conditional statements with list comprehensions

# ----- Mini-project: Student Grades Manager -----

# Step 1: Get Student scores
students_scores = input("Enter student scores separated by commas: ")
scores = [int(score) for score in students_scores.split(",")]

# Step 2: Assign Grades using list comprehensions
grades = [
    "A" if score >= 90 else
    "B" if score >= 80 else
    "C" if score >= 70 else
    "D" if score >= 60 else
    "F"
    for score in scores
]

# Step 3: Filter passing and failing students
passing_students = [score for score in scores if score >= 60]
failing_students = [score for score in scores if score < 60]

# Step 4: Display results
print("\n---- Student Grades ---")
for i, (score,grade) in enumerate(zip(scores, grades), start=1):
    print(f"Student {i}: Score = {score}, Grade = {grade}")

print("\nPassing Students:", passing_students)
print("Failing Students:", failing_students)
