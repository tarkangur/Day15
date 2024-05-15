from game_data import data

from art import logo, vs

import random

from replit import clear

def control(count_A, count_B):
  """follower comparison"""
  if count_A >= count_B:
    return "a"
  else:
    return "b"
def result(Follower, Choose, Score):
  """Follower and chosen comparison"""
  if Follower == Choose:
    clear()
    return Score + 1   
  else:
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {Score}")
    exit()
def game():
  list_A = []
  list_B = []
  Score = 0
  Follower = ""
  Choose = ""
  list_A = random.choice(data)
  while Follower == Choose:
    list_B = random.choice(data)
    while list_A == list_B:
      list_B = random.choice(data)
    print(logo)
    if Score > 0:
      print(f"You're right! Current score: {Score}.")
    print(f"Compare A = {list_A['name']}, {list_A['description']}, {list_A['country']}")
    print(vs)
    print(f"Against B = {list_B['name']}, {list_B['description']}, {list_B['country']}")
    count_A = list_A['follower_count']
    count_B = list_B['follower_count']
    Follower = control(count_A, count_B)
    Choose = input("Who has more followers? Type 'A' or 'B': ").lower()
    Score = result(Follower, Choose, Score)
    list_A = list_B
game()
