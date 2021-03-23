phone_number = input()

area_code = phone_number[0:3]
prefix = phone_number[3:6]
line_number = phone_number[6:]

print('({}) {}-{}'.format(area_code, prefix, line_number))
