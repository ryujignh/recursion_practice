class Card:
    def __init__(self, value, suit, intValue):
        self.value = value
        self.suit = suit
        self.initValue = intValue

    def getCardString(self):
        return self.suit + self.value + "(" + str(self.initValue) + ")"


card1 = Card("A", "♦︎", 1)

# 出力して確認
print(card1.getCardString())
print(card1.initValue)
print(card1.value)
print(card1.suit)
