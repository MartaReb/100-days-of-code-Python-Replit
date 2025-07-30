import random

greetings = ["Cześć", "Hello", "Salut", "Ciao", "Anyoung", "Yassou", "Habari", "Ahlan", "Hallo", "Tjena", "Hej"]
number = random.randint(0, len(greetings) - 1)
print (greetings[number])