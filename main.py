from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 20
reps = 0
clock = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(clock)
    timer.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Break", foreground=GREEN)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Break", foreground=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work", foreground=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global clock
        clock = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
            check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer = Label(text="Timer", highlightthickness=0, background=YELLOW, font=(FONT_NAME, 30, "bold"), fg=PINK)
timer.grid(column=1, row=0)

start = Button(text="start", background=YELLOW, highlightthickness=0, fg=PINK, font=(FONT_NAME, 10, "bold"),
               command=start_timer)
start.grid(column=0, row=3)

reset = Button(text="reset", highlightthickness=0, background=YELLOW, fg=PINK, font=(FONT_NAME, 10, "bold"),
               command=reset_timer)
reset.grid(column=3, row=3)

check_mark = Label(text="", background=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
check_mark.grid(column=1, row=4)

window.mainloop()
