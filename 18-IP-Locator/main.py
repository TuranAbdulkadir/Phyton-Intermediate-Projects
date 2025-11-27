import geocoder

ip = geocoder.ip("me")
print(f"Your IP: {ip.ip}")
print(f"City: {ip.city}")
print(f"Country: {ip.country}")
print(f"Lat/Lng: {ip.latlng}")