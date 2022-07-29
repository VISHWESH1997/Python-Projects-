from tkinter import *
from pandas import *
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
# ---------------------------Info from file----------------------#
try:
    data = read_csv("./data/words_to_learn.csv")
    data_dict = data.to_dict(orient='records')
except FileNotFoundError:
    data = read_csv("./data/french_words.csv")
    data_dict = data.to_dict(orient='records')
    # data_dict_learn = data.to_dict()
    # new_data = DataFrame(data_dict_learn)
    # print(new_data)
    # new_data.to_csv("./data/words_to_learn.csv", index=False)
    # print(data_dict)
    # data_dict = data.to_dict(orient='records')
# french_words = [i for i in data.French]
current_card = {}


# ------------------- next word ----------------------------#


def the_english_word():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(lang_text, text="English", fill="white")
    canvas.itemconfig(words, text=f"{current_card['English']}", fill="white")
    # window.after_cancel()


def next_french_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(lang_text, text="French", fill="black")
    canvas.itemconfig(words, text=f"{current_card['French']}", fill="black")
    flip_timer = window.after(3000, func=the_english_word)
    # window.after(1000)
    # canvas.itemconfig(words, text=f"{current_card['English']}")

    # the_english_word(current_card)


def tick():
    global current_card
    next_french_word()
    print(len(data_dict))
    data_dict.remove(current_card)
    new_data = DataFrame(data_dict)
    new_data.to_csv("./data/words_to_learn.csv", index=False)

    # next_french_word()
    # data_dict.remove(current_card)
    # print(data_dict_learn)


window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=the_english_word)

# canvas front card

# row start : 0 column start : 0

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 268, image=front_image)
lang_text = canvas.create_text(400, 150, text="Title", font=(FONT_NAME, 40, "italic"))
words = canvas.create_text(400, 263, text="Word", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# right button
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, relief="flat",
                      bg=BACKGROUND_COLOR, borderwidth=0, command=tick)
right_button.grid(row=1, column=1)

# wrong button
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, relief="flat",
                      bg=BACKGROUND_COLOR, borderwidth=0, command=next_french_word)
wrong_button.grid(row=1, column=0)

next_french_word()
# Labels
#
# language = Label(text="Title", font=(FONT_NAME, 35, "italic"), bg="white")
# language.place(x=300, y=130)
#
# word = Label(text="Word", font=(FONT_NAME, 45, "bold"), bg="white")
# word.place(x=300, y=233)


window.mainloop()
