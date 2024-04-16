import sheety

print("Welcome to Flight Club.\nWe find the best flight deals and email you.")
name = input("What is your first name?\n").title()
lastname = input("What is your last name?\n").title()
email = "a"
check_email = "b"

while email != check_email:
  email = input("What is your email?\n")
  if email.lower() == "quit" or email.lower() == "exit":
    exit()
  check_email = input("Type your email again.\n")
  if check_email.lower() == "quit" or check_email.lower() == "exit":
    exit()

print("You're in the club!")

sheety.post_new_row(name, lastname, email)
