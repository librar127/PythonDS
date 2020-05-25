class Solution:
    def containsDuplicate(self, nums):
        
        hash_table = set()
        for each in nums:
            if each in hash_table:
                return True
            else:
                hash_table.add(each)
                
        return False