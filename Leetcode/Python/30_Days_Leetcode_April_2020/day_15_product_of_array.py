## Approach 1 - O(N) with Division
def productExceptSelf(nums):

    product = 1
    isZero = False
    zero_count = 0
    for each in nums:
        if each == 0:
            isZero = True
            zero_count += 1
            continue
            
        product *= each
        
    if zero_count >1:
        for i, each in enumerate(nums):
           nums[i] = 0
           
        return nums

    index = 0
    while index < len(nums):
        each = nums[index]
        if each == 0:
            if isZero:
                nums[index] = product
            else:
                nums[index] = 0
        else:
            if isZero:
                nums[index] = 0
            else:
                nums[index] = product//each
        index += 1
        
    return nums
 
## Approach 2 - Using Log Properties - Devision is replaced by the Log     
import math  
def productExceptSelf_Log(nums):
    sum_log = 0
    isZero = False
    zero_count = 0
    for each in nums:
        if each == 0:
            isZero = True
            zero_count += 1
            continue
            
        sum_log += math.log10(each)
    
    answer = [0]*len(nums)  # This does not count as extra space as we can have answer array
    if zero_count >1:        
        return answer

    index = 0
    
    for index, each in enumerate(nums):
        if each == 0:
            if isZero:
                answer[index] = int(round(math.pow(10, sum_log)))
            else:
                answer[index] = 0
        else:
            if isZero:
                answer[index] = 0
            else:
                answer[index] = int(round(math.pow(10, (sum_log-math.log10(each)))))
                pass  
    return answer

## Approach -3 : 2 Array Approach. Time: O(N), Space: O(N)
def productExceptSelf_2Array(nums):
    n = len(nums)
    left = [1]*n
    right = [1]*n
    
    for index in range(1, len(nums)):
        left[index] = nums[index-1] * left[index-1]
    
    index = n-2
    while index >= 0:
        right[index] = nums[index+1] * right[index+1]
        index -= 1
        
    for index, each in enumerate(left):
        left[index] = each * right[index]
        
    return left
        
 ## Approach -3 : Time: O(N), Space: O(1) - Answer space is not counted
def productExceptSelf_1Array(nums):
    n = len(nums)
    answer = [1]*n
    
    for index in range(1, len(nums)):
        answer[index] = nums[index-1] * answer[index-1]
    
    index = n-1
    right = 1
    while index >= 0:
        answer[index] = right * answer[index]
        right *= nums[index]
        index -= 1
        
    return answer   

# Approach 1    
nums = [1,2,3,4]              
print(productExceptSelf(nums))     

nums = [1,2,0,4]              
print(productExceptSelf(nums))     

nums = [0,2,0,4]              
print(productExceptSelf(nums)) 

print()   

# Approach 2
nums = [1,2,3,4]              
print(productExceptSelf_Log(nums))     

nums = [1,2,0,4]              
print(productExceptSelf_Log(nums))     

nums = [0,2,0,4]              
print(productExceptSelf_Log(nums)) 

print()   

# Approach 3
nums = [1,2,3,4]              
print(productExceptSelf_2Array(nums))     

nums = [1,2,0,4]              
print(productExceptSelf_2Array(nums))     

nums = [0,2,0,4]              
print(productExceptSelf_2Array(nums)) 

print()  

# Approach 4
nums = [1,2,3,4]              
print(productExceptSelf_1Array(nums))     

nums = [1,2,0,4]              
print(productExceptSelf_1Array(nums))     

nums = [0,2,0,4]              
print(productExceptSelf_1Array(nums)) 

print() 