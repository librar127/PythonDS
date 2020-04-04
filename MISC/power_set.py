class Powerset():
    def generate_power_set(self, string):
        
        result = ['']
        for index, each in enumerate(string):
            for j in range(2**index):
                result.append(result[j]+each) 
                
        return result
    
s = Powerset()
print(s.generate_power_set('ABCD'))