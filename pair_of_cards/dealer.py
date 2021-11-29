from deck import Deck


class Dealer:

    @staticmethod
    def startGame(amountOfPlayers, gameMode):
        print(amountOfPlayers)
        table = {
            "players": [],
            "gameMode": gameMode,
            "deck": Deck()
        }

        # Shuffle deck
        table["deck"].shuffleDeck()

        for person in range(0, amountOfPlayers):
            # Player's deck
            playerCard = []

            # Use two cards for Blackjack
            # print(gameMode)
            for i in range(0, Dealer.initialCards(gameMode)):
                playerCard.append(table["deck"].draw())
            table["players"].append(playerCard)

        return table

    # Get initial set of cards
    @staticmethod
    def initialCards(gameMode):
        if gameMode == "21":
            return 2
        if gameMode == "poker":
            return 5
        if gameMode == "Pair of Cards":
            return 5

    @staticmethod
    def printTableInformation(table):
        print("Amount of players: " + str(len(table["players"])) + "... Game mode: " + table[
            "gameMode"] + ". At this table: ")

        for i, player in enumerate(table["players"]):
            print(str(i + 1) + "player's cards: ")
            for card in player:
                print(card.getCardString())

    @staticmethod
    def score21Individual(cards):
        value = 0
        for card in cards:
            value += card.initValue

        return value if 21 >= value >= 1 else 0

    # ブラックジャックで誰が勝利したか表示する関数を作成します。
    # それぞれのプレイヤーの手札をscore21Individualで計算し、配列に保存します。例: [10,16,15,16,15,15]
    # この場合、勝利するプレイヤーが複数存在することから、cache[10] = 1, cache[15] = 3, cache[16] = 2のように書き換えます。
    # 配列 [10,16,15,16,15,15]の最大値は16で、cache[16] > 1なのでドローになります。
    # もし、0 <= cache[16] <= 1なら、そのプレイヤーの勝利、それ以外の場合は勝者が誰もいないことになります。
    # ではこのロジックを関数にしてみましょう。
    @staticmethod
    def winnerOf21(table):
        points = []
        cache = {}
        for cards in table["players"]:
            point = Dealer.score21Individual(cards)
            print(point)
            points.append(point)
            if point in cache:
                cache[point] += 1
            else:
                cache[point] = 1

            print(cache)
            print(points)

            winnerIndex = HelperFunctions.maxInArrayIndex(points)
            if cache[points[winnerIndex]] > 1:
                return "It is a draw"
            elif cache[points[winnerIndex]] >= 0:
                return "player " + str(winnerIndex + 1) + " is the winner"
            else:
                return "No winners.."

    @staticmethod
    def pairLists(pairMap):
        result = {
            4: [],
            3: [],
            2: [],
            1: [],
        }

        for key in pairMap:
            if pairMap[key] in result:
                result[pairMap[key]].append(key)

        return result

    # Get pairs count
    @staticmethod
    def countPairs(cards):
        pairMap = {
            14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0,
            8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0,
        }

        for card in cards:
            val = int(Dealer.cardConverter(card))
            pairMap[val] += 1

        return pairMap

    # Convert char values to int
    @staticmethod
    def cardConverter(card):
        convertables = {
            "A": 14, "K": 13, "Q": 12, "J": 11
        }

        val = card[1:]

        if val in convertables:
            return convertables[val]
        else:
            return val

    # Compair the strongest card in of pairs
    @staticmethod
    def getWinnerByMaxCard(player1Pairs, player2Pairs):
        p1Max = max(player1Pairs)
        p2Max = max(player2Pairs)
        result = "draw"

        if p1Max > p2Max:
            result = "player1"
        elif p1Max < p2Max:
            result = "player2"

        print("getWinnerByMaxCard: " + result)
        return result

    # Compair the strongest card when both player don't have any pairs
    @staticmethod
    def compairSingleCards(player1SingleCards, player2SingleCards):
        print(player1SingleCards)
        print(player2SingleCards)
        minRound = min(len(player1SingleCards), len(player2SingleCards))
        print("minRound: " + str(minRound))
        result = "draw"

        for i in range(0, minRound):
            print(i)
            p1 = player1SingleCards[i]
            p2 = player2SingleCards[i]
            if p1 > p2:
                return "player1"
            elif p1 < p2:
                return "player2"
            else:
                result = "draw"
        return result

    @staticmethod
    def getWinner(player1Pairs, player2Pairs):
        winner = "draw"

        for key in player1Pairs:
            # If both player don't have a pair in this key(2,3, or 4)
            p1PairLen = len(player1Pairs[key])
            p2PairLen = len(player2Pairs[key])
            print("key: " + str(key))
            if key > 1:
                if p1PairLen == 0 and p2PairLen == 0:
                    continue
                elif p1PairLen > 0 and p2PairLen > 0:
                    winner = Dealer.getWinnerByMaxCard(player1Pairs[key], player2Pairs[key])
                    if winner == "draw":
                        continue
                    else:
                        return winner

                elif p1PairLen > p2PairLen:
                    return "player1"
                else:
                    return "player2"
            else:
                return Dealer.compairSingleCards(player1Pairs[key], player2Pairs[key])

        return winner

    @staticmethod
    def winnerPairOfCards(player1, player2):
        # ここから書きましょう

        player1Pairs = Dealer.countPairs(player1)
        player2Pairs = Dealer.countPairs(player2)

        player1Pairs = Dealer.pairLists(player1Pairs)
        player2Pairs = Dealer.pairLists(player2Pairs)

        winner = Dealer.getWinner(player1Pairs, player2Pairs)
        return winner


class HelperFunctions:

    @staticmethod
    def maxInArrayIndex(intArr):
        maxIndex = 0
        maxValue = intArr[0]
        for i, num in enumerate(intArr):
            if num > maxValue:
                maxValue = num
                maxIndex = i

        return maxIndex


# PlayerAの手札
# card1 = Card("♦︎", "A", 1)
# card2 = Card("♦︎", "J", 11)
#
# # PlayerBの手札
# card3 = Card("♦︎", "9", 9)
# card4 = Card("♦︎", "K", 13)
#
# print(Dealer.score21Individual([card1, card2]))
# print(Dealer.score21Individual([card3, card4]))
# # 最大値は19(= index 2)
# arr1 = [1, 9, 19, 3, 4, 6]
# print(HelperFunctions.maxInArrayIndex(arr1))
#
# # 最大値は5(= index 0)
# arr2 = [5, 2, 1, 3, 5, 5]
# print(HelperFunctions.maxInArrayIndex(arr2))
# table = Dealer.startGame(2, "21")
# Dealer.printTableInformation(table)
# print(Dealer.winnerOf21(table))


table = Dealer.startGame(2, "Pair of Cards")
Dealer.printTableInformation(table)
print(Dealer.winnerPairOfCards(table))
