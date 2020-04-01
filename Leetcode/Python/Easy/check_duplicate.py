class Solution:
    def containsDuplicate(self, nums):
        
        hash_table = {}
        for each in nums:
            if each in hash_table:
                return True
            else:
                hash_table[each] = 1
                
        return False
    
s = Solution()
print(s.containsDuplicate([1,2,3,4]))