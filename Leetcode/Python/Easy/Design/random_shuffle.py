from random import randint
class Solution:
    
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.array
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        new_array = self.original
        arr_len = len(new_array)
        for index, _ in enumerate(new_array):      
            rand_index = randint(0, arr_len-1)
            new_array[index], new_array[rand_index] = new_array[rand_index], new_array[index]
            
        return new_array

# Your Solution object will be instantiated and called as such:
nums = [1,2,3,4,5,6,7,8]
obj = Solution(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()
param_3 = obj.reset()

print(param_1, param_2)