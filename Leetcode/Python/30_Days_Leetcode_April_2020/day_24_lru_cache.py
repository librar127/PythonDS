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