import os, time, pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('Day 26 - Play A Song/audio.wav')
sound.play()

def pause():
  pygame.mixer.pause()

pause()

def play():
  pygame.mixer.unpause()
  while True:
    stop_playback = input("Press 2 anytime to pause playback and go back to the menu: ")
    if stop_playback == "2":
      pause()
      return 
    else:
      continue


while True:
  os.system("clear")
  print("🎵 MyPOD Music Player")
  time.sleep(1)
  print("Press 1 to Play")
  print("Press 2 to Exit")
  print("Press anything else to see the menu again")
  choice = input()
  if choice == "1":
    play()
  elif choice == "2":
    exit()
  else:
    continue