from collections import OrderedDict
class LRUCache:
    
    def __init__(self, capacity):
        self.hashmap = OrderedDict()
        self.capacity = capacity
        self.cache_size = 0
        
    def get(self, key):
        if key in self.hashmap.keys():
            
            ### return the item
            item = self.hashmap[key]

            ### And Bring the item at the front
            self.hashmap.move_to_end(key, last=False)
            #print("GET ->->", self.hashmap)
            return item

        else:
            return -1
        

    def put(self, key, value):
        
        if key in self.hashmap.keys():
           
            ### Insert / Update the key value pair
            self.hashmap[key] = value
            
            ### And Bring the item at the front
            self.hashmap.move_to_end(key, last=False)
            
             
        ### If not already existing, then check if size is full of capacity
        elif self.cache_size == self.capacity:
            #last_key = list(self.hashmap.keys())[-1]
            self.hashmap.popitem()
            
            ### Insert the new Item and bring it at the front            
            self.hashmap[key] = value
            
            ### And bright the item at front
            self.hashmap.move_to_end(key, last=False)
            
        else:
            
            ### Insert / Update the key value pair
            self.hashmap[key] = value
            
            ### And bright the item at front
            self.hashmap.move_to_end(key, last=False)
            
            ### Update the cache size
            self.cache_size += 1
            
        #print("PUT ->->", self.hashmap)


print("### Test #1")
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1)) # returns 1
cache.put(3, 3)     # evicts key 2
print(cache.get(2)) # returns -1 (not found)
cache.put(4, 4)     # evicts key 1
print(cache.get(1)) # returns -1 (not found)
print(cache.get(3)) # returns 3
print(cache.get(4)) # returns 4

print("### Test #2")
cache = LRUCache(2)
print(cache.get(2))
print(cache.put(2, 6))
print(cache.get(1))
print(cache.put(1, 5))
print(cache.put(1, 2))
print(cache.get(1))
print(cache.get(2))

print("### Test #3")
cache = LRUCache(2)
print(cache.put(2, 1))
print(cache.put(1, 1))
print(cache.put(2, 3))
print(cache.put(4, 1))
print(cache.get(1))
print(cache.get(2))