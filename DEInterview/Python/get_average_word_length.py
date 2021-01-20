def getAverageLength(string):
    
    return round(sum([len(each.strip()) for each in string.split()])/len(string.split()), 2)

string = "Firstlydddd this is the firstcccc string  "
print(getAverageLength(string))
    
    