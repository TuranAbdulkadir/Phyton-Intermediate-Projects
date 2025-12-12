import tkinter as tk
import requests

def get_weather():
    city = entry.get()
    api_key = "464522430030245466542525" # (Örnek key, çalışmazsa openweathermap'ten alman gerekebilir)
    # Test için herkese açık bir API kullanıyoruz:
    url = f"https://wttr.in/{city}?format=%C+%t"
    
    try:
        response = requests.get(url)
        lbl_result.config(text=f"Durum: {response.text}")
    except:
        lbl_result.config(text="Hata: Şehir bulunamadı.")

root = tk.Tk()
root.title("Hava Durumu App")
root.geometry("300x200")

tk.Label(root, text="Şehir Girin:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 12))
entry.pack()

tk.Button(root, text="Sorgula", command=get_weather, bg="orange").pack(pady=10)
lbl_result = tk.Label(root, text="...", font=("Arial", 14, "bold"))
lbl_result.pack()

root.mainloop()