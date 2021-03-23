# use this list to easily translate a month number to Month string
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
input_date = input()

# use string slicing to extract the month and day
month = int(input_date[0:2])
date = int(input_date[3:5])
year = int(input_date[6:10])

# use the month number as the basis for an index into the months lists to extract to full month string
if month < 1 or month > 12:
    print('Invalid Month')
    exit()
if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or 
    month == 10 or month == 12) and (date < 1 or date > 31):
    print('{}: Invalid Day'.format(months[month-1]))
    exit()
if (month == 4 or month == 6 or month == 9 or month == 10) and (date < 1 or date > 30):
    print('{}: Invalid Day'.format(months[month-1]))
    exit()
if month == 2:
    if year % 4 == 0 and (date < 1 or date > 29):
        print('{}: Invalid Day'.format(months[month-1]))
        exit()
    elif year % 4 != 0 and (date < 1 or date > 28):
        print('{}: Invalid Day'.format(months[month-1]))
        exit()

if (month == 3 and 20 <= date <= 31) or month == 4 or month == 5 or (month == 6 and 1 <= date <= 20):
    print('{}: Spring'.format(months[month-1]))

if (month == 6 and 21 <= date <= 30) or month == 7 or month == 8 or (month == 9 and 1 <= date <= 21):
    print('{}: Summer'.format(months[month-1]))     

if (month == 9 and 22 <= date <= 30) or month == 10 or month == 11 or (month == 12 and 1 <= date <= 20):
    print('{}: Autumn'.format(months[month-1]))
        
if (month == 12 and 21 <= date <= 31) or month == 1 or month == 2 or (month == 3 and 1 <= date <= 19):
    print('{}: Winter'.format(months[month-1]))


