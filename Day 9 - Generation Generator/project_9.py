year = int(input("What year were you born? "))
if year >= 1925 and year <= 1946:
  print("You are a Traditionalist.")
elif year >= 1947 and year <= 1964:
  print("You are a Baby Boomer.")
elif year >= 1965 and year <= 1981:
  print("You are a Gen X.")
elif year >= 1982 and year <= 1995:
  print("You are a Millenial.")
elif year >= 1996 and year <= 2015:
 print("You are a Gen Z.")
else:
  print("Try again!")