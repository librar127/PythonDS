class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        
        index = 0
        while index < len(arr):
            if arr[index] == 0:
                arr.pop()
                arr.insert(index, 0)
                index += 2
            else:
                index += 1
                
        return arr
    
s = Solution()
nums = [1,0,2,3,0,4,5,0]
print(s.duplicateZeros(nums))   
                