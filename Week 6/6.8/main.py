# TODO: get user input for the whole number of small bars
num_small = int(input())
# TODO: get user input for the whole number if large bars
num_large = int(input())
# TODO: get user input for the whole number amount of chocolate needed
amount_chocolate = int(input())

# TODO: determine how many small bars are needed after using the large bars first
small_needed = amount_chocolate - num_large * 5

# TODO: print out a message according to the instructions
if small_needed > num_small:
    print('There is not enough chocolate')
elif small_needed < 0:
    print('You need to use 0 of the small bars')
else:
    print('You need to use {} of the small bars'.format(small_needed))