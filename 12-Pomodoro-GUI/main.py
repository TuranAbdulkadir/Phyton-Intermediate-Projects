import tkinter as tk
import time

def start_timer():
    work_sec = 25 * 60
    count_down(work_sec)

def count_down(count):
    min_s = count // 60
    sec_s = count % 60
    canvas.itemconfig(timer_text, text=f"{min_s:02}:{sec_s:02}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        label.config(text="Break Time!")

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg="#f7f5dd")

label = tk.Label(text="Timer", fg="#9bdeac", bg="#f7f5dd", font=("Arial", 35, "bold"))
label.pack()

canvas = tk.Canvas(width=200, height=224, bg="#f7f5dd", highlightthickness=0)
timer_text = canvas.create_text(100, 112, text="25:00", fill="black", font=("Arial", 35, "bold"))
canvas.pack()

start_btn = tk.Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.pack()

window.mainloop()