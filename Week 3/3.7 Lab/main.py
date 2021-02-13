'''
Author: Shengye Zang
Date: Feb 12 2021
Assignment: 3.7 External Lab
'''
# get the user input for the three legs of the jog
num_miles_at_easy_pace = int(input())
num_miles_at_tempo     = int(input())
num_miles_at_easy_pace = num_miles_at_easy_pace + int(input())

# TODO: convert the time that they left their house to seconds-since-midnight
seconds_since_midnight = 6 * 60 * 60 + 52 * 60

# TODO: calculate how many seconds were spent jogging at an easy pace
sec_easy_pace = num_miles_at_easy_pace * (8 * 60 + 15)

# TODO: calulate how many seconds were spent jogging at tempo
sec_tempo = num_miles_at_tempo * (7 * 60 + 12)

# TODO: calculate the total amount of time spent jogging
total_jogging_time = sec_easy_pace + sec_tempo

# TODO: calculate the time they returned home from their jog in seconds-since-midnight
time_re_since_midnight = seconds_since_midnight + total_jogging_time

# TODO: convert the time they returned home to hours and minutes since midnight
hours = time_re_since_midnight // (60 * 60)
time_re_since_midnight -= hours * 60 * 60
minutes = time_re_since_midnight // 60

# display the time they returned home as hh:mm
print("{:d}:{:02d}".format(hours, minutes))