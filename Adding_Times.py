'''
This program will calculate and display the time an alarm will sound.
Times are in military format using a 24 hour cycle: 00:00:00 - 23:59:59
The beginning time is specified in the code. Modify this to play around
The alarm time will be entered via user input as 3 quantities: hours, minutes, seconds
This program does not take into account times that will exceed a 24 hour period
I'll leave that to you as a fun challenge
'''
# EXTRA CHALLENGE: Account for times that exceed 24 hours

# begnning time
hours   = 3
minutes = 45
seconds = 15

# alarm time via user input. Convert input to integer
alarm_hours     = int(input("How many hours? "))
alarm_minutes   = int(input("How many minutes? "))
alarm_seconds   = int(input("How many seconds? "))

'''
EXTRA CHALLENGE: Allow time to be entered in "HH:MM:SS" format with a single input statement
instead of indidivual quantities and "slice out" the indviduals fields. This wll require the 
concept of string slicing (foreshadowing).You can either research this online or read ahead 
a bit in zyBooks
'''

# normalize each time into a quantity of seconds
total_seconds = hours * 3600 + minutes * 60 + seconds
total_seconds_alarm = alarm_hours * 3600 + alarm_minutes * 60 + alarm_seconds

# add them together to create the new time
new_time = total_seconds + total_seconds_alarm

# convert back to HH:MM:SS. We will assume that days are not involved
new_hours = new_time // 3600    # divide out the hours
new_time = new_time % 3600      # how many seconds remain after dividing out hours

new_minutes = new_time // 60    # divide out the minutes
new_time = new_time % 60        # how many seconds are left over after dividing out hours

'''
the {:02d} formatting rule is saying: pad with 0's up to 2 digits.
This is necessary because Python will not show "leading zeroes".
When the variable's value is inserted into the string at these locations
that format rule will be followed; only if the value needs a leading zero
'''
print("Alarm will go off at: {:02d}:{:02d}:{:02d}".format(new_hours, new_minutes, new_time))