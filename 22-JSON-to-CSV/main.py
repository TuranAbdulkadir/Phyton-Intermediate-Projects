import json
import csv

# Sample JSON data (or load from file)
data = '[{"name": "Ali", "age": 25}, {"name": "Veli", "age": 30}]'
json_data = json.loads(data)

with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(json_data[0].keys()) # Header
    for row in json_data:
        writer.writerow(row.values())

print("Converted JSON to data.csv")