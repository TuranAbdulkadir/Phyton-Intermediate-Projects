import psutil

print(f"CPU Usage: {psutil.cpu_percent()}%")
print(f"RAM Usage: {psutil.virtual_memory().percent}%")
print(f"Battery: {psutil.sensors_battery().percent}%")