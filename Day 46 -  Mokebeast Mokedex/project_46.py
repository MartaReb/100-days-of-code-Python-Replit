import time, os

moke_beast = {}

def pretty_print():
  for name, value in moke_beast.items():
    print(f"{name}")
    for subkey, subvalue in value.items():
      print(f"  {subkey}: {subvalue}", end=" |")
    print()
  
    
while True:
  print("🌟MokeBeast Generator🌟")
  print()
  name = input("Enter the MokeBeast name: ")
  type = input("Enter the MokeBeast type: ")
  special_move = input("Enter the MokeBeast special move: ")
  hp = input("Enter the MokeBeast starting HP: ")
  mp = input("Enter the MokeBeast starting MP: ")
  print()
  moke_beast[name] = {"Type":type, "Special Move":special_move, "HP":hp, "MP":mp}

  again = input("Would you like to add another MokeBeast (y/n)? ").lower()
  time.sleep(1)
  os.system('cls')
  if again == "n":
    pretty_print()
    break
