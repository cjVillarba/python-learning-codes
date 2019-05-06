class Card:
	
	special_names= {1:'Ace', 11:'Jack', 12:'Queen',13:'King'}
	
	def __init__(self, suit,pips):
		self.suit = suit
		self.pips = pips
	
	def __str__(self):
		card_name = Card.special_names.get(self.pips,str(self.pips))
		return "%s of %s (S)" % (card_name,self.suit)
		
	def __repr__(self):
		card_name = Card.special_names.get(self.pips,str(self.pips))
		return "%s of %s (R)" % (card_name,self.suit)
		
ace_of_spades = Card("Spades",1)
my_hand = [ace_of_spades]

print(ace_of_spades)
print(my_hand)	

str_card = str(ace_of_spades)
print(str_card)

repr_card = repr(ace_of_spades)
print(repr_card)