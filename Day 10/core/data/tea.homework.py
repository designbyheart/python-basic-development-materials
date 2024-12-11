from datetime import datetime, time


def is_time_in_range(start, end, current):
    return start <= current <= end


start_time = time(9, 0)  # start time needs to be before end time
end_time = time(17, 0)
current_time = datetime.now().time()

if is_time_in_range(start_time, end_time, current_time):
    print("Within working hours")
elif current_time < start_time:
    print("It's not during working hours.")
else:
    print("Closed.")
