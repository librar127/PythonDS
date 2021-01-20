def getMismatchedWords(str1, str2):
    result = []
    
    for each in str1.split():
        if each not in str2.split():
            result.append(each)
    
    for each in str2.split():
        if each not in str1.split():
            result.append(each)
    
    return result

string1 = "Firstly this is the first string"
string2 = "Next is the second string"
print(getMismatchedWords(string1, string2))