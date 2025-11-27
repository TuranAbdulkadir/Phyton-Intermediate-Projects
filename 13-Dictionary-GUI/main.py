from PyDictionary import PyDictionary
import tkinter as tk

dictionary = PyDictionary()

def search():
    word = entry.get()
    meaning = dictionary.meaning(word)
    result.config(text=str(meaning['Noun'][0]) if meaning else "Not found")

root = tk.Tk()
root.geometry("400x300")
root.title("Dictionary")

tk.Label(root, text="Enter Word:").pack(pady=10)
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Search", command=search).pack(pady=10)
result = tk.Message(root, text="", width=350)
result.pack()

root.mainloop()