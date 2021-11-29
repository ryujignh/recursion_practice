class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def reverseInorderTraversal(root):
    results = []

    results = reverseInorderTraversalHelper(root, results)
    return results


def reverseInorderTraversalHelper(root, results):
    if root:
        reverseInorderTraversalHelper(root.right, results)
        results.append(root.data)
        reverseInorderTraversalHelper(root.left, results)

    return results

# preorderTraversal(preorderTraversal([0, -10, 5, None, -3, None, 9])) # [0, -10, -3, 5, 9]
