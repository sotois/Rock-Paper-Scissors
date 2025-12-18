def get_user_choice():
  choice = input("Enter rock, paper, or scissors: ")
  return choice
def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    return "It's a tie!"
  elif user_choice == "rock":
    if computer_choice == "scissors":
      return "You win!"
  else:
    return "Computer wins!"
  elif user_choice == "paper":
    if computer_choice == "rock":
      return "You win!"
  else: 
    return "Computer wins!"
  elif user_choice == "scissors":
    if computer_choice == "paper":
      return "You win!"
  else:
    return "Computer wins!"
