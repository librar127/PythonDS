class Solution:
    def romanToInt(self, s):
        
        #### Method 1
        '''
        roman_2_int_dict_1 = {
            'I' : 1,
            'V' : 5,       
            'X' : 10,          
            'L' : 50,         
            'C' : 100,        
            'D' : 500,       
            'M' : 1000
        }
        
        roman_2_int_dict_2 = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        roman_num_list = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        
        
        output_sum = 0
        for each_item in roman_num_list:
            if each_item in s:
                output_sum += roman_2_int_dict_2[each_item]
                s = s.replace(each_item, "")
        
        for each_item in s:
            if each_item in roman_2_int_dict_1.keys():
                output_sum += roman_2_int_dict_1[each_item]
                
        return output_sum
        '''
        
        #### Method 2
        roman_2_int_dict = {
            'I' : 1,
            'V' : 5,       
            'X' : 10,          
            'L' : 50,         
            'C' : 100,        
            'D' : 500,       
            'M' : 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        
        output_sum = 0
        i = 0
        while i < len(s):
            print(i, s[i], '\n')
            if i+1 < len(s) and s[i]+s[i+1] in roman_2_int_dict.keys():
            
                output_sum += roman_2_int_dict[s[i]+s[i+1]]
                i += 2
            
            else:
                if s[i] in roman_2_int_dict.keys():
                    output_sum += roman_2_int_dict[s[i]]
                    i += 1
                    
        return output_sum

solution = Solution()
input = "MCMXCIV"
print(solution.romanToInt(input))