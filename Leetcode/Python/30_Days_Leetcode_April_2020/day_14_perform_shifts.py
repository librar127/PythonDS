def doShift(string, direction, shift_count):
    charlist = [each for each in string]
    n = len(string)
    if shift_count > n:
        shift_count = shift_count % n
    if direction == 0:
        print('Left')
        return ''.join(charlist[shift_count:]+charlist[:shift_count])
    else:        
        print('Right')
        return ''.join(charlist[n-shift_count:]+charlist[:n-shift_count])


def stringShift(s, shift):
    left_shift = 0
    right_shift = 0
    final_direction = 0
    final_shift = 0
    for each in shift:
        direction, shift_count = each[0], each[1]

        if direction == 0:
            left_shift += shift_count
        else:
            right_shift += shift_count

        if left_shift > right_shift:
            final_direction = 0
            final_shift = left_shift - right_shift
        else:
            final_direction = 1
            final_shift =  right_shift - left_shift

    return doShift(s, final_direction, final_shift)
    

print(stringShift('abc', [[0,4],[1,2]]), '\n')
print(stringShift('abcdefg', [[1,1],[1,1],[0,2],[1,3]]), '\n')
print(stringShift('mecsk', [[1,4],[0,5],[0,4],[1,1],[1,5]]), '\n')

            
        