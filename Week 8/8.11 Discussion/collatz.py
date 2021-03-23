# write your validation loop here
user_num = input()
valid = (user_num.isnumeric()) and (int(user_num) > 0)
while not valid:
    print('{} IS INVALID'.format(user_num))
    user_num = input()
    valid = (user_num.isnumeric()) and (int(user_num) > 0)

print()
print('Hailstone sequence for: {}'.format(user_num))
# write your collatz loop here
current = int(user_num)
count = 1
print(current, end='  ')
while current != 1:
    if current % 2 == 0:
        current = current // 2
        count += 1
        print(current, end='  ')
    else:
        current = current * 3 + 1
        count += 1
        print(current, end='  ')
print()
print('Hailstone sequence for {} has {} elements'.format(user_num, count))
        