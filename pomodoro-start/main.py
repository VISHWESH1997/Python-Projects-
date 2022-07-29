from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None
# MARKS = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPS
    window.after_cancel(TIMER)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    tick_label.config(text="")
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global REPS
    REPS += 1
    print(REPS)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS % 2 == 1:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
    elif REPS % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)

    else:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)


# count_down(5 * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global REPS
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        marks =""
        start_timer()
        work_session = math.floor(REPS / 2)
        for _ in range(work_session):
            marks += "✔"
            # print(mark)
        tick_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# canvas is used to add an image on top of a window or to write something on img etc
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, font=(FONT_NAME, 30, "bold"), text="00:00", fill="white")
canvas.grid(row=2, column=2)

# count_down(5)
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)

timer_label = Label(text="Timer", font=(FONT_NAME, 28, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=1, column=2)

tick_label = Label(font=(FONT_NAME, 12, "bold"), fg=GREEN, bg=YELLOW)
tick_label.grid(row=4, column=2)

window.mainloop()
