
class Solution:
    def findAndReplacePattern(self, words, pattern):
        '''
        :type words: list of str
        :type pattern: str
        :rtype: list of str
        '''
        
        result = []
        for each_word in words:
            if len(each_word) != len(pattern):
                continue
            
            result_word = ''
            dict1 = {}
            dict2 = {}
            for index, each_char in enumerate(each_word):
                matching_char = ''
                if each_char in dict1:
                    
                    matching_char = dict1[each_char]                    
                    if matching_char == pattern[index]:                        
                        result_word += each_char  
                        continue
                    else:
                        result_word = ''
                        break  
                    
                else:
                    if pattern[index] in dict2:
                        result_word = ''
                        break
                            
                    dict1[each_char] = pattern[index]
                    dict2[pattern[index]] = each_char
                    result_word += each_char
            
            if result_word:                        
                result.append(result_word)    
                
        return result
        
s = Solution()
words = ["ad", "bb"]
pattern = "cc"
print(s.findAndReplacePattern(words, pattern))