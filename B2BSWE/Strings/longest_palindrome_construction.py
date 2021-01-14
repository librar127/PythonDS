
class Solution:
    def longestPalindrome(self, s):
        '''
        :type s: str
        :rtype: int
        '''
        if not s:
            return 0
        
        hashmap = {}
        for each in s:
            if each in hashmap:
                hashmap[each] += 1
            else:
                hashmap[each] = 1
        
        print(hashmap)   
           
        longest_odd = 1
        longest_even = 0
        for each in hashmap:
            if hashmap[each] % 2 == 0:
                longest_even += hashmap[each]
            if hashmap[each] % 2 != 0 and hashmap[each] > longest_odd:
                longest_odd = hashmap[each] 
                               
        return (longest_even + longest_odd)
            
        
s = Solution()
input = "xyz"
print(s.longestPalindrome(input))