'''
  Day 16: Daily journal logger Using file writing
  Topics Covered:
  1. File writing in python
  2. Writing to files(w mode)
  3. Appending to files(a mode)
  4. Handling file writing errors
  5. Mini-project: Daily journal logger
'''

# # Creating a text file and writing into it
# with open('journal.txt','w') as file:
#     file.write('Day 1: Today I learned about Writing and appending into files in python.\n')

# # Appending into this file
# with open('journal.txt','a') as file:
#     file.write("Day 2: I Built a journal logger today.\n")

# # Handing file writing error
# try:
#     with open("/restricted/journal.txt",'w') as file:
#         file.write('Test entry')
# except PermissionError:
#     print("You do not have permission to write to the file.")     

# ----- Mini-project: Daily journal logger -----

# Step 1: Define the journal file
JOURNAL_FILE = 'daily_journal.txt'

# Step 2: Add a new entry
def add_entry():
    entry = input('Writ your journal entry: ')
    with open(JOURNAL_FILE,'a') as file:
        file.write(entry + '\n')
    print('Enty added successfully!')

# Step 3: View all enteries
def view_enteries():
    try:
        with open(JOURNAL_FILE,'r') as file:
            content = file.read()
            if content:
                print('\n --- Your Journal Enteries ---')
                print(content)
            else:
                print("No enteries found. Start writing today!")
    except FileNotFoundError:
        print('No journal file found. Add an entry first')

# Step 4: Search enteries by keyword   
def search_enteries():
  keyword = input('Enter a eyword to search for: ').lower()
  try:
      with open(JOURNAL_FILE,'r') as file:
          content = file.readlines()
          found = False
          print('\n --- Search Results ---')
          for entry in content:
              if keyword in entry.lower():
                  print(entry.strip())
                  found = True
          if not found:
              print('No matching enteries found.') 
  except FileNotFoundError:
      print('No journal file found. add an entry first.')

# Step 5: Dispay menu
def show_menu():
    print('\n --- Daiy journal Logger ---')
    print('1. Add a new entry. ')
    print('2. View all enteries. ')
    print('3. Search enteries by keyword. ')
    print('4. Exit ')

# Step 6: Manin program Loop
while True:
    show_menu()
    choice = input('Enter your choice (1-4): ').strip()

    if choice == '1':
        add_entry()
    elif choice == '2':
        view_enteries()
    elif choice == '3':
        search_enteries()
    elif choice == '4':
        print('Exiting the Daily journal Logger. Good bye!')
        break    
    else: 
        print('Invalid Choice. Please enter a number between 1 and 4.')  
              