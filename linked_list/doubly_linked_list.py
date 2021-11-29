class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self, arr):
        if len(arr) <= 0:
            self.head = Node(None)
            self.tail = self.head
            return

        self.head = Node(arr[0])
        currentNode = self.head
        for i in range(1, len(arr)):
            currentNode.next = Node(arr[i])
            currentNode.next.prev = currentNode
            currentNode = currentNode.next

        self.tail = currentNode

    def at(self, index):
        iterator = self.head;
        for i in range(0, index):
            iterator = iterator.next
            if iterator == None: return None

        return iterator

    # def reverse(self):
    #     reverse = self.tail
    #     iterator = self.tail.prev
    #
    #     currentNode = reverse
    #     while iterator is not None:
    #         currentNode.next = iterator
    #
    #         iterator = iterator.prev
    #         if iterator is not None: iterator.next = None
    #
    #         currentNode.next.prev = currentNode
    #         currentNode = currentNode.next
    #
    #     self.tail = currentNode
    #     self.head = reverse
    #     self.head.prev = None

    def reverse(self):
        current = self.head

        while current is not None:
            next = current.next
            current.next = current.prev
            current.prev = next
            current = next

        current = self.head
        self.head = self.tail
        self.tail = current
        # while iterator is not None:
        #     currentNode.next = iterator
        #
        #     iterator = iterator.prev
        #     if iterator is not None: iterator.next = None
        #
        #     currentNode.next.prev = currentNode
        #     currentNode = currentNode.next
        #
        # self.tail = currentNode
        # self.head = reverse
        # self.head.prev = None

    def printInReverse(self):
        iterator = self.tail;
        while(iterator != None):
            print(iterator.data, end=" ")
            iterator = iterator.prev
        print()

    def printList(self):
        iterator = self.head;
        while(iterator != None):
            print(iterator.data, end=" ")
            iterator = iterator.next
        print()

    def append(self, newNode):
        temp = self.head
        self.head = newNode
        current = self.head
        current.next = temp
        temp.prev = current

    def prepend(self, newNode):
        temp = self.tail
        self.tail = newNode
        # current = self.head
        self.tail.prev = temp
        temp.next = self.tail

    def addNextNode(self, node, newNode):
        temp = node
        print(temp)
        next = temp.next
        temp.next = newNode
        next.prev = newNode
        newNode.next = next
        newNode.prev = temp

numList = DoublyLinkedList([35,23,546,67,86,234,56,767,34,1,98,78,555])
# numList.printList()
# numList.reverse()
# numList.printList()
# numList.append(Node(1))
# numList.printList()
#
# numList.append(Node(1))
# numList.printList()

numList.addNextNode(numList.at(78), Node(679))
numList.printList()

# numList.printInReverse()