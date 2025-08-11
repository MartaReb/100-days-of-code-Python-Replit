import os, time

to_do_list = []
def view_list():
  if len(to_do_list) == 0:
    print("Your list is empty 🥳")
  else:
    options = input("1: All\n2: By Priority\n> ")
    time.sleep(2)
    os.system("cls")
    if options == "1":
      print("Your 'To Do' list:")
      for task in to_do_list:
        for item in task:
          print(f"{item:<5}", end=" | ")
        print()
    else:
      priority = input("What priority?\n> ")
      for row in to_do_list:
        if priority in row:
          print("Your 'To Do' list:")
          for item in row:
            print(f"{item:<5}", end=" | ")
          print()

def add_item():
  item = input("What is the task? > ")
  task_date = input("When is it due by? > ")
  priority = input("What is the priority (from 1 to 5)? > ")
  task = [item, task_date, priority]
  to_do_list.append(task)
  print("Item added to the list.")

def remove_item():
  item = input("What do you want to remove?\n> ")
  for task in to_do_list:
    if item in task:
      to_do_list.remove(task)
      print("Item removed from the list.")
    else:
      print("Item not found in agenda.")

def exit_program():
  print("Goodbye!")
  exit()
  
print("🌟Life Organizer🌟")
print()
print("Welcome to the life organizer.")
while True:
  action = input("What would you like to do:\nview, add, remove, exit?\n> ")
  time.sleep(2)
  os.system("cls")
  if action == "view":
    view_list()
  elif action == "add":
    add_item()
  elif action == "remove":
    remove_item()
  elif action == "exit":
    exit_program()
  else:
    print("Invalid action. Please try again.")
    
  time.sleep(3)
  os.system("cls")