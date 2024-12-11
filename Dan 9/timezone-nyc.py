from datetime import datetime
import pytz

local_timezone = pytz.timezone("America/New_York")
meeting_time = local_timezone.localize(datetime(2024, 10, 16, 14, 0))  # 2 PM local time
utc_time = meeting_time.astimezone(pytz.utc)
print(
    "Meeting Time in UTC:",
    utc_time,
    datetime.strftime(utc_time, "%Z"),
    datetime.strftime(utc_time, "%z"),
    datetime.strftime(meeting_time, "%H:%M %Z %z"),
)
