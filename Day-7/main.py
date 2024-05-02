
import random
from hangman_words import word_list
from hangman_art import logo, stages
from replit import clear

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

#print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"
guess_letter = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

    guess_letter.append(guess)
    if guess in guess_letter:
        if guess_letter.count(guess) > 1:
            print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        if guess_letter.count(guess) > 1:
            lives == lives
        elif guess_letter.count(guess) < 2:
            print(
                f"You guessed {guess}, that's not in the word. You lose a life."
            )
            lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was: {chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
