string = input()

# write a for loop to iterate forwards through each character
for character in string:
    print(character)
# write a while loop to iterate backwards through each character
print()
index = len(string) - 1
while index >= 0:
    print(string[index])
    index -= 1