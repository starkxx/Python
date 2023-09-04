password_list= []
for char in range (1,nr_letters+1):
  password_list.append(random.choice(letters))
  print(password_list)
for char in range(1,nr_symbols+1):
  password_list.append(random.choice(symbols))
  print(password_list)
for char in range(1,nr_numbers):
  password_list.append(random.choice(numbers))
  print(password_list)
  random.shuffle(password_list)
  password=""
  print(password_list)
  for char in password_list:
    password+=char
  print(f"Your password is :{password}")
