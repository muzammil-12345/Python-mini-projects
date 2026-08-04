'''
  Day 25: Animal Sound Simulator using Polymorphism
  Topics Covered:
  1. What is polymorphism
  2. Method overriding in polymorphism
  3. Using polymorphim in python
  4. Real-word examples of polymorphism
  5. Project: Animal sound simulator
'''

# What is polymorpism?
'''
Polymorphism allows objects of different classes
to be treated as objects of a common super class.
The term "poly" means 'many' and  "morphism" means
'many'. This allows the same interface to behave 
differently based on th objects.
'''

# # Example of polymorphism using method ovvrriding
# class Animal:
#     def make_sound(self):
#         print("Animal maks a sound")

# class Dog(Animal):
#     def make_sound(self):
#         print("Dog barks")

# class Cat(Animal):
#     def make_sound(self):
#         print("Cat meows")
# # Poymorphism in action
# animals = [Dog(), Cat()]
# for animal in animals:
#     animal.make_sound()

# # Another Example
# class Shape:
#     def area(self):
#         print("Calculating Area...")

# class Circle(Shape):
#     def area(self):
#         print("Area of circle: Pi * r * r")

# class Square(Shape):
#     def area(self):
#         print("Area of Sqaure: Side * Side")

# # Poymorphism in action 
# shapes = [Circle(), Square()]
# for shape in shapes:
#     shape.area()       

# # Now 3. Using polymorphism in python
# '''Next is something called as duck typing,
# using dynamic typing in python
# '''
# # Example
# class Bird:
#     def make_sound(self):
#         print("Bird chirps!")

# class Duck:
#     def make_sound(self):
#         print("Duck quacks!")

# def animal_sound(animal):
#     animal.make_sound()        

# # polymorphism in function arguments
# bird = Bird()
# duck = Duck()

# animal_sound(bird)
# animal_sound(duck)

# --- Project: Animal Sound Simulator ---
# Base class
class Animal:
    def make_sound(self):
        print("Some generic animal sound")
# derived class
class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow! Meow!")

class Lion(Animal):
    def make_sound(self):
        print("Roar! Roar!")

class Cow(Animal):
    def make_sound(self):
        print("Moo! Moo!")                          

class Duck(Animal):
    def make_sound(self):
        print("Quack! Quack!")   

# Simulator Class
class AnimalSoundSimualtor:
    def __init__ (self):
        self.animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
            print(f"{animal.__class__.__name__} added to he simulator.")
        else:
            print("Invalid animal type")

    def make_all_sounds(self):
        if not self.animals:
            print("No animals in th simulator")
        else:
            print("\n--- Animal Sounds ---")
            for animal in self.animals:
                animal.make_sound()    

# Main program
simulator = AnimalSoundSimualtor()
while True:
    print("\n--- Animals Sound Simulator ---")
    print("1. Add Dog")
    print("2. Add Cat")
    print("3. Add Lion")
    print("4. Add Cow")
    print("5. Add Duck")
    print("6. Make all sounds")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")
    if choice == '1':
        simulator.add_animal(Dog())
    elif choice == '2':
        simulator.add_animal(Cat())
    elif choice == '3':
        simulator.add_animal(Lion())    
    elif choice == '4':
        simulator.add_animal(Cow())
    elif choice == '5':
        simulator.add_animal(Duck()) 
    elif choice == '6':
        simulator.make_all_sounds()
    elif choice == '7':
        print("Exiting the simulator. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose (1-6)") 


          
                



