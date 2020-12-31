
class Solution:
    def timeDifference_1(self, times):
        '''
        :type times: list of str
        :rtype: int
        :O(NLogN) solution
        '''
        min_diff = 999999
        s_times = sorted(times)
        
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
        
    def timeDifference(self, times):
        '''
        :type times: list of str
        :rtype: int
        :O(N) solution
        '''
        min_diff = 9999
        min_list = [0]*1440
        
        for each_time in times:
            hh,mm = each_time.split(":")
            time_2_index = int(hh)*60+int(mm)
            
            if min_list[time_2_index]:
                return 0
            
            min_list[time_2_index] = time_2_index
            
        start_flag = False
        last_index = 0
        for each in min_list:
            if each > 0:
                last_index = each
                
        for index,each in enumerate(min_list):
            if each > 0:
                
                if start_flag == False:
                    diff = each+1440 - min_list[last_index]
                else:
                    diff = each - min_list[last_index]
                    
                start_flag = True   
                if diff < min_diff:
                    min_diff = diff
                    
                last_index = index
        
        return min_diff