def numberOfTimes1(substring, string):
    return string.count(substring)


def numberOfTimes(substring, string):
    start = 0
    result = 0
    for index in range(len(substring), len(string)):
        if substring == string[start:index]:
            result += 1
        start += 1
    return result

string = "mississippi"
substring = "ip"
print(numberOfTimes(substring, string))