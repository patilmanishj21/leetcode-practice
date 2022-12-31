def productExceptSelf(nums):
        res=[1]*len(nums)

        pre=1
        for i  in range(len(nums)):
            res[i] = pre
            pre=pre*nums[i]
        
        post=1
        for j  in range(len(nums)-1,-1,-1):
            res[j]=res[j]*post
            post=post*nums[j]
        
        return res

nums = [1,2,3,4]
print(productExceptSelf(nums))
