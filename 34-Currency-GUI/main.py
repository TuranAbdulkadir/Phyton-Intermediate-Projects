import tkinter as tk

def convert():
    try:
        usd = float(entry_usd.get())
        # Örnek sabit kur (APIsiz çalışsın diye)
        try_rate = 34.50 
        result = usd * try_rate
        lbl_result.config(text=f"{result:.2f} TL")
    except ValueError:
        lbl_result.config(text="Sayı girin!")

root = tk.Tk()
root.title("Döviz Çevirici")
root.geometry("250x150")

tk.Label(root, text="USD Miktarı:").pack(pady=5)
entry_usd = tk.Entry(root)
entry_usd.pack()

tk.Button(root, text="Çevir (TL)", command=convert, bg="green", fg="white").pack(pady=10)
lbl_result = tk.Label(root, text="0.00 TL", font=("Arial", 16, "bold"))
lbl_result.pack()

root.mainloop()