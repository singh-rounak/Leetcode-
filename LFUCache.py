from collections import defaultdict, OrderedDict


class Node:
    def __init__(self, key, val, freq):
        self.key = key
        self.val = val
        self.freq = freq
    

class LFUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.min_freq = None
        
        # hash map for key-node
        self.key2node = dict()
        
        # doubly-linked hash map
        self.freq2node = defaultdict(OrderedDict)

    def get(self, key):
        if key not in self.key2node:
            return -1
        
        node = self.key2node[key]
        # cuz node has been "get", its frequency would go up
        # remove its old pair in freq2node
        del self.freq2node[node.freq][key]
        
        # further check whether old node.freq is empty in freq2node
        if not self.freq2node[node.freq]:
            del self.freq2node[node.freq]
        
        # update node in freq2node
        node.freq += 1
        self.freq2node[node.freq][key] = node
        
        # update min_freq
        if not self.freq2node[self.min_freq]:
            self.min_freq += 1
    
        return node.val
        

    def put(self, key, value): 
        if not self.capacity:
            return 
        
        if key in self.key2node:
            self.key2node[key].val = value
            # update key 
            _ = self.get(key)
            return 
        
        # already reached capacity limit
        if len(self.key2node) == self.capacity:
            # remove least frequently used node
            k, node = self.freq2node[self.min_freq].popitem(last=False)
            del self.key2node[k]
        
        self.freq2node[1][key] = self.key2node[key] = Node(key, value, 1)
        self.min_freq = 1
        return 
