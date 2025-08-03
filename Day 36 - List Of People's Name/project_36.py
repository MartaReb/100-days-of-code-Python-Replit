list_name = []

def print_list():
  print()
  print("Your list of names:")
  for name in list_name:
    print(name)
  
while True:
  first_name = input("Enter your first name: ").strip().capitalize()
  last_name = input("Enter your last name: ").strip().capitalize()
  print(f"Your name is {first_name} {last_name}")
  name = first_name + " " + last_name
  if name not in list_name:
    list_name.append(name)  
  else:
    print("ERROR: Duplicate name")
  print_list()