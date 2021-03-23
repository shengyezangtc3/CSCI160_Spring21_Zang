is_leap_year = False
   
input_year = int(input())

is_leap_year = False if (input_year % 4 != 0) or (input_year % 100 == 0 and input_year % 400 != 0) else True

if is_leap_year == False:
    print('{} - not a leap year'.format(input_year))
else:
    print('{} - leap year'.format(input_year))