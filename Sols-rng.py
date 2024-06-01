import random

NameAura = ('Common', 'Uncommon', 'Good', 'natural', 'Rare', 'Divinus', 'Rage')
Rolls = 0

while True:
    Answers = input(('Q for randomized Aura or E for Rolls Checking:'))
    if Answers == 'Q' or Answers == 'q':
      print("You Got", random.choice(NameAura))
    elif Answers == 'E' or Answers == 'e':
        print("You Rolled", Rolls, "Times")