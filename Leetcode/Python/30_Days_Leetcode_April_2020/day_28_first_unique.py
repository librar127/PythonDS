class FirstUnique:
    
    def arrange(self):
        self.hashmap = {}
        for each in self.nums:
            if each in self.hashmap:
                self.hashmap[each] += 1
            else:                
                self.hashmap[each] = 1
        
    def __init__(self, nums):
        self.nums = nums
        self.hashmap = {}
        self.pointer = 0
        
        self.arrange()

    def showFirstUnique(self):
        if len(self.nums) <= 0:
            return -1
        
        for index in range(self.pointer, len(self.nums)):
            self.pointer = index
            if self.hashmap[self.nums[index]] == 1:
                return self.nums[index]
            
        return -1 

    def add(self, value):
        self.nums.append(value)
        
        if value in self.hashmap:
            self.hashmap[value] += 1
        else:                
            self.hashmap[value] = 1