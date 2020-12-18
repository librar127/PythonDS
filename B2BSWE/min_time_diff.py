
class Solution:
    def timeDifference(self, times):
        '''
        :type times: list of str
        :rtype: int
        '''
        min_diff = 999999
        s_times = sorted(times)
        print(s_times)
        for index in range(len(s_times)-1):
            next_a, next_b = s_times[index+1].split(":")
            curr_a, curr_b = s_times[index].split(":")
            
            diff = (int((next_a))*60+int(next_b)) - (int(curr_a)*60+int(curr_b))            
            if diff < min_diff:
                min_diff = diff
                
        
        curr_a, curr_b = s_times[len(s_times)-1].split(":")
        next_a, next_b = s_times[0].split(":")  
        
        diff = ((int(next_a)+24)*60+int(next_b)) - (int(curr_a)*60+int(curr_b))
        if diff < min_diff:
            min_diff = diff     
                
        return min_diff
        
            
s = Solution()
print(s.timeDifference(["00:03","23:59","12:03"]))