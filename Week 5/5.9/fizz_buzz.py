
# TODO: get an integer from the user
user_num = int(input())

# TODO: print out fizz and buzz based on the instructions
if (user_num % 3 == 0) and (user_num % 5 == 0):
    print('fizzbuzz')
elif user_num % 3 == 0:
    print('fizz')
elif user_num % 5 == 0:
    print('buzz')
else:
    print('Neither fizz nor buzz nor fizzbuzz')