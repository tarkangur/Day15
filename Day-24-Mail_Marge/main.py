with open("Input/Names/invited_names.txt", "r") as names:
    guest = names.readlines()

with open("Input/Letters/starting_letter.txt", "r") as start_letter:
    letter = start_letter.read()
    for n in guest:
        name = n.strip("\n")
        final_letter = letter.replace("[name]", f"{name}")
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", "x") as invite:
            invite.write(final_letter)
