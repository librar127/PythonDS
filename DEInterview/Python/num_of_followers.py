def getFollowersCount(arr):
    result = []
    hashmap = {}
    
    for each in arr:
        if each[0] in hashmap.keys():
            current = hashmap[each[0]]
            current.add(each[1])
            hashmap[each[0]] =  current
        else:
            hashmap[each[0]] = set(each[1])
            
    print(hashmap)
    for each in hashmap:
        result.append((each, len(hashmap[each])))
    
    return result


arr = [('A', 'C'), ('A', 'B'), ('B', 'C'), ('C', 'B'), ('B', 'D')]
print(getFollowersCount(arr))