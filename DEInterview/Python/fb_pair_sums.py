def numberOfWays(arr, k):
 	# Write your code here
  hashmap = {}
  for each in arr:
    if each in hashmap:     
      hashmap[each] += 1
    else: 
      hashmap[each] = 1
  
  
  count = 0
  for each in hashmap:
    if k-each in hashmap and k-each != k/2:
      count += hashmap[each]
    elif k-each in hashmap and k-each == k/2:
      count += hashmap[each] * (hashmap[each]-1)
  return count // 2


k_2 = 6
arr_2 = [1, 5, 3, 3, 3]
print(numberOfWays(arr_2, k_2))