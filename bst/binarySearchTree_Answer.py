import math

class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        # 左の二分木
        self.left = left
        # 右の二分木
        self.right = right

# BinarySearchTreeという構造体を作成してください。
class BinarySearchTree:
    def __init__(self, arrList):
        sortedList = sorted(arrList)
        self.root = BinarySearchTree.sortedArrayToBST(sortedList)

    @staticmethod
    def sortedArrayToBST(array):
        if len(array) == 0: return None
        return BinarySearchTree.sortedArrayToBSTHelper(array, 0, len(array)-1)

    @staticmethod
    def sortedArrayToBSTHelper(arr, start, end):
        if start == end: return BinaryTree(arr[start], None, None);

        mid = math.floor((start+end)/2)

        left = None;
        if mid-1 >= start: left = BinarySearchTree.sortedArrayToBSTHelper(arr, start, mid-1)

        right = None
        if mid+1 <= end: right = BinarySearchTree.sortedArrayToBSTHelper(arr, mid+1, end)

        root = BinaryTree(arr[mid], left, right)
        return root

    def keyExist(self, key):
        iterator = self.root
        while iterator is not None:
            if iterator.data == key:return True
            if iterator.data > key: iterator = iterator.left
            else: iterator = iterator.right

        return False

    def search(self, key):
        iterator = self.root
        while iterator is not None:
            if iterator.data == key: return iterator
            if iterator.data > key: iterator = iterator.left
            else: iterator = iterator.right

        return None

balancedBST = BinarySearchTree([1,2,3,4,5,6,7,8,9,10,11])
print(balancedBST.keyExist(6))
print(balancedBST.search(6).data)
print(balancedBST.keyExist(2))
print(balancedBST.search(2).data)
print(balancedBST.search(34))