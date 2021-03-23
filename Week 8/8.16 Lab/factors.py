user_num = input()
factors = []

if user_num[0] == '-':
    invalid = True
else:
    invalid = (not user_num.isnumeric()) or (int(user_num) == 0)

while invalid:
    print('{} is invalid. Try again'.format(user_num))
    user_num = input()
    if user_num[0] == '-':
        invalid = True
    else:
        invalid = (not user_num.isnumeric()) or (int(user_num) == 0)

user_num = int(user_num)
if user_num == 1:
    print('1 is a special case')
else:
    for i in range(1, user_num+1):
        if user_num % i == 0:
            factors.append(i)
    
    if len(factors) == 2:
        print('{} is prime. Only factors are 1 and {}'.format(user_num, user_num))
    else:
        print('Factors: {}'.format(factors))
        print('The largest factor that is not {} itself is: {}'.format(user_num, factors[-2]))