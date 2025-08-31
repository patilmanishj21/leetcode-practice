'''
Given a 0-indexed n x n integer matrix grid, 
return the number of pairs (ri, cj) 
such that row ri and column cj are equal.
A row and column pair is considered equal 
if they contain the same elements 
in the same order (i.e., an equal array).

Example 1:

Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]

'''


def EqualRowandColumnsPair(grid):
    # hashset={}
    # for i in range(len(grid)):
    #     col=[]
    #     for j in range(len(grid[i])):
    #         col.append(grid[i][j])
    #         tup=tuple(col)
    #     if tup in hashset:
    #         hashset[tup]+=1
    #     else:
    #         hashset[tup]=1
    # for j in range(len(grid[0])):
    #     row=[]
    #     for i in range(len(grid)):
    #         row.append(grid[i][j])
    #         tup=tuple(row)
    #     if tup in hashset:
    #         hashset[tup]+=1
    #     else:
    #         hashset[tup]=1
            
    # print(hashset)
    hashset = {}
    n = len(grid)
    count = 0

    for i in range(n):
        row=[]
        for j in range(n):
            row.append(grid[i][j])
        tup= tuple(row)
        if tup in hashset:
            hashset[tup]+=1
        else:
            hashset[tup]=1
    for j in range(n):
        col=[]
        for i in range(n):
            col.append(grid[i][j])
        tup = tuple(col)
        if tup in hashset:
            count+=hashset[tup]
    return count
            
        
       

            

grid = [[3,2,1],[1,7,6],[2,7,7]]
print(EqualRowandColumnsPair(grid))