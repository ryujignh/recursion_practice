import random

from card import Card


class Deck:
    def __init__(self):
        self.deck = self.generateDeck()

    @staticmethod
    def generateDeck():
        newDeck = []
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["♣", "♦", "♥", "♠"]

        for suit in suits:
            for i, value in enumerate(values):
                newCard = Card(value, suit, i + 1)
                # print(newCard.getCardString())
                newDeck.append(newCard)
            return newDeck

    def printDeck(self):
        print("Displaying cards....")
        for card in self.deck:
            print(card.getCardString())

    def shuffleDeck(self):
        deckSize = len(self.deck)
        for i in range(0, deckSize):
            j = random.randint(i, deckSize - 1)
            temp = self.deck[i]
            self.deck[i] = self.deck[j]
            self.deck[j] = temp

    def draw(self):
        return self.deck.pop()


# cards = Deck()
# cards.printDeck()
# print("shuffle-------------")
# cards.shuffleDeck()
# cards.printDeck()
