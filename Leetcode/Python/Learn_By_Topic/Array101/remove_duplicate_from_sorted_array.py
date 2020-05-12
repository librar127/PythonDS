## https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3248/
class Solution:
    def removeDuplicates(self, nums):
        
        index = 0
        while index < len(nums)-1:
            if nums[index] == nums[index+1]:
                nums.pop(index+1)
            else:
                index += 1
        return len(nums)
    
    
        ## Approach 2 
        start = 0
        index = 0
        while index < len(nums)-1:            
            if nums[index] != nums[index+1]:
                nums[start+1] = nums[index+1]
                start += 1
                index += 1
            else:
                index += 1
                
        return start+1
    
s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(s.removeDuplicates(nums)) 