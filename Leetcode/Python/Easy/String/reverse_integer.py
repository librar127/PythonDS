import sys
def reverse_integer(nums):
    
    negative = False
    if nums <0:
        negative = True
        nums = nums*-1
    
    new_num = 0
    while nums >0:
        new_num = new_num*10 + nums%10
        nums =  nums//10
    
    if new_num > 0x7FFFFFFF :
        return 0
     
    if negative:
        new_num *= -1
        
    return new_num

print(reverse_integer(1534236469))