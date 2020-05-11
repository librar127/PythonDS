class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_count_so_far = 0
        current_count = 0
        
        for _, each in enumerate(nums):
            if each == 1:
                current_count += 1
            else:
                if current_count > max_count_so_far:
                    max_count_so_far = current_count
                current_count = 0
        if current_count > max_count_so_far:
            return current_count
        else:
            return max_count_so_far
    
s  = Solution()
nums = [1,1,0,1,1,1]
print(s.findMaxConsecutiveOnes(nums))