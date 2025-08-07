print("🌟Website Rating🌟")
name = input("Input the website name: ")
url = input("Input the URL: ")
description = input("Input your a description: ")
rating = input("Input the a star rating out of 5: ")
print()
website_info = {"name":name, "url":url, "description" :description, "rating":rating}

for name, value in website_info.items():
  print(f"{name}: {value}")