def get_user_choice():
  choice = input("Enter rock, paper, or scissors: ")
  return choice

def get_computer_choice():
    computer_move = random.choice(['rock', 'paper', 'scissors'])
    return computer_move
