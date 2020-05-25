class Solution:
    def isHappy(self, n):
        hashset = set()
        
        while True:
            
            squares = 0
            while n > 0:
                squares += (n % 10)**2
                n = n // 10
            
            if squares == 1:
                return True
            n = squares
            if squares in hashset:
                return False
            else:
                hashset.add(squares)