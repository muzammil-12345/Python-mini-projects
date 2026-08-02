# Day 5 : Countdown Timer

# -----Countdown Timer-----

import time

# Step 1: Get user input for countdown start
start = int(input("Enter the number to start the countdown from: "))

# Step 2: Countdown using a while loop
print("\n--- Countdown Begins ---")
while start > 0:
  print(start)
  time.sleep(0.5)
  start -= 1

# Step 3: Print final message
print("Countdown Complete!")
