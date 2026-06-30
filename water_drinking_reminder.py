import time
from plyer import notification

def water_reminder(interval_minutes):
    interval_seconds = interval_minutes * 60

    print("Water Drinking Reminder Started...")
    
    # 1. Send an immediate notification to test if it works!
    notification.notify(
        title="Reminder Active!",
        message=f"You will be reminded every {interval_minutes} minutes.",
        app_name="Hydration App",
        timeout=5
    )

    while True:
        time.sleep(interval_seconds)
        notification.notify(
            title="Drink Water 💧",
            message="Time to take a sip and stay hydrated.",
            app_name="Hydration App",
            timeout=10
        )

# Test with 1 minute for quick validation, change back to 30 later!
water_reminder(1)