import time
def alarm_clock(alarm_time):
    while True:
        current_time = time.strftime('%H:%M:%S')
        if current_time == alarm_time:
            print("Alarm!")
            break
        time.sleep(1)

alarm_time = input("set the alarm(HH:MM:SS): ")
print(f'Alarm set for {alarm_time}')
alarm_clock(alarm_time)