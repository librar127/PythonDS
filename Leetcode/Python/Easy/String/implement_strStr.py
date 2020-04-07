def strStr(haystack, needle):
    
    if len(needle) <= 0:
        return 0
    
    if len(needle) > len(haystack):
        return -1
    
    index = 0
    while index <= len(haystack) - len(needle):
        if haystack[index:index+len(needle)] == needle:
            return index
        index += 1
        
    return -1


haystack, needle = "hello", "ll"
print(strStr(haystack, needle))

haystack = "aaaaa"
needle = "bba"
print(strStr(haystack, needle))

haystack = "bba"
needle = ""
print(strStr(haystack, needle))

haystack = "a"
needle = "a"
print(strStr(haystack, needle))

haystack = "bba9999dfgghhdft"
needle = "dft"
print(strStr(haystack, needle))

haystack = "dftdd"
needle = "dftdd"
print(strStr(haystack, needle))

haystack = "aaa"
needle = "aaaa"
print(strStr(haystack, needle))

haystack = "mississippi"
needle = "issip"
print(strStr(haystack, needle))
