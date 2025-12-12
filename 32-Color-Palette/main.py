from PIL import Image

print("--- RENK PALETİ ÇIKARICI ---")
try:
    img = Image.open("image.jpg")
    img = img.resize((150, 150)) # İşlemi hızlandır
    result = img.convert('P', palette=Image.ADAPTIVE, colors=5) # En baskın 5 renk
    result.putalpha(0)
    colors = result.getcolors(150*150)
    
    print("Baskın Renk Kodları (RGB):")
    for count, col in colors:
        print(f"🎨 {col}")

except FileNotFoundError:
    print("❌ 'image.jpg' bulunamadı!")