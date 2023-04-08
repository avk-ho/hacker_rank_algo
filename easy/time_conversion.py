# AM/PM to 24h

# "12:01:00PM" "12:01:00"
# "12:01:00AM" "00:01:00"

def time_converter(time):
    hours, mins, secs = time.split(":")
    # print(hours, mins, secs)

    is_PM = "PM" in secs
    is_12h = int(hours) == 12

    if is_PM:
        if not is_12h:
            hours = str(int(hours) + 12)
    
    else:
        if is_12h:
            hours = "00"
    
    return ":".join((hours, mins, secs[:2]))




time1 = "08:01:00PM"
time2 = "12:01:00AM"

print(time_converter(time1))
print(time_converter(time2))