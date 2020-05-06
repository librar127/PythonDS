class Solution:
    def climbStairs_tle(self, n):
        if n <= 1:
            return 1
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
        
    def climbStairs(self, n):
        steps = []
        
        steps.append(1)
        steps.append(2)
        index = 2
        while index < n:
            steps.insert(index, steps[index-1]+steps[index-2])
            index += 1
            
        return steps[n-1]