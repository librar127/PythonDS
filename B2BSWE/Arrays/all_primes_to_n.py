
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
        for each in range(4, n, 1): # T(n) = O(n)
            prime = True           
            for i in range(2, each-1): # T(n) = O(n)
                if each%i == 0:
                    prime = False
                    break
            if prime:
                result.append(each)
            
        return result
    # T(n) = O(n^2)
    # S(n) = O(n)
    
    def enumeratePrimes_1(self, n): 
        '''
        :type n: int
        :rtype: list of int
        '''
        if n in [0, 1]:
            return []
        if n in [2, 3]:
            return [n]
        
        result = [2, 3]
        for each in range(4, n, 1): # T(n) = O(n)
            prime = True  
            i = 2        
            while i*i <= each: # Improvement 1 - Any non- prime always divisible by: a <= sqrt(n) <= b. T(n) = O(n^0.5)
                if each%i == 0:
                    prime = False
                    break
                i += 1
            if prime:
                result.append(each)
            
        return result
    # T(n) = O(n^1.5)
    # S(n) = O(n)
    
    def enumeratePrimes_2(self, n): 
        '''
        :type n: int
        :rtype: list of int
        '''
        
        isPrime = [True for _ in range(n)] # S(n) = O(n)
        isPrime[0] = False
        isPrime[1] = False
        
        for each in range(2, n): # T(n) = O(n)
            index = each + each
            while index <  n: # Improvement 2 - forward lookup. For any prime number, go into the numbers till n-1 and mark non-Prime if prime divides any number     
                isPrime[index] = False # This look going through just only prime numbers hence T(n) = O(log(log(n)))
                index += each
        
        result = [] 
        for index, each in enumerate(isPrime):
            if each:
                result.append(index) 
                  
        return result
    # T(n) = O(log(log(n)))
    # S(n) = O(n)
        
s = Solution()
print(s.enumeratePrimes_2(23))