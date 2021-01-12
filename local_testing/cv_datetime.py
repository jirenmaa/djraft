from datetime import datetime, timedelta, timezone


def convert_timedelta(duration):
    days, seconds = abs(duration.days), duration.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return hours, minutes, seconds

# td = timedelta(2, 7743, 12345)
td = timedelta(0, 86258)
hours, minutes, seconds = convert_timedelta(td)
print('{} hours, {} minutes, {} seconds'.format(hours, minutes, seconds))

print((63901 % 3600) // 60, 63901 // 3600)
