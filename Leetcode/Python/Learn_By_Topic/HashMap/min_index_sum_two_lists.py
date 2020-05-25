class Solution:
    def findRestaurant(self, list1, list2):
        hashmap = {}
        min_index = 99999999
        result_list = []
        
        for index, each in enumerate(list1):
            hashmap[each] = index
            
        for index, each in enumerate(list2):
            if each in hashmap:
                if hashmap[each] + index < min_index:
                    min_index = hashmap[each] + index
        
        for index, each in enumerate(list2):
            if each in hashmap:
                if hashmap[each] + index == min_index:
                    result_list.append(each)
            
        return result_list
    
s = Solution()
s1 = ["Shogun","Tapioca Express","Burger King","KFC"]
s2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
print(s.findRestaurant(s1, s2))