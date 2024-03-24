import tkinter
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
word_dict = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/english_words.csv")
    word_dict = original_data.to_dict(orient="records")
else:
    words_dict = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_dict)
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="Turkish", fill="white")
    canvas.itemconfig(card_word, text=current_card["Turkish"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def right_word():
    words_dict.remove(current_card)
    data = pandas.DataFrame(words_dict)
    data.to.csv("data/words_to_learn.csv", index=False)
    next_card()


window = tkinter.Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")

flip_timer = window.after(3000, func=flip_card)

canvas = tkinter.Canvas(width=800, height=526)
card_front_img = tkinter.PhotoImage(file="images/card_front.png")
card_back_img = tkinter.PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 158, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

right_img = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=right_word,)
right_button.grid(column=1, row=1)

wrong_img = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()


window.mainloop()
