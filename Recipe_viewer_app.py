'''
  Day 15: Recipe Viewr App
  Topics Covered: 
  1. File reading in python
  2. Reading files Using open()
  3. Reading Modes(r, rb, r+)
  4. Handling File reading Errors
  5. Mini-project: Recipe viewer app
'''
# Reading Files using open funtion
with open("sample.txt","r") as file:
    for line in file:
        print(line.strip())

# Reading by line And handling File reading errors
try:
  with open("sample.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
except FileNotFoundError:
   print("File not found.")

# ----- Mini-project: Recipe viewer app -----

# Step 1: Load Recipe From file
def load_recipe(file_path):
   try:
      with open(file_path, "r") as file:
         content = file.read()
      recipes = [r for r in content.split("\n\n") if r.strip()]
      recipe_dict = {}
      for recipe in recipes:
         lines = recipe.strip().split("\n")
         if len(lines) >= 3:
            name = lines[0].strip()
            ingredients = lines[1].replace("Ingredients:", "").strip()
            instructions = lines[2].replace("Instructions:", "").strip()
            recipe_dict[name] = {"Ingredients": ingredients, "Instructions": instructions}
      return recipe_dict
   except FileNotFoundError:
      return {}
   
# Step 2: Display the recipe menu
def show_menu():
  print("\n--- Recipe Menu Viewer ---")
  print("1. View the recipe by name.")
  print("2. List All the Recipes.")
  print("3. Exit")

# Step 3 Display the Recipe details
def view():
   name = input("Enter the name of recipe: ").strip()
   if name in recipes:
      print(f"\n--- {name} Recipe Details ---")
      print(f"Ingredients: {recipes[name]['Ingredients']}")
      print(f"Instructions: {recipes[name]['Instructions']}")
   else:
      print('Recipe not found.')

# Step 4: Main program
recipe_file = 'recipe.txt'
recipes = load_recipe(recipe_file)

while True:
   show_menu()
   choice = input("Enter your choice (1/2/3): ")
   if choice == '1':
      view()
   elif choice == '2':
      print("\n---All Recipe---")
      for name in recipes:
         print(name)
   elif choice == '3':
      print("Exiting the program")
      break
   else:
      print("Invalid Choice. Please try again.")
          