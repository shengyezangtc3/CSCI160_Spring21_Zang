'''
Author: Shengye Zang
Date: Feb12 2021
Assignment: 3.8 External Lab
'''

item_name = input('Enter food item name:\n')

# FIXME (1): Finish reading item price and quantity, then output a receipt
item_price = float(input('Enter item price:\n'))
item_quantity = int(input('Enter item quantity:\n'))
total_cost = item_price * item_quantity

print()
print('RECEIPT')
print('{:d} {:s} @ ${:.2f} = ${:.2f}'.format(item_quantity, item_name, item_price, total_cost))
print('Total cost: ${:.2f}'.format(total_cost))
print()
print()
   
# FIXME (2): Read in a second food item name, price, and quantity, then output a second receipt
item2_name = input('Enter second food item name:\n')
item2_price = float(input('Enter item price:\n'))
item2_quantity = int(input('Enter item quantity:\n'))
total_cost += item2_price * item2_quantity

print()
print('RECEIPT')
print('{:d} {:s} @ ${:.2f} = ${:.2f}'.format(item_quantity, item_name, item_price, item_quantity * item_price))
print('{:d} {:s} @ ${:.2f} = ${:.2f}'.format(item2_quantity, item2_name, item2_price, item2_price * item2_quantity))
print('Total cost: ${:.2f}'.format(total_cost))
   
# FIXME (3): Add a gratuity and total with tip to the second receipt
gratuity = total_cost * 0.15

print()
print('15%', 'gratuity: ${:.2f}'.format(gratuity))
print('Total with tip: ${:.2f}'.format(total_cost + gratuity))
