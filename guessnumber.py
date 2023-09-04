from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
#Function to check if user choice is equal to answer
def check_answer(guess, answer,turns):
  """Checks answer against guess and returns no of turns remaining"""
  if guess<answer:
    print("Too low.")
    return turns-1
  elif guess>answer:
    print("Too high.")
    return turns-1
  else:
    print(f"You got it right. {answer} is the right answer!")

#Function to set difficulity
def set_difficulty():
  level= input("Choose difficulty easy or hard. Type 'easy' or 'hard': ")
  if level == "easy":
     return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game(): 
  #choose a random number bw 1 to 100
  print("Welcome to the guessing game.")
  print("I'm thinking of a number between 1 to 100")
  answer = randint(1,100)
  print(answer)
  
  
  turns = set_difficulty()
  
  guess=0 
  #repeat the guessing
  while guess!= answer:
    print(f"You have {turns} attempts remaining to guess the number: ")
  #Ask user to guess a number
    guess= int(input("Make a guess: "))
    turns= check_answer(guess, answer,turns)
    if turns == 0:
      print("You run out of guesses. You lose!")
      #return keyword to stop the loop
      return
    elif guess != answer:
      print("Guess Again!")
# track the number of turns and if wrong reduce by 1

game()
