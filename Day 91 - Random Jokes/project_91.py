import requests, json, os, time

def save_joke(joke):
  with open("jokes.txt", "a") as file:
    file.write(f"{joke}\n")
    print("Joke saved!")
  time.sleep(3)

def load_jokes():
  try:
    with open("jokes.txt", "r") as file:
      jokes = file.readlines()
      for joke in jokes:
        print(joke)
  except FileNotFoundError:
    print("No jokes saved yet!")
  time.sleep(3)

while True:
  os.system("cls")
  result = requests.get("https://icanhazdadjoke.com/",
                        headers={"Accept": "application/json"})
  joke = result.json()
  print(joke["joke"])
  print()
  menu = input("""Do you want to: 
  save this joke (s),
  load old jokes (l),
  new joke (n),
  exit (e)?
  > """).lower()
  os.system("cls")
  if menu == "s":
    save_joke(joke["joke"])
  elif menu == "l":
    load_jokes()
  elif menu == "n":
    continue
  elif menu == "e":
    break
