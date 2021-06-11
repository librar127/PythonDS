
class Solution:
    def runningSum(self, nums):
        result = []
        for index, each in enumerate(nums):
            if index > 0:
                result.append(result[index-1] + each)
            else:
                result.append(each)
            
        return result