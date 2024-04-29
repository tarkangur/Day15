rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
# rps = rock paper scissors
rps = [rock, paper, scissors]
Computer_choose = random.randint(0, 2)
Computer_choose = rps[Computer_choose]

Player_choose = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))
if Player_choose >= 3 or Player_choose < 0:
    print("you type an invalid number, you lose!")
else:
    Player_choose = rps[Player_choose]

    print("Computer Chose:")
    print(Computer_choose)
    print("Your Chose:")
    print(Player_choose)

    if Computer_choose == Player_choose:
        print("it's a draw")
    elif Computer_choose == rock and Player_choose == paper:
        print("you win.")
    elif Computer_choose == rock and Player_choose == scissors:
        print("you lose.")
    elif Computer_choose == paper and Player_choose == rock:
        print("you lose.")
    elif Computer_choose == paper and Player_choose == scissors:
        print("you win.")
    elif Computer_choose == scissors and Player_choose == rock:
        print("you win.")
    else:
        print("you lose.")
