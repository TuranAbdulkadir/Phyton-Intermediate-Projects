import psutil
from plyer import notification
import time

battery = psutil.sensors_battery()
percent = battery.percent

notification.notify(
    title="Battery Status",
    message=f"{percent}% Battery remaining",
    timeout=5
)
print(f"Battery: {percent}%")