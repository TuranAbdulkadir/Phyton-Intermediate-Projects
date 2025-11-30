import requests
import time

def check_internet():
    try:
        requests.get("http://www.google.com", timeout=5)
        return True
    except:
        return False

while True:
    if check_internet():
        print("✅ Online")
    else:
        print("❌ Offline")
    time.sleep(5)