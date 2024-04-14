import sheety

print("Welcome to Flight Club.\nWe find the best flight deals and email you.")
name = input("What is your first name?\n").title()
lastname = input("What is your last name?\n").title()
email = input("What is your email?\n")
check_email = input("Type your email again.\n")
if email == check_email:
  print("You're in the club!")
  sheety.post_new_row(name, lastname, email)
  
else:
  print("Wrong email")
  exit()
