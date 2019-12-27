class LRUCache:
    
    def __init__(self, capacity: int):
        self.hashmap = {}
        self.capacity = capacity
        self.lru_list = []
        
    def get(self, key):
        
        #print(self.hashmap, self.lru_list, key)
        
        if key in self.hashmap.keys():            
            ### Bring the item at front
            self.lru_list.remove(key) 
            self.lru_list.insert(0, key)
            return self.hashmap[key]
        else:
            return -1

    def put(self, key, value):
                
        ### If the item exists already in the LRU        
        if key in self.hashmap.keys():
            self.lru_list.remove(key)
            self.lru_list.insert(0, key) 
            self.hashmap[key] = value 
        
        ### Check the size of cache and then add/delete-add at the front 
        elif len(self.lru_list) == self.capacity:
            evicted_item = self.lru_list.pop()
            self.hashmap.pop(evicted_item, None)
            
            self.lru_list.insert(0, key)
            self.hashmap[key] = value 
            
        else:
            self.lru_list.insert(0, key)
            self.hashmap[key] = value 


cache = LRUCache( 2)

'''
### Test # 1
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1)) # returns 1
cache.put(3, 3)     # evicts key 2
print(cache.get(2)) # returns -1 (not found)
cache.put(4, 4)     # evicts key 1
print(cache.get(1)) # returns -1 (not found)
print(cache.get(3)) # returns 3
print(cache.get(4)) # returns 4

### Test #2
print(cache.get(2))
print(cache.put(2, 6))
print(cache.get(1))
print(cache.put(1, 5))
print(cache.put(1, 2))
print(cache.get(1))
print(cache.get(2))
'''

### Test #3
["LRUCache","put","put","put","put","get","get"]
[[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
print(cache.put(2, 1))
print(cache.put(1, 1))
print(cache.put(2, 3))
print(cache.put(4, 1))
print(cache.get(1))
print(cache.get(2))
