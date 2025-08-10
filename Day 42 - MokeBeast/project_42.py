print("👾 MokéBeast 👾")
print()
moke_beast = {"Beast Name":None, "Type":None, "Special Move":None, "HP":None, "MP":None}

for name, value in moke_beast.items():
  moke_beast[name] = input(f"Enter {name.lower()}: ").strip().title()
print()
if moke_beast["Type"]=="Earth":
  print("\033[32m", end="")
elif moke_beast["Type"]=="Air":
  print("\033[35m", end="")
elif moke_beast["Type"]=="Fire":
  print("\033[31m", end="")
elif moke_beast["Type"]=="Water":
  print("\033[34m", end="")
else:
  print("\033[33m", end="")

for name, value in moke_beast.items():
  print(f"{name:<15}: {value}")