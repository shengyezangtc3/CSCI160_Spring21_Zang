# define grades list
grades = []

# get input, convert to float
g1 = float(input())
g2 = float(input())
g3 = float(input())

# write your code below here
grades.append(g1)
grades.append(g2)
grades.append(g3)
print()
print('Your grades are')
print('Test 1:', g1)
print('Test 2:', g2)
print('Test 3:', g3)
print()
print('Your average is: {:.2f}%'.format(sum(grades) / 3))
print()
print('Lowest grade is: {}'.format(min(grades)))
print()
grades.remove(min(grades))
print('Your average after removing lowest grade is: {:.2f}%'.format(sum(grades) / 2))
print()
grades[0] = grades[0] * 105 / 100
grades[1] = grades[1] * 105 / 100
print('Your grades after applying curve are')
print('Test 1: {}'.format(grades[0]))
print('Test 2: {}'.format(grades[1]))
print()
print('Your average after applying curve is: {:.2f}%'.format(sum(grades) / 2))