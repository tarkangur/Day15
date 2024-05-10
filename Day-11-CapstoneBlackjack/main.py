from replit import clear
from art import logo
import random
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def control(total, list):
  for x in list:
    if x == 11 and total > 21:
      x = list.index(11)
      list[x] = 1
      total = sum(list)

def add_cards():
  random_card = random.choice(cards)
  return random_card

def kart(toplam, deste):
  deste.append(add_cards())
  toplam = sum(deste)
  control(total=toplam, list=deste)
  toplam = sum(deste)

def result(final_user_score, final_computer_score):
  if final_user_score > 21:
    print("You went over. You lose. 😭")
  elif final_user_score < 22 and final_computer_score > 21:
    print("You win. 😃")
  elif final_user_score > final_computer_score:
    print("You win. 😃")
  elif final_user_score == final_computer_score:
    print("Draw 🙃")
  else:
    print("You lose. 😤")

def game():
  clear()
  should_continue = "y"
  while should_continue == "y":
    print(logo)
    computer_cards = []
    your_cards = []
    your_cards.extend([add_cards(), add_cards()])
    score = sum(your_cards)
    control(total=score, list=your_cards)
    score = sum(your_cards)
    computer_cards.extend([add_cards(), add_cards()])
    computer_score_first = computer_cards[0]
    computer_score = sum(computer_cards)

    print(f"  Your cards: {your_cards}, current score: {score}")
    print(f"  Computer's first card: {computer_score_first}")
    if score == 21 or computer_score == 21:
      if score == computer_score:
        print(f"  Your final hand: {your_cards}, final score: {score}")
        print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
        print("Draw 🙃")
      elif score == 21:
        while computer_score < 17:
          kart(toplam=computer_score, deste=computer_cards)
          computer_score = sum(computer_cards)
        print(f"  Your final hand: {your_cards}, final score: {score}")
        print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
        print("Win with a Blackjack 😎")
      elif computer_score == 21:
        print(f"  Your final hand: {your_cards}, final score: {score}")
        print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
        print("Lose, opponent has Blackjack 😱")
    else:
      secim = "y"
      while secim == "y":
        secim = input("Type 'y' to get another card, type 'n' to pass: ")
        if secim == "y":
          kart(toplam=score, deste=your_cards)
          score = sum(your_cards)
          print(f"  Your cards: {your_cards}, current score: {score}")
          print(f"  Computer's first card: {computer_score_first}")
          if score > 21:
            control(total=computer_score, list=computer_cards)
            break
        elif secim == "n":
          control(total=computer_score, list=computer_cards)
          computer_score = sum(computer_cards)
      while computer_score < 17:
        kart(toplam=computer_score, deste=computer_cards)
        computer_score = sum(computer_cards)
      print(f"  Your final hand: {your_cards}, final score: {score}")
      print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
      result(final_user_score=score, final_computer_score=computer_score)
    should_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if should_continue == "y":
      game()
    else:
      exit()
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  game()
