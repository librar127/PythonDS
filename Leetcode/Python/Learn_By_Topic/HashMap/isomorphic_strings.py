class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        hashmap = {}
        hashset = set()
        
        for index, each in enumerate(s):
            if each in hashmap:
                if t[index] != hashmap[each]:
                    return False  
            elif t[index] in hashset:
                return False
            
            else:
                hashmap[each] = t[index]   
                hashset.add(t[index])
        
        return True