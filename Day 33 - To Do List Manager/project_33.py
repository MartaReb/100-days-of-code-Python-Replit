import os, time

toDoList=[]
def printList():
  if len(toDoList) == 0:
    print()
    print("Your list is empty 🥳")
  else:
    print()
    print("Your 'To Do' list:")
    for item in toDoList:
      print(item)

while True:
  print("To Do List Manager")
  print()
  action = input("What would you like to do (view, add, remove, exit)? ")
  if action == "view":
    printList()
  elif action == "add":
    item = input("What do you want to add? ")
    toDoList.append(item)
  elif action == "remove":
    item = input("What do you want to remove? ")
    if item in toDoList:
      toDoList.remove(item)
      print("Item removed from the list.")
    else:
      print("Item not found in agenda.")
  elif action == "exit":
    print("Goodbye!")
    exit()
  else:
    print("Invalid action. Please try again.")
  time.sleep(3)
  os.system("clear")