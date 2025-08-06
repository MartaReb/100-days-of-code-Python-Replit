print("🌟Contact Card🌟")
print()
name = input("Input your name: ").strip()
date = input("Input your date of birth: ").strip()
number = input("Input your telephone number: ").strip()
email = input("Input your email: ").strip()
address = input("Input your address: ").strip()

contact = {"name":name, "date":date, "number":number, "email":email, "address": address}
print()
print(f"Hi {contact['name']}. Our dictionary says that you were born on {contact['date']}, we can call you on {contact['number']}, email {contact['email']}, or write to {contact['address']}.")