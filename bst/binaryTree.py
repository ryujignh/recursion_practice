import math

class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        # 左の二分木
        self.left = left
        # 右の二分木
        self.right = right

def sortedArrayToBSTHelper(arr, start, end):
    if start == end: return BinaryTree(arr[start], None, None)


    mid = math.floor((start+end)/2)
    print(f"start: {start}, end: {end} mid: {mid}")

    left = None
    if mid-1 >= start: left = sortedArrayToBSTHelper(arr, start, mid-1)
    # if left is not None:
    #     print(f"left: {left.data}")
    # else:
    #     print(f"left: {left}")

    right = None
    if mid+1 <= end: right = sortedArrayToBSTHelper(arr, mid+1, end)
    # print(f"right: {right.data}")

    root = BinaryTree(arr[mid], left, right)
    print(f"root.data: {root.data}, root.left: {root.left}, root.right: {root.right}")
    return root

def sortedArrayToBST(nums):
    if len(nums) == 0: return None
    return sortedArrayToBSTHelper(nums, 0, len(nums)-1)

balancedBST = sortedArrayToBST([1,2,3,4,5,6,7,8,9,10,11])
print(balancedBST)