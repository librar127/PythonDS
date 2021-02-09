class Test1:
    def set_up(self):
        self.word_list = ['cat', 'bat', 'rat', 'drat', 'dart', 'drab']

    def is_match(self, query):
    
        for word in self.word_list:
            #if bool(re.fullmatch(rf'{query}', word)):
            if len(query) == len(word):
                for index, each in enumerate(query):   
                    if each == '.' or each == word[index]:
                        if index == len(word)-1:
                            return True
                        continue
                    else:
                        break  
            else:
                continue
            
        return False


queries = ['cat', 'c.t', '.at', '..t', 'd..t', '.....', 'h.t', 'c.']
test1 = Test1()
test1.set_up()
for q in queries:
    print(f'{q} -> {test1.is_match(q)}')