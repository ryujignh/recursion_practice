class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def inorderTraversal(root):
    results = []

    results = inorderTraversalHelper(root, results)
    return results


def inorderTraversalHelper(root, results):
    if root:
        inorderTraversalHelper(root.left, results)

        results.append(root.data)

        inorderTraversalHelper(root.right, results)

    return results

# preorderTraversal(preorderTraversal([0, -10, 5, None, -3, None, 9])) # [0, -10, -3, 5, 9]
