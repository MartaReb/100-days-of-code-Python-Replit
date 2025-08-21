import time, os
inventory = []

try:
  f = open("inventory.txt", "r")
  inventory = eval(f.read())
  f.close()
except FileNotFoundError:
  f = open("inventory.txt", "w")
  f.close()
except SyntaxError:
  pass
  

def add():
  item = input("Enter the item to add: > ").title()
  inventory.append(item)
  print("Added", item, "to inventory.")

def remove():
  item = input("Enter the item to remove: > ").title()
  if item in inventory:
    inventory.remove(item)
    print("Removed", item, "from inventory.")
  else:
    print("Item not found in inventory.")

def view():
  item = input("Enter the item to view: > ").title()
  if item in inventory:
    print(f"There are {inventory.count(item)} {item} in inventory.")
  else:
    print("Item not found in inventory.")
  
while True:
  print("🌟RPG Inventory🌟")
  print()
  menu = input("1. Add item\n2. Remove item\n3. View inventory\n4. Exit\n> ")
  time.sleep(3)
  os.system("cls")
  if menu == "1":
    add()
  elif menu == "2":
    remove()
  elif menu == "3":
    view()
  elif menu == "4":
    print("Goodbye!")
    f = open("inventory.txt", "w")
    f.write(str(inventory))
    f.close()
    exit()
  else:
    print("Invalid input. Please try again.")
  time.sleep(3)
  os.system("cls")