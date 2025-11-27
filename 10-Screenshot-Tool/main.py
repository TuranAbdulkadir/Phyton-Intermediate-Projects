import pyautogui
import tkinter as tk

def shot():
    root.withdraw()
    pyautogui.screenshot("shot.png")
    root.deiconify()
    lbl.config(text="Saved: shot.png")

root = tk.Tk()
root.geometry("200x100")
lbl = tk.Label(root, text="Screenshot Tool")
lbl.pack()
tk.Button(root, text="SNAP", command=shot).pack()
root.mainloop()