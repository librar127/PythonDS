import sys

class Solution:
    def thirdMax(self, nums):
        

        max_ = sys.maxsize
        min_ = -sys.maxsize - 1
        first = min_
        second = min_
        third = min_
        
        if len(nums) == 1:
            return nums[0]
    
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        for _, each in enumerate(nums):
            
            if each > first:
                if second > third:
                    third = second
                if first > second:
                    second = first
                first = each
            elif each > second and each < first:
                if second > third:
                    third = second
                second = each
            elif each > third and each < second:
                third = each
        
        if third == min_:
            return first
        else:
            return third

s = Solution()
nums = [1,2,2,4]
print(s.thirdMax(nums))