class Solution:
    def twoSum(self, nums, target):
        nums_with_index = [[i, nums[i]] for i in range(len(nums))]
        sorted_list = sorted(nums_with_index, key=lambda x:x[1])
        
        i = 0
        j = len(sorted_list)-1
        while i<j:            
            sum_i_j = sorted_list[i][1] + sorted_list[j][1]
            
            if sum_i_j > target:
                j -= 1
            elif sum_i_j < target:
                i += 1
            else:
                return [sorted_list[i][0], sorted_list[j][0]]

solution = Solution()
num_list = [3, 2, 4]
output = solution.twoSum(num_list, 6)
<<<<<<< HEAD
print(output)
=======
print(output)
>>>>>>> e6b271f08413af7110d4672987a29b3d5bf13ad0
