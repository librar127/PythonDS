class Solution:
    def findDisappearedNumbers(self, nums):
        if len(nums) < 2:
            return []
            
        
        for each in nums:
            index = abs(each)-1
            nums[abs(each)-1] = -1*abs(nums[abs(each)-1])
        
        out_list = []
        
        for index, each in enumerate(nums):
            if each > 0:
                out_list.append(index+1)
                
        return out_list

s = Solution()
nums = [4,3,2,7,8,2,3,1]
print(s.findDisappearedNumbers(nums))