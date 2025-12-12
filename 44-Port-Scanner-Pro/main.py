import socket
import threading
from queue import Queue

target = input("Taranacak IP: ")
print("Hızlı tarama başlatılıyor (1-500 arası)...")

def port_scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        con = s.connect((target, port))
        print(f"🔥 PORT AÇIK: {port}")
        s.close()
    except:
        pass

# Threading mekanizması
def worker():
    while True:
        port = q.get()
        port_scan(port)
        q.task_done()

q = Queue()

# 50 tane işçi (thread) çalıştır
for x in range(50):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

# 1'den 500'e kadar portları kuyruğa ekle
for worker in range(1, 501):
    q.put(worker)

q.join()
print("Tarama Bitti.")