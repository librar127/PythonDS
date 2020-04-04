def string_to_integer(str):
    
    valid_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    neg_sign = False
    pos_sign = False
    valid_num = False
    
    #start_num =  False
    num = 0
    for each_char in str:
        if each_char == '+' and neg_sign is False and pos_sign is False and valid_num is False:
            pos_sign = True
            continue
        
        elif each_char == '-' and neg_sign is False and pos_sign is False and valid_num is False:
            neg_sign = True
            continue
            
        elif each_char in valid_nums:
            num = num*10 + int(each_char)
            valid_num = True
            
        else:
            if each_char !=' ':
                break
            elif each_char == ' ' and valid_num is True:
                break
            elif each_char == ' ' and (pos_sign is True or neg_sign is True):
                break
            else:
                pass
    
    if num > 2**31-1 and neg_sign is True:
        num = 2**31
    elif num > 2**31-1 and neg_sign is False:
        num = 2**31-1
            
    if neg_sign is True:
        num = (num) * -1
              
    return num

s = "+42"
s = "    -42"
s = "4193 with words"
s = "words and 987"
s = "-91283472332"
s = "    42 77"
s = "    +42"
s = "+42"
s = "-4193 with words"
s = "+4193 with words"
s = "   -42"
s = "    -42"
s = "-91283472332"
s = "  +1"
s = "  + 1"
s = "41 93 with words"
s = "2147483648"
s = "0-1"
s = "0 123"
print(string_to_integer(s))