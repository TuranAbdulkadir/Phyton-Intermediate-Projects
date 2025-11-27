import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
titles = soup.find_all("span", class_="titleline")

print("--- HACKER NEWS TOP 5 ---")
for i, title in enumerate(titles[:5]):
    print(f"{i+1}. {title.text}")