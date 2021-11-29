class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


def bstSearch(root, key):
    return bstSearchHelper(root, key)

def bstSearchHelper(root, key):
    if root is None: return None
    if root is key: return root

    bstSearchHelper(root.left, key)
    bstSearchHelper(root.right, key)


# bstSearch(preorderTraversal([0, -10, 5, None, -3, None, 9])) # [0, -10, -3, 5, 9]
