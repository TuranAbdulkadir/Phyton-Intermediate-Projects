from cryptography.fernet import Fernet
import os

# Key generation (Run once ideally)
if not os.path.exists("key.key"):
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file: key_file.write(key)
else:
    with open("key.key", "rb") as key_file: key = key_file.read()

fernet = Fernet(key)

def add(name, pwd):
    enc_pwd = fernet.encrypt(pwd.encode()).decode()
    with open("passwords.txt", "a") as f: f.write(f"{name}|{enc_pwd}\n")

def view():
    if not os.path.exists("passwords.txt"): return
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(f"User: {user} | Pass: {fernet.decrypt(passw.encode()).decode()}")

choice = input("1-Add, 2-View: ")
if choice == '1': add(input("Account Name: "), input("Password: "))
elif choice == '2': view()