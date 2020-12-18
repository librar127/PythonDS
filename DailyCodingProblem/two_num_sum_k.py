'''
Problem: Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?

Solution: Three Approaches:
1. Using Brute Force Approach - Time: O(n^2) Space: O(1)
2. Using Sorting and start and end pointers - Time: O(nlog10) Space: O(n)
3. Using HashMap - Time: O(n) Space: O(n)
Using Approach 3rd for implementation - Assuming no duplicate numbers
'''


def two_num_sum_k(arr, k):
    
    hashset = set()
    for each in arr:
        hashset.add(each)
        
    for each in arr:
        if k-each in hashset:
            return (each, k-each)
        
    return "No Pair Found"


arr = [2, 3, 5, 8, 1, 4]
print(two_num_sum_k(arr, 25))
        