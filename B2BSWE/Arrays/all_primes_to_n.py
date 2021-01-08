
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
            prime = True           
            for i in range(2, each-1):
                if each%i == 0:
                    prime = False
                    break
            if prime:
                result.append(each)
            
        return result
        
s = Solution()
print(s.enumeratePrimes(8))