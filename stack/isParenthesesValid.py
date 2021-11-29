class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp

    def pop(self):
        if self.head is None: return None
        temp = self.head
        self.head = self.head.next
        return temp.data

    def peak(self):
        if self.head is None: return None
        return self.head.data


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def isParenthesesValid(parentheses):
    phashMap = {
        "{" : "}",
        "(" : ")",
        "[" : "]",
    }
    # closingParentheses = ["}", ")", "]"]

    stack = Stack()
    stack.push(parentheses[0])
    for char in parentheses[1:]:
        # If stack is not empty
        # and if char is included in phashMap
        # and if char is closing parentheses
        if stack.peak() is not None and char is phashMap.get(stack.peak()):
            stack.pop()
        else:
            stack.push(char)

    return stack.peak() is None