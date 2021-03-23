# TODO: get the percentage of cloud coverage from the user as a whole number
cloud_percentage = int(input())

# TODO: print a message about how cloudy it is according to the table in the instructions
if 0 <= cloud_percentage <= 30:
    print('Clear')
elif 31 <= cloud_percentage <= 70:
    print('Partly Cloudy')
elif 71 <= cloud_percentage <= 99:
    print('Cloudy')
elif cloud_percentage == 100:
    print('Overcast')
else:
    print('Invalid Input')