'''
Day 23: Library Management System Using Constructors and Methods
Topics covered:
1. What are constructors?
2. Using Instance Methods
3. Class Methods vs Static Methods 
4. Encapsulation and validaton
5. Project: Library management system
'''

# What are constructors?
'''A constructor is a secial method method used to
initlize object. In python a cnstructor is defined
by (__init__ method). It runs automatically when
an objects is created. '''

# # Example
# class book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def display_info(self):
#         print(f"Title: {self.title}")
#         print(f"Author: {self.author}")

# # Create an object
# book1 = book("A thousand splendid Suns", "Khalid Housseni")
# book1.display_info()

# # Class methods vs Static methods
# # example of class and statc methods
# class utility:
#     @classmethod
#     def get_version(cls):
#         print(f'App Version: {cls.app_version}')

#     @staticmethod
#     def greet():
#         print("Hello! Welcome to the app") 

# '''Here, Class method (Defined by @classmethod) operates on class itself 
# not on individual instances, So you don't have to pass innstances over there.
# On the other hand, static method does not operate on instance or class
# attributes. Defined by @staticmethod  '''     
# # Encapsulation and Validation
# '''Encapsulation ensures that data is hidden and accessible 
# only through methods.'''

# # Example
# class Account:
#     def __init__(self, owner, balance=0):
#         self.owner = owner  # public attribute, accessible directly
#         self.__balance = balance  # private attribute, double underscore hides it from outside access

#     def deposit(self, amount):
#         if amount > 0:  # validation, only positive amounts allowed
#            self.__balance += amount  # private attribute updated only inside the class
#            print(f"Deposited ${amount}. New balance ${self.__balance}")
#         else:
#             print("Invalid deposit amount")  # invalid input rejected

#     def get_balance(self):
#         return self.__balance  # controlled read access to private attribute


# account = Account("Muzammil", 1000)  # object created, balance set to 1000
# account.deposit(500)  # deposit method called, balance updated safely
# print(f'Account Balance: ${account.get_balance()}')  # balance read using getter method, not direct access

# --- Project: Library management System ---
'''The goal here is to build a library management system 
That allows users to:
1. Adds books to the library
2. Borrow books from the library
3. Return books to the library
4. View all the available books'''

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def display_info(self):
        status = "Available" if not self.is_borrowed else "Borrowed" 
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f'Book "{title}" by {author} added to the library.')

    # View All the books Availbe
    def view_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\n---Library Catalog ---")
            for book in self.books:
                book.display_info()

    # Borrow a book
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                print(f"Book {title} has been borrowed. Enjoy your reading")
                return
        print(f"Book {title} is not available for borrowing")    
   
    # Return a book
    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                print(f'Book {title} has been returned.')
                return
        print(f'Book {title} is not in the library.')    

# Main program
library = Library()
while True:
    print("\n--- Library Management System ---")
    print('1. Add Book')
    print('2. View Books')
    print('3. Borrow Book')
    print('4. Return Book')
    print('5. Exit')

    choice = input('Enter your choice (1-5): ').strip()
    if choice == "1":
        title = input("Enter Book title: ").strip()
        author = input("Enter author name: ").strip()
        library.add_book(title, author)
    elif choice == '2':
        library.view_books()
    elif choice == '3':
        title = input('Enter bok title to borrow: ').strip()
        library.borrow_book(title)
    elif choice == '4':
        title = input("Enter book title to return: ").strip()
        library.return_book(title)
    elif choice == '5':
        print("Exiting Library!")
        break
    else:
        print("Invalid choice. Please choose (1-5).")
