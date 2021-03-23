valid    = False
user_num = 0
count    = 1

# write your code below here
user_num = input()
valid = (user_num.isnumeric()) and (int(user_num) >= 0)
while not valid:
    print('{} IS INVALID'.format(user_num))
    user_num = input()
    valid = (user_num.isnumeric()) and (int(user_num) >= 0)
    count += 1

if count == 1:
    print('It took you 1 time to get it right')
else:
    print('It took you {} times to get it right'.format(count))