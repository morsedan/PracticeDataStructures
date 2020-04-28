class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_head(self, value):
        if self.head is not None:
            node = self.head
            self.head = ListNode(value)
            self.head.next = node
            node.prev = self.head
        else:
            self.head = ListNode(value)
            self.tail = self.head

    def add_to_tail(self, value):
        if self.tail is not None:
            node = self.tail
            self.tail = ListNode(value)
            node.next = self.tail
            self.tail.prev = node
        else:
            self.tail = ListNode(value)
            self.head = self.tail



dll = DoublyLinkedList()
dll.add_to_head(42)
dll.add_to_head(11)
dll.add_to_head(4)

dll.add_to_tail(55)

node = dll.head
while node is not None:
    print(node.value)
    node = node.next