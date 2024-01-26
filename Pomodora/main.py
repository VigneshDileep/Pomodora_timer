import tkinter
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
timer = None
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    window.after_cancel(time)
    timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text= "00:00")
    tick_mark.config(text="")
    reps = 0




# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = 25 * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 2 == 0 and reps < 7:
        count_down(short_break_sec)
        timer.config(text="BREAK", fg=PINK)
    elif reps == 8:
        count_down(long_break_sec)
        timer.config(text="BREAK", fg=RED)
    elif reps % 2 != 0 and reps != 9:
        timer.config(text="WORK", fg=GREEN)
        count_down(work_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global time
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        time = window.after(1000, count_down, count - 1)
    if count ==  0:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        tick_mark.config(text= mark)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodroro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer = tkinter.Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, highlightthickness=0, bg=YELLOW)
timer.grid(column=1, row=0)

start_button = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

tick_mark = tkinter.Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
tick_mark.grid(column=1, row=3)

window.mainloop()
