import random

def roll_dice(sides):
  result = random.randint(1,sides)
  return result

def roll_6_and_8():
  roll_6_sided_dice = roll_dice(6)
  roll_8_sided_dice = roll_dice(8)
  health = roll_6_sided_dice * roll_8_sided_dice
  return health