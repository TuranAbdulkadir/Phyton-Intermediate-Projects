import smtplib

sender_email = "senin_email@gmail.com"
password = "uygulama_sifresi" # Gmail App Password
receiver_email = input("Alıcı Email: ")
message = "Subject: Test Maili\n\nBu Python botu tarafindan gonderilmistir."

try:
    # Gmail SMTP Sunucusu
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    
    server.sendmail(sender_email, receiver_email, message)
    print("[+] Mail başarıyla gönderildi!")
except Exception as e:
    print(f"[-] Hata: {e}")
finally:
    server.quit()