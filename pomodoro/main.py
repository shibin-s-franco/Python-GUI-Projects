import math
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
reps=0
my_timer=None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(my_timer)
    timer.config(text="Timer")
    canvas.itemconfig(timer_text,text="00:00")
    reps=0
    chechmark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    
    reps+=1
    work_min=WORK_MIN*60
    short_break=SHORT_BREAK_MIN*60
    long_break=LONG_BREAK_MIN*60
    if reps%8==0:
        timer.config(text="Break", fg=RED)
        count_down(long_break)
        
    elif reps%2==0:
        timer.config(text="Break", fg=PINK)
        count_down(short_break)
    else:
        timer.config(text="Work", fg=GREEN)
        count_down(work_min)
    
   
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    count_min=math.floor(count/60)
    count_sec=count%60
    # if count_sec==0:
    #     count_sec="00"
    if count_sec in range(10):
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    
    if count>0:
        global my_timer
        my_timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark=""
        mark_sesson=math.floor(reps/2)
        for _ in mark_sesson:
            mark+="✔"
            chechmark.config(text=mark)

    
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas=Canvas(width=210,height=250,bg=YELLOW,highlightthickness=0)
tomoto_img=PhotoImage(file=r"P:\PYTHON\my prog\intermediate level programs\pomodoro\tomato.png")
canvas.create_image(105,125,image=tomoto_img)
timer_text=canvas.create_text(105,143,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(row=1,column=1)

timer=Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME,35,"bold"))
timer.grid(row=0,column=1)

start=Button(text="Start",highlightthickness=0,command=start_timer)
start.grid(row=2,column=0)

reset=Button(text="Reset",highlightthickness=0,command=reset_timer)
reset.grid(row=2,column=2)

chechmark=Label(bg=YELLOW,fg=GREEN)
chechmark.grid(row=3,column=1)

window.mainloop()