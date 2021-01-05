
import math
class Solution:
    def powerOfTwo(self, input):
        '''
        :type input: int
        :rtype: bool
        '''
        if input <= 0:
            return False
            
        x = math.log2(input)
        num = "{:.1f}".format(x)
        decimal_num = num.split('.')[1]
        return decimal_num == '0'
        
        
    def powerOfTwo_1(self, input):
        
        if input <= 0:
            return False
        
        return (input & (input -1)) == 0
    
s = Solution()
print(s.powerOfTwo(6))