class Solution:
    
    
    def swap_zero_and_nonzero(self, nums, start, end):
        tmp = nums[start]
        nums[start] = nums[end]
        nums[end] = tmp
        
        return nums
    
    def moveZeroes(self, nums):
        
        if len(nums) <= 1:
            return nums
        
        # Reduce num of operartions
        all_zeros = True
        for each in nums:
            if each > 0:
                all_zeros = False
        
        if all_zeros is True:
            return nums
        
        zero_pointer = -1
        
        for index, each in enumerate(nums):
            if each == 0: 
                if zero_pointer == -1:
                    zero_pointer = index
            else:
                if zero_pointer >-1:
                    nums = self.swap_zero_and_nonzero(nums, zero_pointer, index)
                    zero_pointer += 1
                    while zero_pointer < index and nums[zero_pointer] > 0:
                        zero_pointer += 1
        return nums
    
    def moveZeroes_with_space(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """        
        
        if len(nums) <= 1:
            return nums
        
        # Reduce num of operartions
        all_zeros = True
        for each in nums:
            if each > 0:
                all_zeros = False
        
        if all_zeros is True:
            return nums
        
        n = len(nums)
        for each in nums:
            if each ==0:
                nums.remove(each)
                nums.insert(n-1, each)
                
        return nums        
                
    def move_zeros_greatsolution(self, nums):
            # I got this from discussion forum
            
            zero_pointer = 0
            for index, each in enumerate(nums):
                if each != 0:
                    # Swap the numbers
                    nums[zero_pointer], nums[index] = nums[index], nums[zero_pointer]
                    zero_pointer += 1
                    
            return nums
    
s = Solution()
expected_list = [-959151711,623836953,209446690,-1950418142,1339915067,-733626417,481171539,-2125997010,-1225423476,1462109565,147434687,-1800073781,-1431212205,-450443973,50097298,753533734,-747189404,-2070885638,-1484353894,-340296594,-2133744570,619639811,-1626162038,669689561,112220218,502447212,-787793179,-726846372,-1611013491,204107194,1605165582,-566891128,2082852116,532995238,-1502590712,2136989777,-2031153343,371398938,-1907397429,342796391,609166045,-2007448660,-1096076344,-323570318,-2082980371,2129956379,-243553361,-1549960929,1502383415,-1394618779,694799815,78595689,-1439173023,-1416578800,685225786,-333502212,-1181308536,-380569313,772035354,-915266376,663709718,1443496021,-777017729,-883300731,-387828385,1907473488,-725483724,-972961871,-1255712537,383120918,1383877998,1722751914,-1156050682,1952527902,-560244497,1304305692,1173974542,-1313227247,-201476579,-298899493,-1828496581,-1724396350,1933643204,1531804925,1728655262,-955565449,-69843702,-461760848,268336768,1446130876,0,0,0,0,0,0,0,0,0,0]
input_list = [-959151711,623836953,209446690,-1950418142,1339915067,-733626417,481171539,-2125997010,-1225423476,1462109565,147434687,-1800073781,-1431212205,-450443973,50097298,753533734,-747189404,-2070885638,0,-1484353894,-340296594,-2133744570,619639811,-1626162038,669689561,0,112220218,502447212,-787793179,0,-726846372,-1611013491,204107194,1605165582,-566891128,2082852116,0,532995238,-1502590712,0,2136989777,-2031153343,371398938,-1907397429,342796391,609166045,-2007448660,-1096076344,-323570318,0,-2082980371,2129956379,-243553361,-1549960929,1502383415,0,-1394618779,694799815,78595689,-1439173023,-1416578800,685225786,-333502212,-1181308536,-380569313,772035354,0,-915266376,663709718,1443496021,-777017729,-883300731,-387828385,1907473488,-725483724,-972961871,-1255712537,383120918,1383877998,1722751914,0,-1156050682,1952527902,-560244497,1304305692,1173974542,-1313227247,-201476579,-298899493,-1828496581,-1724396350,1933643204,1531804925,1728655262,-955565449,0,-69843702,-461760848,268336768,1446130876]
#a = s.moveZeroes_with_space(input_list)
b = s.moveZeroes(input_list)
c = s.move_zeros_greatsolution(input_list)

print(c== expected_list)