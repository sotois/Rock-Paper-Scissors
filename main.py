import random 

def get_user_choice():
  valid_choice = ['rock', 'paper', 'scissors']
  while True:
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    
    if user_choice in valid_choice:
      return user_choice
    
    else:
      print("Invalid choice. Please type 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    return computer_choice
    
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
    
def play_game():
  user_score = 0
  computer_score = 0
  
  while True: 
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    result = determine_winner(user_choice, computer_choice)
    print(result)
    
    if result == "You win!":
      user_score += 1
    elif result == "Computer wins!":
      computer_score += 1
      
    print("Score -> User: {} | Computer: {}".format(user_score, computer_score))
    
    while True:
      play_again = input("Do you want to play again? (yes/no): ")
      if play_again.lower() == "yes":
        break
      elif play_again == "no":
        print("Final score: ")
        print("User: {} | Computer: {}".format(user_score, computer_score))
        return
      else:
        print("Invalid input. Please type 'yes' or 'no'.")
  
play_game()
