# Tn: O(NKLogK) Sn: O(NK)
class Solution:
    def groupAnagrams(self, strs):    
    
        hashmaps = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word in hashmaps:
                hashmaps.get(sorted_word).append(word)
            else:
                hashmaps[sorted_word] = [word]

        return list(hashmaps.values())
    
s = Solution()
input = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(s.groupAnagrams(input))