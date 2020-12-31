import math

class Solution:
    def powerOfFour(self, input):
        '''
        :type input: int
        :rtype: bool
        '''
        
        if input <= 0:
            return False
            
        k = math.log2(input)
        if k%2 == 0:
            return True
        else:
            return False
    
s = Solution()
print(s.powerOfFour(8))