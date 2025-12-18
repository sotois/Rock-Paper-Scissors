import random 

def get_user_choice():
  user_choice = input("Enter rock, paper, or scissors: ")
  return user_choice

def get_computer_choice():
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    return computer_choice
    
def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    return "It's a tie!"
  elif user_choice == "rock":
    if computer_choice == "scissors":
      return "User wins!"
  else:
    return "Computer wins!"
  elif user_choice == "paper":
    if computer_choice == "rock":
      return "User wins!"
  else: 
    return "Computer wins!"
  elif user_choice == "scissors":
    if computer_choice == "paper":
      return "User wins!"
  else:
    return "Computer wins!"
