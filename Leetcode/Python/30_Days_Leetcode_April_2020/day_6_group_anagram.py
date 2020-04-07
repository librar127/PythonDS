def groupAnagrams(strs):    
    
    hashmaps = {}
    for word in strs:
        sorted_word = '_'.join(sorted(word))

        if sorted_word in hashmaps:
            hashmaps.get(sorted_word).append(word)
        else:
            hashmaps[sorted_word] = [word]

    return list(hashmaps.values())

input = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(input))

input = ["eat"]
print(groupAnagrams(input))

input = ["boo", "bob"]
print(groupAnagrams(input))

input = ["hos","boo","nay","deb","wow","bop","bob","brr","hey","rye","eve","elf","pup","bum","iva","lyx","yap","ugh","hem","rod","aha","nam","gap","yea","doc","pen","job","dis","max","oho","jed","lye","ram","pup","qua","ugh","mir","nap","deb","hog","let","gym","bye","lon","aft","eel","sol","jab"]
print(groupAnagrams(input))