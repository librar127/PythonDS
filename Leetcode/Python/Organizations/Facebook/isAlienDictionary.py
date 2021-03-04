class Solution:
    def isAlienSorted(self, words, order):
        
        order_dict = {each:index for index, each in enumerate(order)}            
        
        for i in range(len(words)-1):
            word_1 = words[i]
            word_2 = words[i+1]
            
            for index in range(min(len(word_1), len(word_2))):
                if word_1[index] != word_2[index]:                
                    if order_dict[word_1[index]] > order_dict[word_2[index]]:
                        return False
                    break
            else:       
                if len(word_1) > len(word_2):
                    return False
                
        return True
    
solution = Solution()
words = ["world","row"]
order = "worldabcefghijkmnpqstuvxyz"
print(solution.isAlienSorted(words, order))