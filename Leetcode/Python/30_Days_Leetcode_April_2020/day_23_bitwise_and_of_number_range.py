class Solution:
    def rangeBitwiseAnd(self, m, n) :
        count =  0
        while m != n:
            m = m >> 1
            n = n >> 1
            
            count += 1
            
        
        return (m << count)
        