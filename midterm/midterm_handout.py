
# dictionary of the valid months and their numbers
months = {
    1  : "January",
    2  : "February",
    3  : "March",
    4  : "April",
    5  : "May",
    6  : "June",
    7  : "July",
    8  : "August",
    9  : "September",
    10 : "October",
    11 : "November",
    12 : "December"
}

# dictionary of the different ticket classes
ticket_class = {
    "VIP"       : 200,
    "First"     : 100,
    "Business"  : 50,
    "Economy"   : 0
}

# available seats
seats = ["A3", "A5", "B3", "B4", "C5", "D2", "D4", "E2", "E3"]

# BEGIN USER INPUT AND VALIDATION
#================================
print("WELCOME TO THE TICKET CHECKER")
print("==============================")
print()

input_date = input("Enter the date of the ticket in MM/DD/YYYY format: ")
date = input_date.split("/")
month = date[0]
if (not month.isnumeric()) or (int(month) not in months):
    exit("{} is not a valid month. Ticket cannot be processed. Aborting program".format(month))
month = int(month)

ticket = input("Enter the ticket class (VIP, First, Economy, Business): ")
if ticket not in ticket_class:
    exit("'{}' is not a valid ticket class. Aborting program".format(ticket))

age = int(input("Enter the age: "))
if age <= 0:
    exit("Age must be larger than 0. Aborting program")

num_carry_bag = int(input("How many carry on bags? (0/1): "))
if not 0 <= num_carry_bag <= 1:
    exit("Proper input is 0 or 1 for carry on bags. Aborting program")

num_checked_bag = int(input("How many checked bags? "))
if num_checked_bag < 0:
    exit("This must be a number greater than or equal to 0. Aborting program")

print()
# BEGIN PROCESSING TICKET CHARGE
# ==============================
base_charge = 300

if age < 2:
    base_charge = 0
if 60 <= age < 80:
    base_charge = 290.
if age >= 80:
    base_charge = 200

class_charge = ticket_class[ticket]
carry_charge = 0
checked_charge = 0
if num_carry_bag == 1:
    carry_charge = 10
if num_checked_bag == 2:
    checked_charge = 25
elif num_checked_bag > 2:
    checked_charge = 25 + (num_checked_bag - 2) * 50

total_charge = base_charge + class_charge + carry_charge + checked_charge
    
# DISPLAY OUTPUT
# ==============
print("Available Seats: {}".format(seats))
print()
seat = seats[0]
seats.remove(seat)
seat_aisle = seat[0]
seat_num = seat[1]
print("TICKET SUMMARY")
print("=========================")
format_string = '{title:<17} {content:<18}'
print(format_string.format(title='Ticket Date:', content=months[month]+' '+date[1]+', '+date[2]))
print(format_string.format(title='Passenger Age:', content=age))
format_string = '{title:<17} ${content:.2f}'
print(format_string.format(title='Base Charge:', content=base_charge))
print(format_string.format(title=ticket+' Class:', content=class_charge))
print(format_string.format(title=str(num_carry_bag)+' Carry On:', content=carry_charge))
print(format_string.format(title=str(num_checked_bag)+'Checked Bag(s):', content=checked_charge))
format_string = '{title:<17} {content:<18}'
print(format_string.format(title='Seat Aisle:', content=seat_aisle))
print(format_string.format(title='Seat Number:', content=seat_num))
print("=========================")
format_string = '{title:<17} ${content:.2f}'
print(format_string.format(title='Total Charge:', content=total_charge))
print()
print("Available Seats: {}".format(seats))