class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def symmetricTree(root):
    if root is None: return True
    # ここから書きましょう

    # Left tree inorder traversal
    leftNodes = []
    leftNodes = inorderTraversalHelper(root.left, leftNodes)

    rightNodes = []
    rightNodes = reverseInorderTraversalHelper(root.right, rightNodes)
    print(leftNodes)
    print(rightNodes)
    return leftNodes == rightNodes


def inorderTraversalHelper(root, results):
    if root:
        inorderTraversalHelper(root.left, results)
        results.append(root.data)
        inorderTraversalHelper(root.right, results)
    else:
        results.append(None)

    return results


def reverseInorderTraversalHelper(root, results):
    if root:
        reverseInorderTraversalHelper(root.right, results)
        results.append(root.data)
        reverseInorderTraversalHelper(root.left, results)
    else:
        results.append(None)

    return results
