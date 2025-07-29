print("30 Days Down")
print()
for i in range(1, 31):
  print(f"Day {i}: ")
  thought= input("What did you think? ").lower()
  print()
  myText = f"You thought Day {i} was"
  print(f"{myText:>35} {thought}.")