# https://leetcode.com/problems/lru-cache/


class Node:
    def __init__(self, key: int, value: int):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        
    def insert(self, node: Node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.storage:
            self.remove(self.storage[key])
            self.insert(self.storage[key])
            return self.storage[key].value
        
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.storage:
            self.remove(self.storage[key])
        self.storage[key] = Node(key, value)
        self.insert(self.storage[key])

        if len(self.storage) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.storage[lru.key]


if __name__ == '__main__':
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))
    lru.put(3, 3)
    print(lru.get(2))
    lru.put(4, 4)
    print(lru.get(1))
    print(lru.get(3))
    print(lru.get(4))