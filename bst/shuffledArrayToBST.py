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
    def __init__(self, array):
        self.shuffledArrayBST(array)

    def shuffledArrayBST(self, array):
        if len(array) == 0:
            self.root = None
        else:
            shuffledArray = random.shuffle(array)
            self.root = BinaryTree(shuffledArray[0])
            for i in range(len(shuffledArray)):
                self.insert(shuffledArray[i])

    def insert(self, value):
        iterator = self.root
        while iterator != None:
            if iterator.data > value and iterator.left == None:
                iterator.left = BinaryTree(value)
            elif iterator.data < value and iterator.right == None:
                iterator.right = BinaryTree(value)
            iterator = iterator.left if iterator.data > value else iterator.right

    def printSorted(self):
        self.root.printInOrder()
