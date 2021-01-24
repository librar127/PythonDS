def getCorrectWords(arr, exp):
    
    result = []
    for each_word in arr:
        if len(each_word) != len(exp):
            result.append(False)
            continue

        for index, each_char in enumerate(exp):
            if each_char == '.':
                continue
            elif each_word[index] == each_char:
                if index == len(exp)-1:
                    result.append(True)
                else:
                    continue
            else:
                result.append(False)
                break
                
    return result

arr = ['cat', 'bat', 'rat', 'drat', 'dart', 'drab']
exp = 'c.t'
print(getCorrectWords(arr, exp))
    
