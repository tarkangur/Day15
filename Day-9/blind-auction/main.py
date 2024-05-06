from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
name_and_bid = {}

bidders = "yes"
while bidders == "yes":
    name = input("What is your name?:")
    bid = input("What's your bid?: $")

    name_and_bid[name] = bid

    other_bidders = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if other_bidders == "yes":
        bidders = "yes"
    else:
        bidders = "no"
    clear()

sorted_name_and_bid = dict(
    sorted(name_and_bid.items(), key=lambda x: int(x[1]), reverse=True))

keys_list = list(sorted_name_and_bid.keys())
values_list = list(sorted_name_and_bid.values())

print(f"The winner is {keys_list[0]} with a bit of ${values_list[0]}.")
