'''
Given a binary array nums and an integer k, 
return the maximum number of 
consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
'''
def max_consecutive_ones(nums,k):
    max_w=0
    num_zero=0
    n=len(nums)
    left=0

    for right in range(n):
        if nums[right]==0:
            num_zero+=1
        while num_zero> k:
            if nums[left]==0:
                num_zero-=1
            left+=1

        w= right-left+1

        max_w=max(max_w,w)

    return max_w

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

print(max_consecutive_ones(nums,k))