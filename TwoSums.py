nums=[2,7,11,15]
target=9


def TwoSum(nums,target):
    dict1={}
    for count,ele in enumerate(nums):
        diff=target-ele
        if diff in dict1:
            return [dict1[diff],count]
        
        dict1[ele]=count

print(TwoSum(nums,target))

