from datetime import datetime, timedelta, time

SPECIFIC_TIMES = [
    time(2, 30),   # 8:00 AM
    time(5, 30),   # 8:00 AM
    time(18, 0),  # 12:00 PM
    time(21, 30),  # 3:00 PM
    time(23, 0),  # 6:00 PM
]

def get_next_upload_time():
    now = datetime.now()
    today = now.date()

    # Check if any of the specific times are still available today
    for specific_time in SPECIFIC_TIMES:
        upload_time = datetime.combine(today, specific_time)
        if upload_time > now:
            return upload_time

    # If all times for today are passed, use the first time tomorrow
    first_time_tomorrow = datetime.combine(today + timedelta(days=1), SPECIFIC_TIMES[0])
    return first_time_tomorrow