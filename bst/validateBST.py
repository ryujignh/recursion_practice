class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def validateBST(root):
    # ここから書きましょう

    return valid(root, float("-inf"), float("inf"))


def valid(root, left, right):
    if not root:
        return True
    if not (root.data < right and root.data > left):
        return False
    return (valid(root.left, left, root.data) and root(root.right, root.data, right))