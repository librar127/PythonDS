def firstNotRepeatingCharacter(s):
    hashmap = {}
    for each in s:
        if each in hashmap:
            hashmap[each] += 1
        else:
            hashmap[each] = 1
    
    for each in s:
        if hashmap[each] == 1:
            return each
    
    return '_'