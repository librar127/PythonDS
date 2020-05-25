class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for each in s:
            if each in hashmap:
                hashmap[each] += 1
            else:
                hashmap[each] = 1
                
        for index, each in enumerate(s):
            if hashmap[each] == 1:
                return index
            
        return -1