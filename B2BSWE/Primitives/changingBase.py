
class Solution:
    
    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        return False
        
    def convert2SingleDigit(self, num):
        
        hashmap = {
            10:'A',
            11:'B',
            12:'C',
            13:'D',
            14:'E',
            15:'F',
            16:'G',
            17:'H',
            18:'I',
            19:'J',
            20:'K',
            21:'L',
            22:'M',
            23:'N',
            24:'O',
            25:'P',
            26:'Q',
            27:'R',
            28:'S',
            29:'T',
            30:'U',
            31:'V',
            32:'W',
            33:'X',
            34:'Y',
            35:'X'
        }
        
        return hashmap[num]
    
    def convert2Base10(self, num, base):
        
        sum = 0
        #my_dict2 = dict((y,x) for x,y in my_dict.iteritems())
        for index,each in enumerate(num[::-1]):
            if not self.is_number(each):
                digit = ord(each) - ord('A') + 10
            else:
                digit = int(each)
            sum += digit*(base**index)
        return sum
     
    def convert2GivenBase (self, num, base):
        result = ''
        while num>0:
            rem = num%base
            num = num//base
            if rem > 9:
                result += self.convert2SingleDigit(rem)
            else:
                result += str(rem)
                
        return result[::-1]
        
    def changeBase(self, numAsString, b1, b2):
        '''
        :type numAsString: str
        :type b1: int
        :type b2: int
        :rtype: str
        '''
        if b1 == 10:
            num = int(numAsString)
        else:
            num = self.convert2Base10(numAsString, b1)
        
        
        if b2 == 10:
            output = str(num)
        else:
            output = self.convert2GivenBase(num, b2)
        
        print(num, output)
        
        return output