money = float(input())
reward = 0
if money <= 0:
    print('Invalid input: money recovered must be positive.')
elif money <= 75000:
    reward = float(money * 10 / 100)
    print('Reward for ${:.2f} is ${:.2f}'.format(money, reward))
elif money <= 100000:
    reward = float(7500 + (money - 75000) * 5 / 100)
    print('Reward for ${:.2f} is ${:.2f}'.format(money, reward))
else:
    reward = float(7500 + 1250 + (money - 100000) * 1 / 100)
    if reward >= 50000:
        print('Reward for ${:.2f} is $50000.00'.format(money))
    else:
        print('Reward for ${:.2f} is ${:.2f}'.format(money, reward))