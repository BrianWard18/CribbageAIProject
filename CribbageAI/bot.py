# from Cards import Cards
from Cards import Deck
class Bot:
    
    def __init__ (self, currentDeck):
        self.currentDeck = currentDeck

    def newDeck(self, currentDeck):
        self.currentDeck = currentDeck

	#Bot recieves a hand consisting of 6 cards. 
	#*AS OF NOW* bot will simply discard the first two cards in the hand
	#output will be ((list of new deck), (list of discarded deck))
    def discard(self, six_card_deck):
        discard_list = []
        # print("BOT's CURRENT HAND (discard two):")
        # for card in six_card_deck:
        #     self.currentDeck.showCard(card)
        
        discard_list.append(six_card_deck[0])
        six_card_deck.remove(six_card_deck[0])
        discard_list.append(six_card_deck[0])
        six_card_deck.remove(six_card_deck[0])
        
        # print("BOT's NEW HAND (discarded):")
        # for card in six_card_deck:
        #     self.currentDeck.showCard(card)

        return (six_card_deck, discard_list)

	#hand represents a list of Cards
    # *AS OF NOW* bot will play the first card in the hand
    def playCard(self, hand):
        # print("BOT'S PLAYABLE HAND:")
        # for card in hand:
        #     self.currentDeck.showCard(card)
        
        cardTmp = hand[0]
        return cardTmp

if __name__ == "__main__":
	testDeck = Deck()
	test = Bot(testDeck)
	hand = testDeck.dealHand()
	temp = test.discard(hand)[0]
	print(test.playCard(temp))


