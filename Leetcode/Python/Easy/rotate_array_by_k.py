class Solution:
    def reverse_nums(self, nums, start, end):
        while start < end:
            tmp = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp
            start += 1
            end -= 1
            
        return nums
            
    # Approach 1 - With Extra Memory
    def rotate_with_space(self, nums, k): 
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        list_k = []
        if n == 1:
            return nums
        
        if k>n:
            k = k-n
            
        for i in range(n-k, n):
            list_k.append(nums[i])
        
        del nums[n-k:]    
        list_k.extend(nums)
        return list_k
    
    # Approach 2: O(1) Memory
    def rotate(self, nums, k): 
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        if n == 1:
            return nums
        
        if k>n:
            k = k-n
        
        nums = self.reverse_nums(nums, 0, n-1)
        nums = self.reverse_nums(nums, k, n-1)
        nums = self.reverse_nums(nums, 0, k-1)
        return nums
        
          
s = Solution()
print(s.rotate_with_space([1,2,3], 4))
print(s.rotate([1,2,3], 4))