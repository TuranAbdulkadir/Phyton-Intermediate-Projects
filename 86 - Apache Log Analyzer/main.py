import re

log_file = input("Log Dosyası Yolu (access.log): ")
suspicious_patterns = ["SELECT", "UNION", "OR 1=1", "<script>", "etc/passwd"]

print("[*] Log Analizi Başlatılıyor...")

try:
    with open(log_file, "r") as f:
        for line in f:
            for pattern in suspicious_patterns:
                if pattern in line:
                    # IP adresini ayıkla (Regex)
                    ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line).group()
                    print(f"[!] SALDIRI TESPİTİ! IP: {ip} -> Desen: {pattern}")
except FileNotFoundError:
    print("Dosya bulunamadı.")