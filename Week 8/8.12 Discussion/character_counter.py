characters = [] # fill this list with characters to ignore

# write a sentinel (-1) loop to enter characters 

character = input()

while character != '-1':
    characters.append(character)
    character = input()
    
user_text = input()

# write loop that iterates through the characters in user text
index = 0
count = 0
while index < len(user_text):
    if user_text[index] not in characters:
        count += 1
    index += 1
print(count)
# use a membership test on the characters list