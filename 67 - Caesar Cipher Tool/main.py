def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

text = input("Metin: ")
shift = int(input("Kaydırma Sayısı (örn: 3): "))
print(f"Şifreli Metin: {encrypt(text, shift)}")