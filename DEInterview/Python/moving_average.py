import datetime as dt

def moving_average(input_dict, window):
    moving_average_result = {}
    days = sorted(input_dict.keys())
    running_sum = 0
    
    for each in days[:window]:
        running_sum += input_dict[each]
        
    moving_average_result[days[0]] = round(running_sum/window, 2)
    print(running_sum, days[0]) 
           
    for index in range(1, len(days)-window+1):
        
        running_sum -= input_dict[days[index-1]]
        running_sum += input_dict[days[index + window - 1]]
        
        moving_average_result[days[index]] = round(running_sum/window, 2)
    
    
    return moving_average_result
    
    
example = {
        dt.datetime(2008, 1, 1) : 5, 
        dt.datetime(2008, 1, 2) : 6, 
        dt.datetime(2008, 1, 3) : 7, 
        dt.datetime(2008, 1, 4) : 9, 
        dt.datetime(2008, 1, 5) : 12,
        dt.datetime(2008, 1, 6) : 15, 
        dt.datetime(2008, 1, 7) : 20, 
        dt.datetime(2008, 1, 8) : 22, 
        dt.datetime(2008, 1, 9) : 25, 
        dt.datetime(2008, 1, 10) : 35
}

# print(example)
print(moving_average(example, 3))