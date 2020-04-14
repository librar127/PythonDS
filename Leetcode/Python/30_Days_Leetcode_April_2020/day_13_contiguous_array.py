# Approach 1: Bruteforce Approach - O(N^2)
def findMaxLength_BF(nums):
    
    max_length = 0
    for i, _ in enumerate(nums):
        count = 0
        for j in range(i, len(nums)):
            if nums[j] == 0:
                count -= 1
            else:
                count += 1
            
            if count == 0:
                if j -i +1 > max_length:
                    max_length = j-i+1
                    
    return max_length


# Approach 2: Bruteforce Approach
def findMaxLength(nums):
    
    max_length = 0
    count = 0
    hashmap = {0:0}
    
    for index, each in enumerate(nums):
        
        if each == 0:
            count -= 1
        else:
            count += 1
            
        if count in hashmap.keys():
            max_length = max(max_length, index+1-hashmap[count])
        else:
            hashmap[count] = index + 1
            
    return max_length

nums = [0, 1, 1, 0, 1, 1, 1, 0]
print(findMaxLength_BF(nums))

nums = [0, 0, 1, 0, 0, 0, 1, 1]
print(findMaxLength_BF(nums))

nums =  [1, 1, 1, 0, 1, 1]
print(findMaxLength_BF(nums))


print('================')


nums = [0, 1, 1, 0, 1, 1, 1, 0]
print(findMaxLength(nums))

nums = [0, 0, 1, 0, 0, 0, 1, 1]
print(findMaxLength(nums))

nums =  [1, 1, 1, 0, 1, 1]
print(findMaxLength(nums))