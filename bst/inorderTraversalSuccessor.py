class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def successor(root, key):
    # ここから書きましょう

    # Search the Node
    keyNode = find(root, key)
    if keyNode is None: return None

    # Case 1: KeyNode has right subtree
    # Find the next larger value of the KeyNode
    if keyNode.right is not None:
        return findMin(keyNode.right)

    # Case 2: No right subtree
    else:
        successor = None
        ancestor = root
        while ancestor != keyNode:
            if keyNode.data < ancestor.data:
                successor = ancestor
                ancestor = ancestor.left
            else:
                ancestor = ancestor.right
    return successor

def findMin(root):
    if root is None: return None
    while root.left is not None:
        root = root.left

    return root

def find(root, key):
    while root is not None:
        if root.data == key:
            return root

        elif root.data < key:
            root.parent = root
            root = root.right
        else:
            root.parent = root
            root = root.left

    return None
