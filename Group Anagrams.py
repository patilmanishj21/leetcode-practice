strs = ["eat","tea","tan","ate","nat","bat"]
hashmap={}

for word in strs:
    value=1
    for char in word:
        value=value*ord(char)
    if value in hashmap:
        hashmap[value].append(word)
    else:
        hashmap[value]=[word]

res=[]   
for key in hashmap:
    res.append(hashmap[key])

print(res)

