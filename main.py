#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art
import random

START_RANGE = 1
END_RANGE = 100
EASY_DIFFICULTY = 10
HARD_DIFFICULTY = 5
SECRET_NUMBER = random.randint(START_RANGE, END_RANGE)

def set_guesses(difficulty):
  """
  Returns number of player guesses based on difficulty
  """
  if difficulty == "easy":  
    return EASY_DIFFICULTY
  elif difficulty == "hard":
    return HARD_DIFFICULTY
  else:
    print("Please choose easy/hard!")

def check_guess(player_guess):
  """
  Returns True when player_guess = secret number
  """
  if player_guess < SECRET_NUMBER:
    print("Too low.\n")
  elif player_guess > SECRET_NUMBER:
    print("Too high.\n")
  else:
    print(f"You got it! The secret number was: {SECRET_NUMBER}")
    return True

def number_guesser():
  print(art.logo)
  print("Welcome to Number Guesser! Try to guess the secret number!")

  #Generate random number between range
  print(f"The secret number is between {START_RANGE}-{END_RANGE}..\n")
  print(f"It's {SECRET_NUMBER}")

  #Player chooses a difficulty and set number of guesses
  num_guesses = 0
  while not num_guesses:  
    difficulty = input("Choose a difficulty (easy/hard): ").lower()
    num_guesses = set_guesses(difficulty)

  #Player tries to guess secret number
  while num_guesses > 0:
    print(f"You have {num_guesses} attempts left to guess the number.")
    player_guess = int(input("Make a guess: "))
    num_guesses -= 1

    game_won = check_guess(player_guess)
    if game_won:
      print(art.congrats)
      return

  #Player is out of guesses
  print("You ran out of guesses. You lose.")
  
number_guesser()