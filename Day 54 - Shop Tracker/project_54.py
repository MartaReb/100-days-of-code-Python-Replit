import csv

print("🌟Shop $$ Tracker🌟")
total = 0
with open("./Day 54 - Shop Tracker/Day54Totals.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    sell = float(row["Cost"])*float(row["Quantity"])
    total += sell
  print(f"Total: ${round(total,2)}")

