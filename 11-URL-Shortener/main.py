import pyshorteners

def shorten(url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)

print("--- URL SHORTENER ---")
url = input("Enter long URL: ")
print(f"Short URL: {shorten(url)}")