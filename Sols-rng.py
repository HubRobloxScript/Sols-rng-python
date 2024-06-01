import random
import os


print("Made by Gemcast or Gemcast Backup")
print("Enjoys with sols rng python")
NameAura = ('Common','Uncommon','Good','natural','Rare','Divinus','Crystallized','Rage','Topaz','Ruby','Forbidden','Emerald','Gilded','Ink','Jackpot','Sapphire','Aquamarine','Wind','Diaboli','Precious','Glock')
Biomesay = ('[normal]:Fresh air is good ','[Windy]:A refreshing And cool wind passes through the world..','[Snowy]:White snow and cold begin to cover the surrounding..','[Rainy]:Strong winds and showers sweep through the world..')
Rolls = 0

while True:
    print("Q: Randomize Aura", '\nE: rolls status', '\nC: clear output')
    print(random.choice(Biomesay))
    Answers = input(('>>>'))
    if Answers == 'Q' or Answers == 'q':
      print("You Got", random.choice(NameAura))
      Rolls = Rolls + 1
    elif Answers == 'E' or Answers == 'e':
        print("You Rolled", Rolls, "Times")
    elif Answers == 'C' or Answers == 'c':
      os.system('cls')
