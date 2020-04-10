import math

def isPrime(num):
    
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    
    return True

def countPrime_TImeExceeded_LC_2(num):
    if num <= 1:
        return 0
    
    count = 0 
    index = 2
    while index < num:
        if isPrime(index):
            count += 1
        index += 1
        
    return count

def countPrime_TimeExceeded_LC_1(n):
    
    if n <= 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    if n == 5:
        return 3
    if n== 7:
        return 4
    
    count = 4         
    for i in range(10, n):
        divisible_flag = False
        root_i = math.floor(math.sqrt(i))
        for j in range(2, root_i+1):
            if i % j == 0:
                divisible_flag = True
                break
            
        if not divisible_flag:
            count += 1
        
    return count

def countPrime(n):
    
    result = [] 
    result.append(False)
    result.append(False)
    for _ in range(2, n):
        result.append(True) 
    
    each_num = 2
    while each_num*each_num < n:
        
        ## This condition seems option as it is bit imporvement 
        if not result[each_num]:
            each_num += 1
            continue
        
        index = each_num * each_num
        while index < n:
            result[index] = False
            index += each_num
        
        each_num +=1
        
    count = 0
    for each in result:
        if each:
            count += 1
    
    return count

    
        
print(countPrime(102))