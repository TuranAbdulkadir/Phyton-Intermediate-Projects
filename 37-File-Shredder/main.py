import os
import random
import string

filename = input("Silinecek Dosya Adı (örn: gizli.txt): ")

if os.path.exists(filename):
    file_size = os.path.getsize(filename)
    cycles = 3 # Kaç kez üzerine yazılacak
    
    print(f"⚠️ '{filename}' dosyası {cycles} kez üzerine yazılarak yok edilecek!")
    input("Devam etmek için ENTER'a bas (Geri dönüş yok!)...")
    
    with open(filename, "ba+") as delfile:
        for i in range(cycles):
            print(f"Döngü {i+1}/{cycles} işleniyor...")
            # Dosya boyutu kadar rastgele byte üret
            rand_data = os.urandom(file_size)
            # Başa dön ve yaz
            delfile.seek(0)
            delfile.write(rand_data)
            delfile.flush()
            os.fsync(delfile.fileno())
            
    # Son olarak dosyayı sil
    os.remove(filename)
    print("✅ Dosya başarıyla parçalandı ve silindi!")
else:
    print("❌ Dosya bulunamadı.")