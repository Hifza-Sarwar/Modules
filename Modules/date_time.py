from datetime import datetime
from datetime import date
import time
# Print the current date and time.
print(datetime.now())

# Print today's date only.
print(date.today())

# Display the message "Program Started", wait for 5 seconds, then display "Program Finished".

print("Program started")
time.sleep(0.6)
print("Wait for 5 seconds....")
time.sleep(5)
print("Program finished")

