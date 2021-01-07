
class Solution:
    def threeSum(self, A):
        '''
        :problem: Given an array of n integers, return all unique triplets [a,b,c] in the array such that a + b + c = 0
        :type A: list of int
        :rtype: list of list of int
        '''
        
        hashmap = {}
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                key = A[i]+A[j]
                if key in hashmap:
                    result = hashmap[key]
                    result.append([A[i], A[j]])
                    hashmap[key] = result
                else:
                    hashmap[key] = [[A[i], A[j]]]
        
        result = set()
        for each in A:
            if -1*each in hashmap:
                output_1 = hashmap[-1*each]
                for each_pair in output_1:
                    if each in each_pair:
                        continue
                    each_pair.append(each)
                    result.add(tuple(sorted(each_pair)))
                    
        return [list(each) for each in result]
        
s = Solution()
arr = [-3, -1, 1, 0, 2, 10, -2, 8]
print(s.threeSum(arr))