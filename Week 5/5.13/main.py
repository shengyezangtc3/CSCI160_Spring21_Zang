# TODO: collect user input for three integers
a = int(input())
b = int(input())
c = int(input())

# TODO: determine whether the three integers are evenly spaced
num_list = [a, b, c]
num_list.sort()
if ((min(num_list)+max(num_list)) / 2) == num_list[1]:
    print('{}, {}, {} are evenly spaced'.format(num_list[0], num_list[1], num_list[2]))
else:
    print('{}, {}, {} are not evenly spaced'.format(num_list[0], num_list[1], num_list[2]))

# TODO: print a message according to the instructions