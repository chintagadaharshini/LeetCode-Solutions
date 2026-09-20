class MyHashMap(object):

    def __init__(self):
        self.buckets=[[] for _ in range(1000)]
        

    def put(self, key, value):
        index=key%1000
        for i, pair in enumerate(self.buckets[index]):
            if pair[0]==key:
                self.buckets[index][i]=(key,value)
                return
        self.buckets[index].append((key, value))

        

    def get(self, key):
        index=key%1000
        for pair in self.buckets[index]:
            if pair[0]==key:
                return pair[1]
        return -1
        

    def remove(self, key):
        index=key%1000
        for i, pair in enumerate(self.buckets[index]):
            if pair[0]==key:
                self.buckets[index].pop(i)
                return

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)