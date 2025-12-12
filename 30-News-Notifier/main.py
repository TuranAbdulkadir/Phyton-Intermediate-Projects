from plyer import notification
import requests
import time

# BBC News RSS akışından başlık çekme (Basit yöntem)
print("Haberler kontrol ediliyor...")

# Örnek statik bildirim (API key derdi olmasın diye)
news_title = "Breaking News: Python is Awesome!"
news_msg = "Python developers act like wizards in the tech world."

notification.notify(
    title=news_title,
    message=news_msg,
    app_icon=None,
    timeout=10
)

print("✅ Masaüstü bildirimi gönderildi!")