# Mike は友達 3 人とお金を賭けながらサイコロゲームで遊んでいます。このゲームでは 36 面で構成されているサイコロを n 回振ることができサイコロの目が出ると$4獲得し、蓄積していくことができます。
# ただし、目が前の数字よりも低い場合、バーストし、今までの蓄積は全て失われます。バーストは $4 獲得の前に起こります。
# プレイヤーのサイコロ目を表す配列 player1、player2、player3、player4 が与えられるので、勝利プレイヤー、
# その金額、勝利を決定した連続部分配列を文字列として返す、diceStreakGamble という関数を作成してください。
# ただし、最終的に獲得した金額が同じ場合は最初にサイコロを投げた人を優先してください。
# このゲームではプレイヤー1、2、3、4の順にサイコロを投げます。


# 入力のデータ型： integer[] player1, integer[] player2, integer[] player3, integer[] player4
# 出力のデータ型： string
# diceStreakGamble([1,2,3],[3,4,2],[4,2,4],[6,16,4]) --> Winner: Player 1 won $12 by rolling [1,2,3]
# diceStreakGamble([1,2,3,-1,4,5],[3,4,2],[4,2,4],[6,16,4]) --> Winner: Player 1 won $12 by rolling [-1,4,5]
# diceStreakGamble([4,3,2,1],[4,3,2,1],[4,3,2,1],[4,3,2,1]) --> Winner: Player 1 won $4 by rolling [1]
# diceStreakGamble([1,2,3],[3,4,2],[4,2,4],[6,16,26]) --> Winner: Player 1 won $12 by rolling [1,2,3]
# diceStreakGamble([1,2,1],[3,4,2],[4,2,4],[6,16,26]) --> Winner: Player 4 won $12 by rolling [6,16,26]
# diceStreakGamble([5,19,19,20],[23,23,32,5],[20,23,30,23],[12,20,24,29]) --> Winner: Player 1 won $16 by rolling [5,19,19,20]
# diceStreakGamble([10,9,9,9,1,4],[10,9,9,9,1,4],[0,1,3,6,2,8],[1,2,2,1,0,1]) --> Winner: Player 1 won $8 by rolling [1,4]
# diceStreakGamble([2,45,56,6,4,10,34,20,3,4],[20,45,56,6,4,3,5,3,2,20],[3,4,20,20,21,30,33,35,35,36],[3,4,20,45,56,6,4,3,5,9]) --> Winner: Player 3 won $40 by rolling [3,4,20,20,21,30,33,35,35,36]
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self,data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp

    def pop(self):
        if self.head == None: return None
        temp = self.head
        self.head = self.head.next
        return temp.data

    def peek(self):
        if self.head is None: return None
        return self.head.data

def consecutiveWalk(arr):
    print(f"arr: {arr}")
    stack = Stack()
    stack.push(arr[0])
    for i in arr[1:]:
        if stack.peek() > i:
            while stack.peek() is not None: stack.pop()
        stack.push(i)

    results = []
    while stack.peek() is not None: results.insert(0,stack.pop())
    print(f"results: {results}")
    return results

def diceStreakGamble(player1,player2,player3,player4):
    list = [consecutiveWalk(player1), consecutiveWalk(player2),consecutiveWalk(player3), consecutiveWalk(player4)]

    winner_point = [len(list[0]), len(list[1]), len(list[2]), len(list[3])]
    winner_index = winner_point.index(max(winner_point)) + 1
    winner_list = str(list[winner_index-1])

    return "Winner: Player " + str(winner_index) + " won $" + str(max(winner_point)*4) + " by rolling " + winner_list.replace(' ', '')

# print(diceStreakGamble([1, 2, 3], [3, 4, 2], [4, 2, 4], [6, 16, 4]))  # --> Winner: Player 1 won $12 by rolling [1,2,3]
# print(diceStreakGamble([1, 2, 3], [3, 4, 2], [4, 2, 4], [6, 16, 4]))

# print(diceStreakGamble([1, 2, 3, -1, 4, 5], [3, 4, 2], [4, 2, 4],
#                        [6, 16, 4]))  # --> Winner: Player 1 won $12 by rolling [-1,4,5]
# print(diceStreakGamble([4, 3, 2, 1], [4, 3, 2, 1], [4, 3, 2, 1],
#                        [4, 3, 2, 1]))  # --> Winner: Player 1 won $4 by rolling [1]

# players = [33,2,31,24,16,9,8,20,29,36,7,17,10,15,9,9,6,26,34,9,34,12],[16,11,10,18,1,14,6,18,35,31,13,15,24,36,14,19,36,4,32,9,15,34],[6,5,10,3,11,10,19,29,22,30,5,19,35,33,7,13,36,12,21,26,14,14],[12,34,15,34,6,24,24,28,11,23,2,7,18,7,10,19,9,10,10,21,15,3]
# print(diceStreakGamble(players))  # --> Winner: Player 1 won $4 by rolling [1]

# print(diceStreakGamble([13,23,15,2,35],[3,20,10,4,10],[8,12,1,23,27],[11,11,25,5,25]))  # "Winner: Player 3 won $12 by rolling [1,23,27]"
# print(diceStreakGamble([10,21,5,26,1,29,15,27,28,17,5,8,34,15,19,13,4,35,18,10,20,31,1,18,2,4,16,27],[34,26,22,12,2,36,7,33,26,17,10,12,29,26,30,24,25,23,10,36,6,14,8,12,9,15,24,11],[6,22,20,24,31,26,14,15,32,27,34,16,34,21,29,23,7,19,35,34,15,27,25,27,14,29,18,8],[7,13,21,23,6,25,3,32,17,12,28,10,21,32,29,12,15,33,5,27,27,2,32,27,3,15,10,22]))
# "Winner: Player 1 won $16 by rolling [2,4,16,27]"

# print(diceStreakGamble([31,14,22,24,15,18,6,21,5,20,36,1,28,3,20,26,1,36,22,19,31,2,3,22],[11,3,30,17,16,19,29,8,16,1,8,10,24,12,24,32,19,14,21,17,30,13,25,32],[2,19,34,15,20,30,32,22,23,23,10,22,11,14,2,19,13,14,14,25,3,30,17,18],[14,29,20,17,22,18,25,24,27,36,3,14,33,18,6,12,12,35,29,29,21,10,27,30]))
# "Winner: Player 1 won $12 by rolling [2,3,22]"

print(diceStreakGamble([5, 19, 19, 20], [23, 23, 32, 5], [20, 23, 30, 23], [12, 20, 24, 29]))
# "Winner: Player 1 won $16 by rolling [5,19,19,20]"

[5, 19, 19, 20], [23, 23, 32, 5], [20, 23, 30, 23], [12, 20, 24, 29]
