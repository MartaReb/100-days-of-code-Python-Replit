print("🌟Star Wars Name Generator🌟")
first_name = input("Enter your first name: ").strip().capitalize()
last_name = input("Enter your last name: ").strip().lower()
mother_maiden_name = input("Enter your mother's maiden name: ").strip().capitalize()
city_of_birth = input("Enter the city where you were born: ").strip().lower()

print(f"Your Star Wars name is {first_name[:3]}{last_name[:3]} {mother_maiden_name[:2]}{city_of_birth[-3:]}")