import collections
nums = [0,3,7,2,5,8,4,6,0,1]

setNums=set(nums)
longest=0

for n in nums:
    if (n-1)  not in setNums:
        len=1
        while(n+len) in setNums:
            len+=1
        longest=max(longest,len)
print(longest)


# dmap={}
# countlist=[]
# count=1
# for i in range(0,len(nums)):
#     for j in range (len(nums)-1):
#         if(nums[j]>nums[j+1]):
#             temp=nums[j]
#             nums[j]=nums[j+1]
#             nums[j+1]=temp
# print(nums)
# for ele in range(0,len(nums)-1):
#     if nums[ele] == nums[ele+1]-1:
#         count+=1
#     else:
#         countlist.append(1)
#         count=1
# countlist.append(count)

# print(max(countlist))

# for i in range(len(nums)):
#     dmap[nums[i]]=1+dmap.get(nums[i],0)

# ddmap=collections.OrderedDict(sorted(dmap.items()))

# for k,v in ddmap.items():
#     print(k,v) 