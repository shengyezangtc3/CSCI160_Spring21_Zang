items   = ["Homework", "Labs", "Midterm", "Final"]
weights = [.1, .4, .25, .25]

grades  = []

# TO DO: Prompt for four grades, append each grade to "grades" list
g1 = int(input())
g2 = int(input())
g3 = int(input())
g4 = int(input())
grades.append(g1)
grades.append(g2)
grades.append(g3)
grades.append(g4)

# TO DO: Compute the weighted grades and store in a new list called weighted grades
weighted_grades = []
weighted_grades.append(g1 * weights[0])
weighted_grades.append(g2 * weights[1])
weighted_grades.append(g3 * weights[2])
weighted_grades.append(g4 * weights[3])

# TO DO: Display in a nicely formatted table
print()
print('{:8}{:>10}{:>8}{:>10}{:>8}'.format('Item', 'Homework', 'Labs', 'Midterm', 'Final'))
print('=' * 44)
print('{:8}{:>10}{:>8}{:>10}{:>8}'.format('Score', g1, g2, g3, g4))
print('{:8}{:>10.1f}{:>8.1f}{:>10.1f}{:>8.1f}'.format('Weight', weights[0] * 100, weights[1] * 100, weights[2] * 100, weights[3] * 100))
print('{:8}{:>10}{:>8}{:>10}{:>8}'.format('Total', weighted_grades[0], weighted_grades[1], weighted_grades[2], weighted_grades[3]))
print()
print('Final Grade: {}'.format(sum(weighted_grades)))