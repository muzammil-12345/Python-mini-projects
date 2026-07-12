'''
 Day 20: Event Countdown Timer suing datetime module
 Topics Covered:
 1. Understanding Datetime module
 2. Working with Dates and times
 3. Formatting Date and Time
 4. Calculating Time diffrences
 5. Mini-project: Event Countdown timer
'''
# # Understanding Date and Time module
# from datetime import datetime

# current_time = datetime.now()
# print("Current Date and time: ",current_time)

# # Working with Dates and times
# # Let's Create a specific Date and time
# event_time = datetime(2026, 10, 12, 9, 0, 0)
# print("Event Date and Time: ", event_time)

# # Formatting Date and time
# current_time = datetime.now()
# formatted_time = current_time.strftime("%d-%m-%Y %H:%M:%S")
# print("Formatted time: ", formatted_time)

# # Calculating time differences
# event_date = datetime(2026, 12, 25)
# current_date = datetime.now()
# time_difference = event_date - current_date
# print("Time difference: ",time_difference)

# --- Mini-project: Event Countdown Timer ---

# importing modules
from datetime import datetime, timedelta
import time

# Step 1: Get event Date and time from user
def get_event_datetime():
    try:
        date_input = input("Enter the event date and time (YYYY-MM-DD HH:MM:SS): ")
        return datetime.strptime(date_input, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("Invalid dat format. Please use YYYY-MM-DD HH:MM:SS")
        return None
    
# Step 2:
def calculate_time_remaining(event_date):
    current_datetime = datetime.now()
    time_difference = event_date - current_datetime
    return time_difference

# Step 3: Display Countdown
def display_countdown(time_left):
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f'\nTime Remaining: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds',end="")

# Step 4: Main Countdown loop
def start_countdown(event_date):
    while True:
        time_left = calculate_time_remaining(event_date)
        if time_left.total_seconds() <= 0:
           print('\nCountdown Complete!')
           break
        display_countdown(time_left)
        time.sleep(1)

# Step 5: Main Program
event_datetime = get_event_datetime()
if event_datetime:
    print(f"Event set for: {event_datetime}")
    start_countdown(event_datetime)