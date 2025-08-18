print("🌟Current Leader🌟")
print()

f = open("high.score", "r")
scores = f.read().split("\n")
f.close()

max_score = 0
name =""

for rows in scores:
  data = rows.split()
  if data != [] and int(data[1]) > max_score:
    max_score = int(data[1])
    name = data[0]
print(f"The winner is {name} with {max_score}.")