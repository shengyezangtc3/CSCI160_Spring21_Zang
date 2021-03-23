import math

# TODO: get user input for whole number triangle sides a, b, and c
a = int(input())
b = int(input())
c = int(input())

if not ((a + b > c) and (a + c > b) and (b + c > a)):
    print('{}, {}, and {} do not form a triangle'.format(a, b, c))
elif a == b == c:
    print('{}, {}, and {} form an equilateral triangle'.format(a, b, c))
    if (a * a + b * b == c * c) or (a * a + c * c == b * b) or (b * b + c * c == a * a):
        print('{}, {}, and {} form a Pythagorean triple'.format(a, b, c))
    else:
        print('{}, {}, and {} do not form a Pythagorean triple'.format(a, b, c))
elif a == b or a == c or b == c:
    print('{}, {}, and {} form an isosceles triangle'.format(a, b, c))
    if (a * a + b * b == c * c) or (a * a + c * c == b * b) or (b * b + c * c == a * a):
        print('{}, {}, and {} form a Pythagorean triple'.format(a, b, c))
    else:
        print('{}, {}, and {} do not form a Pythagorean triple'.format(a, b, c))
else:
    print('{}, {}, and {} form a scalene triangle'.format(a, b, c))
    if (a * a + b * b == c * c) or (a * a + c * c == b * b) or (b * b + c * c == a * a):
        print('{}, {}, and {} form a Pythagorean triple'.format(a, b, c))
    else:
        print('{}, {}, and {} do not form a Pythagorean triple'.format(a, b, c))