def topKFrequent(nums, k):
        counts={}
        values=[[] for i in range(len(nums)+1)]
        for ele in nums:
            counts[ele]=1+counts.get(ele,0)
        
        for key,v in counts.items():
            values[v].append(key)

        res=[]
        for i in range(len(values)-1,0,-1):
            for n in values[i]:
                res.append(n)
                if len(res) == k:
                    return res
                    

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums,k))
        