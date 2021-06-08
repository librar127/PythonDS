
def rotationalCipher(input, input_rotation_factor):
  # Write your code here
    print(input, input_rotation_factor)
    result = ""
    for each in input:
        if each.isalnum():
            try: 
                if type(int(each))==int:                  
                    rotation_factor = input_rotation_factor%10
                    print(each, rotation_factor)
                    if int(each)+rotation_factor >= 10:
                        current_char = ((int(each)+rotation_factor)%10)
                    else:
                        current_char = int(each)+rotation_factor
            except:                
                rotation_factor = input_rotation_factor%26
                if each.islower():
                    if (ord(each)-ord('a')+rotation_factor) >= 26:
                        current_char = chr(ord('a') + (ord(each)-ord('a')+rotation_factor)%26)
                    else:
                        current_char = chr(ord(each)+rotation_factor)
                else:
                    if (ord(each)-ord('A')+rotation_factor) >= 26:
                        current_char = chr(ord('A') + (ord(each)-ord('A')+rotation_factor)%26)
                    else:
                        current_char = chr(ord(each)+rotation_factor)  
            result += str(current_char)
        else:
            result += each        
        
    return result

input = "Zebra-493?"
rotationFactor = 3
output = "Cheud-726?"
result = rotationalCipher(input, rotationFactor)
print(result, output==result)

input = "abcdefghijklmNOPQRSTUVWXYZ0123456789"
rotationFactor = 39
output = "nopqrstuvwxyzABCDEFGHIJKLM9012345678"
result = rotationalCipher(input, rotationFactor)
print(result, output==result)

input_1 = "All-convoYs-9-be:Alert1."
rotation_factor_1 = 4
expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
result = rotationalCipher(input_1, rotation_factor_1)
print(result, expected_1==result)

input_2 = "abcdZXYzxy-999.@"
rotation_factor_2 = 200
expected_2 = "stuvRPQrpq-999.@"
result = rotationalCipher(input_2, rotation_factor_2)
print(result, expected_2==result)