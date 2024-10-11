time_12hr = input("Enter time in 12-hour format (hh:mm AM/PM): ")

# Split the input time into hours, minutes, and the AM/PM part
time, period = time_12hr.split()
hh, mm = map(int, time.split(":"))

# Convert the 12-hour time to 24-hour time
if period == "PM" and hh != 12:
    hh += 12
elif period == "AM" and hh == 12:
    hh = 0

# Print the result in 24-hour format
print(f"Time in 24-hour format: {hh:02d}:{mm:02d}")
