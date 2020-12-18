
class Solution:
    def addStrings(self, s1, s2):
        '''
        :type s1: str
        :type s2: str
        :rtype: str
        '''
        carry = 0
        result = ''
        n1 = len(s1)
        n2 = len(s2)
        
        while (n1 > 0) or (n2 > 0):        
            
            d1 = int(s1[n1-1]) if n1 > 0 else 0            
            d2 = int(s2[n2-1]) if n2 > 0 else 0
            
            sum = d1 + d2 + carry
            carry = sum // 10
            rem = sum % 10
            result = str(rem)+result           
            
            n1 -= 1
            n2 -= 1 
            
        if carry > 0:               
            return str(carry)+result
        else:
            return result
            
s = Solution()
print(s.addStrings('101', '1'))
                