import random
from art import logo

EASY_TURNS = 10
HARD_TURNS = 5

def easy_hard():
  """difficulty selection"""
  level = input("Choose a difficulty. Type 'easy' or 'hard':")
  if level == "easy":  
    return EASY_TURNS
  else:
    return HARD_TURNS

def number_guess(guess, computer_number, attempts):  
  if guess > computer_number:
    print("Too high.")
    return attempts - 1
  elif guess < computer_number:
    print("Too low.")
    return attempts - 1
  else:
    print(f"You got it! The answer was {computer_number}")

def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  computer_number = random.randint(1, 100)
  attempts = easy_hard()
  guess = 0
  
  while guess != computer_number:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attempts = number_guess(guess, computer_number, attempts)
    if attempts == 0:
      print("You've run out of guesses, you lose.")
      print(f"The answer was {computer_number}")
      exit()
    elif guess != computer_number:
      print("Guess again.")
game()
  







