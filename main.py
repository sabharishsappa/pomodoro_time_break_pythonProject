from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0
timer = None
marks =""

# ---------------------------- TIMER RESET ------------------------------- #

def timer_reset():
    window.after_cancel(timer)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text,text="00:00")
    checkmarks.config(text="")
    global reps
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps+=1
    work_sec = int(WORK_MIN*60)
    short_break_sec = int(SHORT_BREAK_MIN*60)
    long_break_sec = int(LONG_BREAK_MIN*60)

    if reps%8 ==0:
        count_down(long_break_sec)
        title_label.config(text="Break",fg=RED)

    if reps %2 ==0:
        count_down(short_break_sec)
        title_label.config(text="Break",fg=PINK)

    else:
        count_down(work_sec)
        title_label.config(text="Work",fg=GREEN)


# -------------------  --------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = count//60
    count_sec = count%60

    if count_sec<10:
        count_sec = f"0{count_sec}"

    if count_min<10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark =""
        work_sessions = reps//2
        for _ in range(work_sessions):
            mark+="✔"
        checkmarks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodora")
window.config(padx=100,pady=50,bg=YELLOW)
# window.minsize(height=600,width=600)

title_label = Label(text="Timer", font=(FONT_NAME,50,"normal"),fg=GREEN,bg=YELLOW)
title_label.grid(row=0,column=1)


# canvas widget
tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
# canvas.create_window(width=200,height=224)
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",font=(FONT_NAME,35,"bold"),fill="white")
canvas.grid(row=1,column=1)

start_button = Button(text="Start",highlightbackground=YELLOW,command=start_timer)
start_button.grid(column=0,row=2)
reset_button = Button(text="Reset",highlightbackground=YELLOW,command=timer_reset)
reset_button.grid(column=2,row=2)

checkmarks = Label(bg=YELLOW,fg=GREEN)
checkmarks.grid(column=1,row=3)


window.mainloop()