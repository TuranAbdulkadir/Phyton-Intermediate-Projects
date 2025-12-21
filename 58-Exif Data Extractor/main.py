from PIL import Image
from PIL.ExifTags import TAGS

image_path = input("Fotoğraf Dosya Yolu: ")

try:
    image = Image.open(image_path)
    exif_data = image._getexif()

    if exif_data:
        print("\n[*] Exif Verileri Bulundu:")
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            print(f"{tag_name:25}: {value}")
    else:
        print("[-] Bu fotoğrafta Exif verisi yok.")
except IOError:
    print("Dosya açılamadı.")