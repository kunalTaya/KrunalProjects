import random
from art import logo
from art import vs
from replit import clear
from game_data import data

def format_account(account):
  account_name = account['name']
  account_decr = account['description']
  account_follower=account["follower_count"]
  account_country = account[ 'country']
  return f"{account_name},a {account_decr} from {account_country}."
  
print(logo)
score = 0
game_continue = True
account_b = random.choice(data)
while game_continue:
  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b:
    account_b = random.choice(data)
  
  def check_answer(guess,a_follower,b_follower):
    if a_follower > b_follower:
      return guess == 'a'
    else:
      return guess =='b'
  
  print(f"Compare A:{format_account(account_a)}")
  print(vs)
  print(f"Compare B :{format_account(account_b)}")
  
  n = 0
  guess  = input("who want to compare A or B ").lower()
  
  a_follower = account_a["follower_count"]
  b_follower = account_b['follower_count']
  clear()
  print(logo)
  
  is_correct = check_answer(guess,a_follower,b_follower)
  if is_correct:
    score +=1
    print(f"You guess it right and the final score is {score}")
  else:
    print(f"You are wrong and final score is {score}")
    game_continue = False
    