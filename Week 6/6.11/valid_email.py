email_address = input()

# write your code below here
if '@' not in email_address:
    print("Invalid email. Emails require a '@'")
elif '@' == email_address[0]:
    print("Invalid email. There is an '@' but it is the first character")
elif '@' == email_address[-1]:
    print("Invalid email. There is an '@' but it is the last character")
elif '.' not in email_address:
    print("Invalid email. Emails require a '.'")
elif '.' != email_address[-4]:
    print("A '.' is present but our system requires a three letter domain. The '.' should be 4th from the end")
else:
    print('{} is a valid email'.format(email_address))
