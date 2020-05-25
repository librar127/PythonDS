class Solution:
    
    def twoSum(self, nums, target):
        
        #    This can be solved three different ways:
        #    1. Brute force approach = O(n^2)
        #    2. With Sorting and two pointers - start and end = O(NLogN)
        #    3. Using HashMaps - Time: O(N) Space: O(N)
        
        
        hashmap = {}
        for index, each in enumerate(nums):
            if each not in hashmap:
                hashmap[each] = index
        
        for index, each in enumerate(nums):  
            if target-each in hashmap.keys():
                if index == hashmap[target-each]:
                    pass
                else:
                    return sorted([index, hashmap[target-each]])