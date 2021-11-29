import math


class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        # 左の二分木
        self.left = left
        # 右の二分木
        self.right = right


# BinarySearchTreeという構造体を作成してください。

class BinarySearchTree:
    def __init__(self, arr):
        sorted_arr = sorted(arr)
        self.root = BinarySearchTree.sortedArrayToBSHelper(sorted_arr, 0, len(sorted_arr) - 1)

    def sortedArrayToBSHelper(arr, start, end):
        if start == end: return BinaryTree(arr[start], None, None)

        mid = math.floor((start + end) / 2)

        left = None
        if mid - 1 >= start: left = BinarySearchTree.sortedArrayToBSHelper(arr, start, mid - 1)

        right = None
        if mid + 1 <= end: right = BinarySearchTree.sortedArrayToBSHelper(arr, mid + 1, end)

        root = BinaryTree(arr[mid], left, right)
        return root

    def keyExist(self, key):

        iterator = self.root
        while iterator != None:
            if iterator.data == key:
                return True
            # keyがnodeより大きかったら右に行く
            elif iterator.data < key:
                iterator = iterator.right
            # keyがnodeより大きかったら左に行く
            else:
                iterator = iterator.left

        return False

    def search(self, key):
        iterator = self.root
        while iterator != None:
            if iterator.data == key:
                return iterator
            elif iterator.data < key:
                iterator = iterator.right
            # keyがnodeより大きかったら左に行く
            else:
                iterator = iterator.left
        return None


# 根ノードの部分木 subT を返します。キーが BinarySearchTree 内に見つからない場合は null を返します。Exists(key) は、キーを受け取り、そのキーが BinarySearchTree 内に存在するかどうかを判定するブーリアン値を返します。


balancedBST = BinarySearchTree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
print(balancedBST.keyExist(6))
print(balancedBST.search(6).data)
print(balancedBST.keyExist(2))
print(balancedBST.search(2).data)
print(balancedBST.search(34))
