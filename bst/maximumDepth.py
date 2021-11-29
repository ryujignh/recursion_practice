class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def maximumDepth(root):
    if root is None:
        return 0

    stack = [[root, 1]]
    res = 1

    while stack:
        node, depth = stack.pop()

        if node:
            res = max(res, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])

    return res

# https://www.youtube.com/watch?v=hTM3phVI6YQ&t=259s