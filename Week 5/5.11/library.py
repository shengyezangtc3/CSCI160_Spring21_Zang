# TODO: gather the book number from the user as a whole number
book_num = int(input())

# TODO: print out the floor that the book can be found on
# according to the table in the instructions, or an error
# message if an invalid floor number is given
if 100 <= book_num <= 199:
    print('Basement')
elif 200 <= book_num <= 500 or book_num > 900:
    print('Main Floor')
elif 700 <= book_num <= 750:
    print('Archives')
elif 501 <= book_num <= 900:
    print('Upper Floor')
else:
    print('Invalid book number')