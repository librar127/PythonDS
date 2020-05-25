class Solution:
    def containsNearbyDuplicate(self, nums, k):
        
        hashmap = {}
        for index, each in enumerate(nums):
            if each in hashmap:
                if abs(index - hashmap[each]) <= k:
                    return True
                else:
                    hashmap[each] = index
            else:
                hashmap[each] = index
        return False
    
s = Solution()
nums, k = [1,2,3,1,2,3], 2
print(s.containsNearbyDuplicate(nums, k)) 