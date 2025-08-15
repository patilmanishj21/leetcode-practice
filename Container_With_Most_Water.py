'''
You are given an integer array height of length n. There are n vertical 
lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.
Notice that you may not slant the container.
Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by 
array [1,8,6,2,5,4,8,3,7]. In this case, the max area of 
water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1

'''



def containerWithMostWater(height):
    start=0
    end=len(height)-1
    max_area=0
    while start< end:
        area=min(height[start],height[end])*(end-start)

        if height[start] < height[end]:
            start += 1
        else:
            end -= 1

        max_area=max(area, max_area)


    return max_area


# height = [1,8,6,2,5,4,8,3,7]
# height=[1,1]
# height = [4, 3, 2, 1, 4]

#height=[8,7,2,1]

height=[3,3,4]



print(containerWithMostWater(height))