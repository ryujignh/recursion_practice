# 受け取った配列をシャッフルし、insertメソッド使って要素を1つずつ空の二分探索木に挿入していきます。シャッフルすることで、根ノードの選択をランダムにすることができ、平均の高さがO(logn)に近づきます。
# 例えば[1,2,3,4,5]という配列があった時、根ノードを1として順に二分探索木を作成すると、2 から 5 まで全て右側の子となってします。これは高さがO(n)となり非常に効率の悪い構造ですが、このような構造になるのは[1,2,3,4,5]と[5,4,3,2,1]の2通りしかありません。その確率は 2/5! となり要素数が増えるほど低くなります。

import math
import random


class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def printInOrder(self):
        self.inOrderWalk(self)
        print("")

    def inOrderWalk(self, tRoot):
        if tRoot is not None:
            self.inOrderWalk(tRoot.left)
            print(str(tRoot.data), end=' ')
            self.inOrderWalk(tRoot.right)


class BinarySearchTree:
    def __init__(self, arrList):
        self.generateRandomBST(arrList)

    # 受け取った配列をシャッフルしてBSTを作る関数を作ります。
    def generateRandomBST(self, arrList):
        if not arrList:
            self.root = None
        else:
            BinarySearchTree.shuffle(arrList)
            self.root = BinaryTree(arrList[0])
            for i in range(len(arrList)):
                # 　シャッフルした配列の要素を一つずつinsertでBSTに挿入します。
                self.insert(arrList[i])

    def insert(self, value):
        iterator = self.root
        while iterator is not None:
            if iterator.data > value and iterator.left == None:
                iterator.left = BinaryTree(value)
            elif iterator.data < value and iterator.right == None:
                iterator.right = BinaryTree(value)
            iterator = iterator.left if iterator.data > value else iterator.right

            # in-placeでシャッフルする関数

    @staticmethod
    def shuffle(list):
        for i in range(len(list) - 1, -1, -1):
            j = math.floor(random.randint(0, i + 1))
            [list[i], list[j]] = [list[j], list[i]]

        return list;

    @staticmethod
    def maximumDepth(root):
        if root == None: return 0
        leftdepth = BinarySearchTree.maximumDepth(root.left)
        rightdepth = BinarySearchTree.maximumDepth(root.right)
        return rightdepth + 1 if rightdepth > leftdepth else leftdepth + 1

    def printSorted(self):
        if self.root == None: return;
        self.root.printInOrder()


# 昇順に並んだ配列を作る関数
class RandomContainer:
    @staticmethod
    def generateList(size):
        list = []
        for i in range(size):
            list.append(i)

        return list


list = RandomContainer.generateList(256)
balancedBST = BinarySearchTree(list)
balancedBST.printSorted()

print(16 * 16)  # 256   要素数が増えると高さが log2n に近づきます。
print("MaxDepth: " + str(BinarySearchTree.maximumDepth(balancedBST.root)))

list2 = []
balancedBST2 = BinarySearchTree(list2)
balancedBST2.printSorted()
print("MaxDepth: " + str(BinarySearchTree.maximumDepth(balancedBST2.root)))