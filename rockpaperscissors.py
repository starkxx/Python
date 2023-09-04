import random
x= random.randint(0,2)
y=int(input('Type "0" for rock, "1" for paper and "2" for scissors.'))
if(y == 0):
  print("You choose:\n"+ rock)
elif(y == 1):
  print("You choose:\n"+ paper)
elif(y == 2):
  print("You choose:\n"+ scissors)
else:
  print("Invalid choice.")
if(x == 0):
  print("Computer Chose:\n"+ rock)
elif(x == 1):
  print("Computer Chose:\n"+ paper)
elif(x == 2):
  print("Computer Chose:\n"+ scissors)
else:
  print("Invalid choice.")

if(x==0 and y==0):
  print("It is a tie.")
elif(x==0 and y==1):
  print("You win.")
elif(x==0 and y==2):
  print("Computer wins.")
elif(x==1 and y==0):
  print("Computer wins.")
elif(x==1 and y==1):
  print("It is a draw.")
elif(x==1 and y==2):
  print("You win.")
elif(x==2 and y==0):
  print("You win.")
elif(x==2 and y==1):
  print("Computer wins.")
elif(x==2 and y==2):
  print("It is a tie.")
else:
  print("Invalid choice.")
