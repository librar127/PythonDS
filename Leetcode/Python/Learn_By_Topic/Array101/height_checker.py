class Solution:
    def heightChecker(self, heights):
        s_array = sorted(heights)
        
        count = 0
        for index, each in enumerate(heights):
            if each != s_array[index]:
                count += 1
        return count
    
s = Solution()
nums = [2,1,2,1,1,2,2,1]
print(s.heightChecker(nums))