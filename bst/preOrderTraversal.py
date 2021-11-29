class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


def preorderTraversal(root):
    results = []

    results = preorderTraversalHelper(root, results)
    return results

def preorderTraversalHelper(root, results):
    if root:
        results.append(root.data)
        preorderTraversalHelper(root.left, results)

        preorderTraversalHelper(root.right, results)

    return results

# preorderTraversal(preorderTraversal([0, -10, 5, None, -3, None, 9])) # [0, -10, -3, 5, 9]
