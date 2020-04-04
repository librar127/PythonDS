def find_first_unique_character(string):
    
    if len(string) == 0:
        return -1
    if len(string) == 1:
        return 0
    
    hashmap = {}
    for each in string:
        if each in hashmap:
            hashmap[each] += 1
        else:
            hashmap[each] = 1
            
    for index, each in enumerate(string):
        if hashmap[each] == 1:
            return index
            
    return -1

print(find_first_unique_character('leetcode'))
print(find_first_unique_character('loveleetcode'))
print(find_first_unique_character(""))