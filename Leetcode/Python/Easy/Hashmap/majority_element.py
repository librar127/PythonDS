class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        num_dict = {}
        for each in nums:
            if each in num_dict:
                num_dict[each] += 1
                if num_dict[each] >= n/2:
                    return each
            else:
                num_dict[each] = 1
        
        majority_count = 0
        majority_element = -1
        for each in num_dict:
            if num_dict[each] > majority_count:
                majority_count = num_dict[each]
                majority_element = each
                
        return majority_element
            
sol = Solution()
nums = [2,2,1,1,1,2,2]
print(sol.majorityElement(nums))