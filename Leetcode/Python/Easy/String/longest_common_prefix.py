def longestCommonPrefix(strs):
    result = ""
    
    if len(strs) <= 0:
        return ""
    
    for char_index, each in enumerate(strs[0]):
        for index in range(1, len(strs)):
            if not len(strs[index]) > char_index or strs[index][char_index] != each:
                return result
        result += each                
            
    return result

'''
input = ["flower","flow","flight"]
print(longestCommonPrefix(input))

input = ["dog","racecar","car"]
print(longestCommonPrefix(input))
'''

input = ["aa","a"]
print(longestCommonPrefix(input))
