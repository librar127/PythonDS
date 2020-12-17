class Solution:
    def reverseBits(self, input):
        '''
        :type input: int
        :rtype: int
        : Desc: Given an input integer input, return the integer value of input's bits reversed. \
        : You will only be reversing the "significant portion" of the binary representation (ignoring leading zeros).
        '''
        
        if input == 1:
            return 1
            
        output = 0
        while input:
            output <<= 1
            bit_x = input & 1
            output |= bit_x
            input >>= 1
            
        return output
    
s = Solution()
print(s.reverseBits(11))