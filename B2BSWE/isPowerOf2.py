
import math
class Solution:
    def powerOfTwo_1(self, input):
        '''
        :type input: int
        :rtype: bool
        '''
        if input <= 0:
            return False
            
        x = math.log2(input)
        if x%2==0:
            return True
        else:
            return False
        
    def powerOfTwo(self, input):
        
        if input <= 0:
            return False
        
        return (input & (input -1)) == 0
    
s = Solution()
print(s.powerOfTwo(8))