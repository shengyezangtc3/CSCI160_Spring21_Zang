user_num = int(input())

for n in range(1, user_num+1):
    if n % 15 == 0:
        print('FIZZBUZZ')
    elif n % 3 == 0:
        print('FIZZ')
    elif n % 5 == 0:
        print('BUZZ')
    else:
        print(n)
    