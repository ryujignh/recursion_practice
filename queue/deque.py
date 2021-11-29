# https://recursionist.io/dashboard/course/3/lesson/415

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# ここから開発しましょう。
class Dequeue:
    def __init__(self):
        self.head = None
        self.tail = None

    # EnqueueFront - リストの先頭に要素を挿入する関数
    def enqueueFront(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = Node(data)
            self.head.prev = node
            node.next = self.head
            self.head = node

    # EnqueueBack - リストの末尾に要素を挿入する関数
    def enqueueBack(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = Node(data)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    # DequeueFront - リストの先頭にある要素を削除して返す関数
    def dequeueFront(self, data):
        if self.head is None: return None
        temp = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        return temp.data

    # DequeueBack - リストの末尾にある要素を削除して返す関数
    def dequeueBack(self, data):
        if self.tail is None: return None
        temp = self.tail
        self.tail = temp.prev

        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None

        return temp.data
