
class Solution:
    
    def enumeratePrimes(self, n):
        '''
        :type n: int
        :rtype: list of int
        '''
        if n in [0, 1]:
            return []
        if n in [2, 3]:
            return [n]
        
        result = [2, 3]
        for each in range(4, n, 1):
            test_list = range(2, each-1)            
            out_list = [True if each%i == 0 else False for i in test_list]
            if any(out_list):
                continue
            else:
                result.append(each)
            
        return result
        
s = Solution()
print(s.enumeratePrimes(1))