user_num = int(input())
output = ''
while user_num > 0:
    output = str(user_num % 2) + output
    user_num = user_num // 2

if len(output) < 32:
    output = '0' * (32 - len(output)) + output

print(output[0:8] + '-' + output[8:16] + '-' + output[16:24] + '-' + output[24:32])