import random

options = ('rock', 'paper', 'scissors')

def choose_options():
  user_option = input('rock, paper,or scissors ==> ').lower()
  if not user_option in (options):
    print('Not valid option!')
    #continue
    return None, None

  computer_option = random.choice(options)

  print('User option => ', user_option)
  print('Computer option => ', computer_option)
  return user_option, computer_option

def check_rules(user_option, computer_option,user_wins, computer_wins) :
  if user_option == computer_option:
    print('Tie!')
  elif user_option == 'rock':
    if computer_option == 'scissors':
      print('rock wins scissors')
      print('user wins!')
      user_wins += 1
    else:
      print('paper wins rock')
      print('computer wins')
      computer_wins += 1
  elif user_option == 'paper':
    if computer_option == 'rock':
      print('paper wins rock')
      print('user wins')
      user_wins += 1
    else:
      print('scissors win paper')
      print('computer wins')
      computer_wins += 1
  elif user_option == 'scissors':
    if computer_option == 'rock':
      print('rock wins scissors')
      print('computer wins')
      computer_wins += 1
    else:
      print('scissors win paper')
      print('user wins')
      user_wins += 1
  return user_wins, computer_wins

def run_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1
  while True:
    print('=' * 20)
    print('ROUND ', rounds)
    print('=' * 20)
    print('User wins: ', user_wins)
    print('Computer wins: ', computer_wins)
    print('=' * 20)
  
    user_option, computer_option = choose_options()  
    user_wins, computer_wins = check_rules(user_option, computer_option,user_wins, computer_wins)
    rounds += 1
    
    if computer_wins == 2:
      print('Computer won!')
      break
    if user_wins == 2:
      print('User won!')
      break
    
run_game()