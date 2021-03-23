suits = {
			"H" : "Hearts",
			"D" : "Diamonds",
			"C" : "Clubs",
			"S" : "Spades",
		}
		
# TO DO: Define face dictionary here

cards = {
	        "K" : "King",
			"Q" : "Queen",
			"J" : "Jack",
			"A" : "Ace"
        }

card = input() # input

# TO DO: Index the individual characters of the card input
index_cards = cards[card[0]]
index_suits = suits[card[1]]
print('{} is a {} of {}'.format(card, index_cards, index_suits))

# TO DO: Plug those into the appropriate dictionaries to extract the full string

# TO DO: Display the full string description as described in the instructions