modifiers = {

		"i"	: "1",
		"a" : "@",
		"m" : "M",
		"B" : "8",
		"s" : "$",
		"e" : "3",
		"o" : "0",
		"h"	: "4",
}


word = input()
password = ''

for i in range(len(word)):
	if word[i] in modifiers:
		password += modifiers[word[i]]
	else:
		password += word[i]

password += '!'
print(password)