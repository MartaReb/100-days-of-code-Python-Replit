class Character:
  def __init__(self, character_type, name, health, magic_points):
    self.character_type = character_type
    self.name = name
    self.health = health
    self.magic_points = magic_points

  def pretty_print(self): 
    print(f"Type: {self.character_type}\nName: {self.name}\nHealth: {self.health}\nMagic Points: {self.magic_points}")

class Player(Character):
  def __init__(self, name, health, magic_points, lives):
    super().__init__("Player", name, health, magic_points)
    self.lives = lives
    
  def pretty_print(self): 
    super().pretty_print()
    alive_status = "Yes" if self.lives > 0 else "No"
    print(f"Lives: {self.lives}\nIs Alive?: {alive_status}\n")
    

class Vampire(Character):
  def __init__(self, name, health, magic_points, strength, is_night=True):
    super().__init__("Vampire", name, health, magic_points) 
    self.strength = strength
    self.is_night = is_night
    
  def pretty_print(self):
    super().pretty_print()
    time_status = "Night" if self.is_night else "Day"
    print(f"Strength: {self.strength}\nDay/Night?: {time_status}\n")
  
class Orc(Character):
  def __init__(self, name, health, magic_points, strength, speed):
    super().__init__("Orc", name, health, magic_points) 
    self.strength = strength
    self.speed = speed
    
  def pretty_print(self):
    super().pretty_print()
    print(f"Strength: {self.strength}\nSpeed: {self.speed}\n")


player_1 = Player("David", 100, 50, 3)
vampire_1 = Vampire("Vlad", 100, 50, 10, False)
orc_1 = Orc("Grom", 100, 50, 10, 10)

player_1.pretty_print()
vampire_1.pretty_print()
orc_1.pretty_print()