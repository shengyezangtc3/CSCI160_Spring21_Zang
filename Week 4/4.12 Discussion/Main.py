full_name = input()				# input full name, including spaces
split_name = full_name.split()	# split name (at spaces) into a list

# TO DO: Print the full name
print('Your full name is:', full_name)

# TO DO: Print the full name sur-name ordered: last, first
print('Your surname-ordered name is: {}, {}'.format(split_name[1], split_name[0]))

# TO DO: Print just the initials
print('Your initials are: {}{}'.format(split_name[0][0], split_name[1][0]))

# TO DO: Print the sum of the initials ordinals
print('The sum of your initial\'s ordinals is: {}'.format(ord(split_name[0][0]) + ord(split_name[1][0])))

# TO DO: Print the length of the full name
print('You have {} characters in your name'.format(len(full_name) - 1))