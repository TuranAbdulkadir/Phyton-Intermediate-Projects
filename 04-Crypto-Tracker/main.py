import requests
import time

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd"

while True:
    try:
        data = requests.get(url).json()
        print(f"BTC: ${data['bitcoin']['usd']}")
        print(f"ETH: ${data['ethereum']['usd']}")
        print(f"SOL: ${data['solana']['usd']}")
        print("-" * 20)
        time.sleep(5)
    except:
        print("Fetching data...")
        time.sleep(5)