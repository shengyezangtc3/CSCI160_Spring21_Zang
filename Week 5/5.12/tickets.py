TICKET_PRICE = 12.99    # ticket price
age = int(input())		# age

# TO DO: Prompt for number of tickets
num_tickets = int(input())

# TO DO: Create a branching structure that selects the proper discount level
       # Calculate the discount
if age >= 65:
       print('You receive the senior citizen discount')
       if num_tickets == 1:
              print('Your total for 1 ticket is ${:.2f}'.format(1299 * 85 / 10000))
       else:
              print('Your total for {} tickets is ${:.2f}'.format(num_tickets, num_tickets * 1299 * 85 / 10000))
elif age <= 18:
       print('You receive the student discount')
       if num_tickets == 1:
              print('Your total for 1 ticket is ${:.2f}'.format(1299 * 90 / 10000))
       else:
              print('Your total for {} tickets is ${:.2f}'.format(num_tickets, num_tickets * 1299 * 90 / 10000))
else:
       print('You pay the full price')
       if num_tickets == 1:
              print('Your total for 1 ticket is $12.99')
       else:
              print('Your total for {} tickets is ${:.2f}'.format(num_tickets, num_tickets * 1299 / 100))

# TO DO: Print the results, keeping in mind the different displays for multiple or single tickets