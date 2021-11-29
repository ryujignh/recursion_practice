class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def postorderTraversal(root):
    results = []

    results = postorderTraversalHelper(root, results)
    return results


def postorderTraversalHelper(root, results):
    if root:
        postorderTraversalHelper(root.left, results)
        postorderTraversalHelper(root.right, results)
        results.append(root.data)

    return results

# preorderTraversal(preorderTraversal([0, -10, 5, None, -3, None, 9])) # [0, -10, -3, 5, 9]
