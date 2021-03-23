a = int(input())
b = int(input())

if a % b == 0:
    print('{} is a factor of {}'.format(b, a))
else:
    print('{} is not a factor of {}'.format(b, a))