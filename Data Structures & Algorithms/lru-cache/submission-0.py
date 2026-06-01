class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.nest = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # dict, compare if len(cache) < capacity:
        # remove the LRU/element at head of the LL
        self.cache = {}
        # Dummy LRU/MRU end nodes
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        # connect them, doubly-LL
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        
    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.next, node.prev = next, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # remove + reinsert at right, making it MRU
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            # the val in the dict is pointer to node, so get the val
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove the LRU from LL, and delete LRU from the cache/dict
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
