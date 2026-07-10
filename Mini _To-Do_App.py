'''
  Day 17: Mini To-Do ap using JSON files
  Topics Covered:
  1. What are JSON Files?
  2. Reading JSON data
  3. Writing a JSON file
  4. Modifying JSON file
  5. Mini-project: Mini To-DO App
'''

# Example of JSON data
# [
#  {"task":"Learn python json", "Status":"Incomplete"},
#  {"task":"Build a To-do app", "status":"Complete"}
# ]

# Loading and reading JSON file

# import json

# with open("json_data", 'r') as file:
#     tasks = json.load(file)
#     print(tasks)

# # Writing a JSON file
# tasks = [
#     {"task":"Complete project", "status":"Incomplete"}
# ]

# with open("tasks.json",'w') as file:
#     json.dump(tasks, file, indent=4)

# # Modifying JSON file 
# with open('tasks.json','r') as file:
#     tasks = json.load(file)

# tasks.append({"task":"Learn python", "status":"Incomplete"})

# with open("tasks.json",'w') as file:
#     json.dump(tasks, file, indent=2)

# --- Mini-project: Mini To-Do App using JSON ----
import json
import os

# File for storing data
TASK_FILE = 'my_tasks.json'

# Ensure the tasks file exist
if not os.path.exists(TASK_FILE):
    with open(TASK_FILE,'w') as file:
        json.dump([], file)

# Step 1: Load Task From JSON
def load_tasks():
    with open(TASK_FILE,'r') as file:
        return json.load(file)

# Step 2: Save tasks to JSON
def save_tasks(tasks):
    with open(TASK_FILE,'w') as file:
        json.dump(tasks, file, indent=2)

# Step 3: Add a new task      
def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "status":"Incomplete"})
    save_tasks(tasks)
    print(f"Task {task} added successfully!")

# Step 4: View all tasks
def view_tasks():
    tasks = load_tasks()
    if tasks:
        print("\n--- To-do list ---")
        for idx, task in enumerate(tasks, start=1):
            print(f'{idx}. {task["task"]} - {task["status"]}')
    else:
        print("No Task Found.")

# Step 5: Update Task Status
def update_task():
    tasks = load_tasks()
    view_tasks()
    try:
        task_index = int(input("Enter the task number to update: ")) - 1
        if 0 <= task_index < len(tasks):
            new_status = input("Enter the new status (Complete/Incomplete): ")
            tasks[task_index]["status"] = new_status
            save_tasks(tasks)
            print('Task Updated Successfully!')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number")

# Step 6: Delete a task
def delete_task():
    tasks = load_tasks()
    view_tasks()
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            save_tasks(tasks)
            print(f"Task {deleted_task['task']} deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Step 7: Display Menu:
def show_menu():
    print('\n--- Mini To-do App ---')
    print("1. Add a new task")
    print("2. View all tasks")
    print('3. Update task status')
    print('4. Delete a task')
    print('5. Exit')

# Step 8: Main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        task = input("Enter the task description: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting the To-do app.")                
        break
    else:
        print('Invalid input. Please enter a valid number (1-5).')





