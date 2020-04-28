from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.order = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key not in self.storage:
            return None
        value = self.storage[key]
        node = self.order.head
        while node:
            if node.value == value:
                self.order.move_to_end(node)
                break
            node = node.next
        return value[1]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        value = (key, value)
        if key in self.storage:
            self.storage[key] = value
            node = self.order.head
            while node:
                if node.value == value:
                    self.order.move_to_tail(node)
                    return
                else:
                    node = node.next
        if len(self.storage) == self.limit:
            node = self.order.head
            self.order.delete(node)
            del self.storage[node.value[0]]
        self.order.add_to_tail(value)
        self.storage[key] = value
        # print(self.storage[key][1])
        # print(self.order.tail.value)


cache = LRUCache(3)
cache.set('item2', 'b')
cache.set('item3', 'c')
cache.set('item1', 'a')
cache.set('item2', 'z')
print("a ==", cache.get('item1'))
# # c.set("a", 1)
# # c.set("b", 3)
# # c.set("a", 2)
# # c.set("c", 4)
# # print("here", c.get("a"))
# # print(c.get("c"))
# # print(c.get("b"))
#

