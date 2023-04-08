class Node():
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = {} #map key to node

        #left = Least recent(LRU), right = most recent
        self.right, self.left = Node(0,0), Node(0,0)
        self.right.prev, self.left.next = self.left, self.right
        
    #remove node from the list
    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    #insert node at right
    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        prv.next = nxt.prev =node
        node.next, node.prev = nxt, prv


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache)>self.cap:
            #remove from the list and delete the lru from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
