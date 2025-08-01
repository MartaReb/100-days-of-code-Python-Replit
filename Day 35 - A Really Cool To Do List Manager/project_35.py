import os, time

to_do_list=[]
def print_list():
  if len(to_do_list) == 0:
    print()
    print("Your list is empty 🥳")
  else:
    print()
    print("Your 'To Do' list:")
    for item in to_do_list:
      print(item)

while True:
  print("To Do List Manager")
  print()
  action = input("What would you like to do: view, add, edit, remove, delete or exit? ")
  if action == "view":
    print_list()
  elif action == "add":
    item = input("What do you want to add? ").title()
    to_do_list.append(item)
  elif action == "remove":
    item = input("What do you want to remove? ").title()
    if item in to_do_list:
      check = input("Are you sure you want to remove this? (y/n) ")
      if check == "y":
        to_do_list.remove(item)
        print("Item removed from the list.")
      else:
        print("Item not removed.")
    else:
      print("Item not found in agenda.")
  elif action == "edit":
    item = input("What do you want to edit? ").title()
    new = input("What do you want to change it to?\n").title()
    for i in range(0,len(to_do_list)):
      if to_do_list[i] == item:
        to_do_list[i] = new
  elif action == "delete":
    check = input("Are you sure you want to delete the list? (y/n) ")
    if check == "y":
      to_do_list.clear()
      print("List deleted.")
  elif action == "exit":
    print("Goodbye!")
    exit()
  else:
    print("Invalid action. Please try again.")
  time.sleep(3)
  os.system("clear")