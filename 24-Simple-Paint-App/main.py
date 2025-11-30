import tkinter as tk

root = tk.Tk()
root.title("Simple Paint")

canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack()

def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill="black", width=5)

canvas.bind("<B1-Motion>", paint)
root.mainloop()