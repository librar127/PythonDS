class Solution:
    def canJump(self, nums):
        
        reachable = 0
        
        for index, each in enumerate(nums):
            if reachable < index:
                return False
            reachable = max(reachable, index + each)
                
        return True