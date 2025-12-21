import qrcode

url = input("QR Koda Dönüştürülecek Link: ")
img = qrcode.make(url)

file_name = "malicious_qr.png"
img.save(file_name)

print(f"[+] QR Kod oluşturuldu: {file_name}")