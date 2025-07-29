def colorChange(color):
  if color == "red":
    return("\033[0;31m")
  elif color == "reset":
    return("\033[0m")
  elif color == "blue":
    return("\033[0;34m")
  elif color == "yellow":
    return("\033[1;33m")
  elif color == "green":
    return("\033[0;32m")
  elif color == "purple":
    return("\033[0;35m")


print(f'{colorChange("red")}{"":>5}={colorChange("reset")}={colorChange("blue")}={colorChange("yellow")}  Music App  {colorChange("blue")}={colorChange("reset")}={colorChange("red")}=\n')
print(f'🔥▶️\t{colorChange("reset")}Radio Gaga')
print(f'\t{colorChange("yellow")}Queen\n\n')
print(f'{colorChange("reset")}PREV')
print(f'{colorChange("green")}{"":>10}NEXT')
print(f'{colorChange("purple")}{"":>20}PAUSE')