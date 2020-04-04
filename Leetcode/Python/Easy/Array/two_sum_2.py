class Solution:
    
    def twoSumwithSorting(self, nums, target):
        sorted_nums = sorted(nums)
        start = 0
        end = len(nums)-1
        while start <= end:
            if target > sorted_nums[start] + sorted_nums[end]:
                start += 1
            elif target < sorted_nums[start] + sorted_nums[end]:
                end -= 1
            else:
                return [nums.index(sorted_nums[start]), nums.index(sorted_nums[end])]  
            
            
    def twoSumwithHashMap(self, nums, target):
        hashmap = {}
        for index, each in enumerate(nums):
            if each not in hashmap:
                hashmap[each] = index
        
        for index, each in enumerate(nums):  
            if target-each in hashmap.keys():
                if index == hashmap[target-each]:
                    pass
                else:
                    return sorted([index, hashmap[target-each]])
        
    def twoSum(self, nums, target):
        
    #    This can be solved three different ways:
    #    1. Brute force approach = O(n^2)
    #    2. With Sorting and two pointers - start and end = O(NLogN)
    #    3. Using HashMaps - Time: O(N) Space: O(N)
        
        result_sorting = self.twoSumwithSorting(nums, target)
        result_hashmap = self.twoSumwithHashMap(nums, target)

        return [result_hashmap, result_sorting]
    
s = Solution()
print(s.twoSum([5, 7, 3, 3, 8], 6))