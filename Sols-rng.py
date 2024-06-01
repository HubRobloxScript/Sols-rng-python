import random

NameAura = ('Common', 'Uncommon', 'Good', 'natural', 'Rare', 'Divinus', 'Rage')
Rolls = 0

while True:
    print("Q: Randomize Aura")
    print("E: Checking rolls")
    Answers = input(('Game:'))
    if Answers == 'Q' or Answers == 'q':
      print("You Got", random.choice(NameAura))
      Rolls = Rolls + 1
    elif Answers == 'E' or Answers == 'e':
        print("You Rolled", Rolls, "Times")
