def valid_anagram(s, t):
    if len(s) != len(t):
        return False
        
    valid = True
    hashmap = {}
    for each in s:
        if each in hashmap:
            hashmap[each] += 1
        else:            
            hashmap[each] = 1
        
    for each in t:
        if each in hashmap and hashmap[each] > 0:
            hashmap[each] -= 1
        else:
            valid = False
        
    return valid

s1, s2 = "anagram", "nagaaram"
print(valid_anagram(s1, s2))

s = "rat"
t = "car"
print(valid_anagram(s, t))
    