class LRUCache:
    class Node:
        def __init__(self, val = 0, key = 0, prev = None, next = None):
            self.val = val
            self.key = key
            self.prev = prev
            self.next = next

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.capacity = capacity

        self.head = self.Node()
        self.tail = self.Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if not key in self.hashmap:
            return -1
        
        # detach
        self.hashmap[key].prev.next = self.hashmap[key].next
        self.hashmap[key].next.prev = self.hashmap[key].prev
        
        # attach
        self.hashmap[key].next = self.head.next
        self.head.next.prev = self.hashmap[key]
        self.hashmap[key].prev = self.head
        self.head.next = self.hashmap[key]
        
        return self.hashmap[key].val
        
        
        

    def put(self, key: int, value: int) -> None:        
        # update node value
        if key in self.hashmap:
            self.hashmap[key].val = value

            # detach
            self.hashmap[key].prev.next = self.hashmap[key].next
            self.hashmap[key].next.prev = self.hashmap[key].prev
            
        else:
            # check capacity
            if len(self.hashmap) == self.capacity:
                del self.hashmap[self.tail.prev.key]
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev

            self.hashmap[key] = self.Node(value, key)
        
        # attach
        self.hashmap[key].next = self.head.next
        self.head.next.prev = self.hashmap[key]
        self.hashmap[key].prev = self.head
        self.head.next = self.hashmap[key]
            
        
        

        
