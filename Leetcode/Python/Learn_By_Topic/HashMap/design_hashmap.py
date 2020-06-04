# Without Collision

class MyHashMap:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.modulo = 1000000
        self.key_value_hashmap = [[None, None]]*self.modulo

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        location = key % self.modulo
        self.key_value_hashmap[location] = [key, value]
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        location = key % self.modulo
        location_item = self.key_value_hashmap[location]
        if location_item and location_item[0] == key:
            return location_item[1]
        else:
            return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        location = key % self.modulo
        location_item = self.key_value_hashmap[location]
        if location_item is not None:
            self.key_value_hashmap[location] = None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)