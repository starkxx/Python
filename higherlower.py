from art import logo,vs
from game_data import data
from replit import clear
import random

def format_data(account):
     """Format account data into a single line."""
     account_name =account["name"]
     account_descr= account["description"]
     account_country=account["country"]
     return(f"{account_name}, a {account_descr}, from {account_country}")


##Use if statement to check if user is correct.

def check_answer(guess, a_followers,b_followers):
  """Take the user input and return if it right."""
  if a_followers > b_followers :
    return guess == "a"
  else:
    return guess == "b"


#Display Art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
#Make game repeatable
while game_should_continue:

#Randomly generate data from game data
  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b :
      account_b = random.choice(data)
  
  print(f"Compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Against B: {format_data(account_b)}.")
  #Ask user for a guess.
  guess= input("Who has more followers?Type 'A' or 'B'?").lower()
  
  #Check if user is correct.
  ##Get follower count of wach account.
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  is_correct = check_answer(guess, a_follower_count, b_follower_count)
   #Clear screen
  clear()
  print(logo)
  #Give user feedback on their guess.
  #Score Keeping
  if is_correct:
    score +=1
    print("You are right!")
    print(f"Your score is: {score}.")
  else:
    game_should_continue= False
    print("You are wrong.")
    print(f"Your final score is: {score}.")
    
