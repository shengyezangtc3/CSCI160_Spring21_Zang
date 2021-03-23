highway_number = int(input())

if 1 <= highway_number <= 99:
    if highway_number % 2 == 0:
        print('I-{} is primary, going east/west.'.format(highway_number))
    else:
        print('I-{} is primary, going north/south.'.format(highway_number))
elif 100 <= highway_number <= 999:
    if (highway_number % 100) % 2 == 0:
        print('I-{} is auxiliary, serving I-{}, going east/west.'.format(highway_number, highway_number%100))
    else:
        print('I-{} is auxiliary, serving I-{}, going north/south.'.format(highway_number, highway_number%100))
else:
    print('{} is not a valid interstate highway number.'.format(highway_number))
