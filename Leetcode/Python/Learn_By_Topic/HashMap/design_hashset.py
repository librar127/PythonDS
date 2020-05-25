## It does not pass all testcases, need to relook 

class MyHashSet:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashset = []
        self.modulo = 10000
        
        index = 0
        while index < self.modulo:
            self.hashset.insert(index, None)
            index += 1        

    def add(self, key: int) -> None:
        location = key % self.modulo
        val = self.hashset[location]
        if val:
            if isinstance(val, list):
                if key not in val:
                    val.append(key)
                    self.hashset[location] = val
            else:
                if key == val:
                    return
                new_list = []
                new_list.append(val)
                new_list.append(key)
                self.hashset[location] = new_list
        else:
            self.hashset[location] = key
                
    def remove(self, key: int) -> None:
        if self.contains(key):            
            location = key % self.modulo
            val = self.hashset[location]
            if isinstance(val, list):
                val.remove(key)
                self.hashset[location] = val                
            else:
                self.hashset[location] = None

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        location = key % self.modulo
        val = self.hashset[location]
        if val:
            if isinstance(val, list):
                for each in val:
                    if each == key:
                        return True
            else:
                return val == key
        else:
            return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)