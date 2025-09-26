import requests, json, os

os.mkdir("Pictures")

for i in range(10):
  result = requests.get("https://randomuser.me/api/")
  if result.status_code == 200:
    user = result.json()
  
    for person in user["results"]: 
      name = f"""{person["name"]["first"]} {person["name"]["last"]}""" 
      picture = requests.get(person["picture"]["medium"])
      f = open(f"Pictures/{name}.jpg", "wb")
      f.write(picture.content)
      f.close()