'''
Given an array of integers arr, 
return true if the number of occurrences 
of each value in the array 
is unique or false otherwise.


Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:
Input: arr = [1,2]
Output: false
Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

'''

def uniqNumberOfOccurrences(nums):
    nums.sort()
    hashset={}
    for num in nums:
        if num in hashset:
            hashset[num]+=1
        else:
            hashset[num]=1
    counts=set()
    for count in hashset.values():
        if count in counts:
            return False
        else:
            counts.add(count)
    return True
#nums = [1,2,2,1,1,3]
nums = [1,2]
nums = [-3,0,1,-3,1,1,1,-3,10,0]
print(uniqNumberOfOccurrences(nums))