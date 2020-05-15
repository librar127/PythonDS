class Solution:
    def checkIfExist(self, arr):
        
        cache = set()
        for each in arr:
            if each*2 not in cache and each/2 not in cache:
                cache.add(each)
            else:
                return True
            
        return False

s = Solution()
nums = [7,1,14,11]
print(s.checkIfExist(nums))