## https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3247
class Solution:
    def removeElement(self, nums, val):
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
            else:
                start += 1
        return start
    
s = Solution()
nums = [0,1,2,2,3,0,4,2]
print(s.removeElement(nums, 2)) 