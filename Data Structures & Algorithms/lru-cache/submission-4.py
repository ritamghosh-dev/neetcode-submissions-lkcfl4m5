class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.size=capacity
        self.q=deque() #Dpuble ended queue to keep track of latest visited items in Cache

    def get(self, key: int) -> int:
        if key in self.cache:
            self.q.remove(key)
            self.q.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key]=value
            self.q.remove(key)
            self.q.append(key)
        elif len(self.cache)==self.size:
            self.cache.pop(self.q.popleft())
            self.cache[key]=value
            self.q.append(key)
        else:
            self.cache[key]=value
            self.q.append(key) 

