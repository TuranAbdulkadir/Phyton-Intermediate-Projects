import tkinter as tk
from tkinter import filedialog

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension="txt")
    if not filepath: return
    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Notepad Clone - {filepath}")

window = tk.Tk()
window.title("Python Notepad")

txt_edit = tk.Text(window)
btn_save = tk.Button(window, text="💾 Farklı Kaydet", command=save_file, bg="blue", fg="white")

btn_save.pack(fill=tk.X)
txt_edit.pack(expand=True, fill=tk.BOTH)

window.mainloop()