def sortByFreq(arr):
    hashmap=dict()
    result = []
    for item in arr:
        if item in hashmap:
            hashmap[item]+=1
        else:
            hashmap[item]=1                
    sorted_hashmap = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
    
    final_result = []
    keys = list(sorted_hashmap.keys())        
    result = [keys[0]]
    for index in range(1, len(keys)):            
        if sorted_hashmap[keys[index]] == sorted_hashmap[keys[index-1]]:
            result.append(keys[index])
        else:
            if len(result) > 1:
                result_s = sorted(result)
                for each in result_s:
                    final_result.extend([each]*sorted_hashmap[each])
            else:
                final_result.extend([keys[index-1]]*sorted_hashmap[keys[index-1]])
                
            result = [keys[index]]
    
    if len(result) > 0:            
        result_s = sorted(result)
        for each in result_s:
            final_result.extend([each]*sorted_hashmap[each])
        
    return final_result

arr = [5,5,4,6,4, 6]  
arr = [6, 6, 2, 3, 1, 4, 1, 5, 6, 2, 8, 7, 4, 2, 1, 3, 4, 5, 9, 6]  
print(sortByFreq(arr))