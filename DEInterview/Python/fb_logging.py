# Question: https://leetcode.com/discuss/interview-question/896522/Facebook-Data-Engineering-Interview-Onsite
def process_input(arr):
    
    result = {}
    for each_row in arr: 
        #print("Processing: ", each_row)
        machine, process, activity, time = each_row 
        if (machine, process) in result and activity == 'start':
            d = result[(machine, process)] 
            if 'start' in d:
                d['start'].append(float(time))
            else:
                d['start'] = [float(time)]
            result[(machine, process)] = d
        elif (machine, process) not in result and activity == 'start':
            d = {}
            d['start'] = [float(time)]
            result[(machine, process)] = d
        elif (machine, process) in result and activity == 'end':
            d = result[(machine, process)] 
            if 'end' in d:
                d['end'].append(float(time))
            else:
                d['end'] = [float(time)]
            result[(machine, process)] = d
        elif (machine, process) not in result and activity == 'end':
            d = {}
            d['end'] = [float(time)]
            result[(machine, process)] = d 
              
    output = []
    header = ["machine", "process", "start", "end"]   
    output.append(header)
    for each in result:
        start, end = result[each]['start'], result[each]['end']
        for index, _ in enumerate(start):
            line = [each[0], each[1], start[index], end[index]]
            output.append(line)
    print(output)
    
input = [    
    ["m0","p0","start",0.712],
    ["m0","p1","start",0.841],
    ["m0","p2","start",1.523],
    ["m0","p2","end",1.966],
    ["m0","p1","start",2.856],
    ["m0","p2","start",3.347],
    ["m0","p2","end",3.567],
    ["m0","p1","start",3.800],
    ["m0","p2","start",4.618],
    ["m0","p2","end",5.497],
    ["m0","p1","start",5.961],
    ["m0","p2","start",6.324],
    ["m0","p2","end",6.673],
    ["m0","p1","end",7.233],
    ["m0","p1","end",7.533],
    ["m0","p1","end",7.933],
    ["m0","p1","end",8.333],
    ["m0","p0","end",9.933]
]
process_input(input)

Sample output
=============
[
    ['machine', 'process', 'start', 'end'], 
    ['m0', 'p0', 0.712, 9.933], 
    ['m0', 'p1', 0.841, 7.233], 
    ['m0', 'p1', 2.856, 7.533], 
    ['m0', 'p1', 3.8, 7.933], 
    ['m0', 'p1', 5.961, 8.333], 
    ['m0', 'p2', 1.523, 1.966], 
    ['m0', 'p2', 3.347, 3.567], 
    ['m0', 'p2', 4.618, 5.497], 
    ['m0', 'p2', 6.324, 6.673]
]