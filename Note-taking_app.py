"""
   DAY 10: File Handling in Python
   Mini-project: Note-taking App
"""

# Basic syntax
file = open("filename.txt", "mode") 
# After doing work with the file, it is important to close it
file.close()

# Reading from file
# "with" is used to open a file and automatically close it after the block of code is executed
with open("hello.txt", "r") as file:
    content = file.read()
    print(content)

# Writing into a file
with open("hello.txt", "w") as file:
    file.write("\nThis is note taking app\n")
    print("Content written to the file.")

# Appending to a file
with open("hello.txt", "a") as file:
    file.write("\nThis is an appended line.\n")
    print("Content appended to the file.")

# Reading lines from a file
with open("hello.txt", "r") as file:
    lines = file.readlines()
    print("Lines in the file:")
    for line in lines:
        print(line.strip())
        

# -----Mini-project: Note-taking App-----    

# Step 1: define a file name 
file_name = "myNotes.txt"

# Step 2: Display a menu to the user
def show_menu():
    print("----Note-taking App Menu----")
    print("1. View Notes")
    print("2. Add Note")
    print("3. Delete Note")
    print("4. Exit")

# Step 3: Add a new note funtion
def add_note():
    note = input("Enter your note: ")
    with open(file_name, "a") as file:
        file.write(note + "\n")
    print("Note added successfully.")

# Step 4: View notes function
def view_notes():
    try:
        with open(file_name, "r") as file:
            content = file.readlines()
            if content:
                print("----Your Notes----")
                for index, note in enumerate(content, start=1):
                    print(f"{index}. {note.strip()}")
            else:
                print("No notes found.")
    except FileNotFoundError:
        print("No notes found. Please add a note first.")

# Step 5: Delete a note function
def delete_note():
   confirmation = input("Are you sure you want to delete all notes? (y/n): ")
   if confirmation.lower() == "y":
       with open(file_name, "w") as file:
           file.write("")
       print("All notes deleted successfully.")
   else:
       print("Deletion cancelled.")

 # Step 6: Main loop to run the app
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            view_notes()
        elif choice == "2":
            add_note()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.") 

main()                