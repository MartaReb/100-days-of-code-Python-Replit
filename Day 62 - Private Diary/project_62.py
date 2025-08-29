import datetime, csv, os, time

def add_entry():
  entry = input("Enter your diary entry: ")
  with open("diary.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([datetime.datetime.now(), entry])
    print("Entry added successfully")
    
def view_entries():
  try:
    with open("diary.csv") as file:
      reader = csv.reader(file)
      entries = list(reader)
      if not entries:
        print("No diary entries found.")
      else:
        for row in entries:
          print(f"{row[0]} - {row[1]}")
  except FileNotFoundError:
    print("No diary entries found.")

password = "my_password"
question = input("Enter the password: ")

while True:
  time.sleep(2)
  os.system("clear")
  if question == password:
    print("""Welcome to your private diary
    1. Add a new entry
    2. View all entries
    3. Exit""")
    choice = input("> ")
    time.sleep(2)
    os.system("clear")
    if choice == "1":
      add_entry()
    elif choice == "2":
      view_entries()
    elif choice == "3":
      exit()
    else:
      print("Invalid choice")   
  else:
    print("Access denied")
    exit()
