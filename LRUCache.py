    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        # use OrderedDict to simulate LRU cache
        self.memory = OrderedDict()

    # @return an integer
    def get(self, key):
        if key in self.memory:
            value = self.memory[key]
            # remove key then add it again
            del self.memory[key]
            self.memory[key] = value
            return value
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def put(self, key, value):
        if key in self.memory:
            # remove key if already in cache
            del self.memory[key]
        self.memory[key] = value
        # pop an item (oldest) if cache is full
        if len(self.memory) > self.capacity:
            self.memory.popitem(False)

