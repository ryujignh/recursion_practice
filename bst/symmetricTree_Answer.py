class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def symmetricTree(root):

    if root is None: return True

    return symmetricTreeHelper(root.left, root.right)


def symmetricTreeHelper(leftNode, rightNode):
    if leftNode is None and rightNode is None: return True

    if leftNode is None or rightNode is None: return False

    if leftNode.data != rightNode.data: return False

    return symmetricTreeHelper(leftNode.left, rightNode.right) and symmetricTreeHelper(leftNode.right, rightNode.left) 