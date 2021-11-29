class PairOfCardHelper:

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
            val = int(PairOfCardHelper.cardConverter(card))
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
                    winner = PairOfCardHelper.getWinnerByMaxCard(player1Pairs[key], player2Pairs[key])
                    if winner == "draw":
                        continue
                    else:
                        return winner

                elif p1PairLen > p2PairLen:
                    return "player1"
                else:
                    return "player2"
            else:
                return PairOfCardHelper.compairSingleCards(player1Pairs[key], player2Pairs[key])

        return winner

    @staticmethod
    def winnerPairOfCards(player1, player2):
        # ここから書きましょう

        player1Pairs = PairOfCardHelper.countPairs(player1)
        player2Pairs = PairOfCardHelper.countPairs(player2)

        player1Pairs = PairOfCardHelper.pairLists(player1Pairs)
        player2Pairs = PairOfCardHelper.pairLists(player2Pairs)

        winner = PairOfCardHelper.getWinner(player1Pairs, player2Pairs)
        return winner
