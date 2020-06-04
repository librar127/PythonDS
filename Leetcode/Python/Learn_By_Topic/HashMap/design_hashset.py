## Without Collision
class MyHashSet:
        
    def __init__(self):
        """
        Initialize your data structure here.
        """        
        self.modulo = 1000000
        self.hashset = [None]*self.modulo

    def add(self, key: int) -> None:
        """
        Add an item to Hashset if not already exists        
        Arguments: Key to be inserted        
        Return: None
        """
        location = key % self.modulo
        if not self.hashset[location]:
            self.hashset[location] = key
                
    def remove(self, key: int) -> None:
        """
        Delete an item from Hashset if already exists   
             
        Arguments: Key to be deleted        
        Return: None        
        """
        location = key % self.modulo
        self.hashset[location] = None

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element        
        Argument: Key to be searched for        
        return: Boolean flag with True or False
        """
        location = key % self.modulo
        return self.hashset[location] == key
    