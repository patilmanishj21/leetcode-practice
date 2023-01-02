import collections

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

cols=collections.defaultdict(set)
rows=collections.defaultdict(set)
sq=collections.defaultdict(set)

def sudoku():
    for r in range(9):
        for c in range(9):
            if str(board[r][c])==".":
                continue
            if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in sq[(r //3 ,c // 3)]):
                return False
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            sq[(r //3 ,c // 3)].add(board[r][c]) 
    return True


print(sudoku())
            



# maprow={}
# for row in board:
#     for i in range(0,9):
#         if str(row[i])==".":
#             pass
#         else:
#             maprow[row[i]]=1+maprow.get(row[i],0)
#     print("roW---")
#     if 2 in maprow.values():
#         print(False)
#         break
#     else:
#         print(True)
#     maprow={}

# mapcol={}
# for i in range(0,9):
#         if str(board[i][8])==".":
#             pass
#         else:   
#             mapcol[board[i][8]]=1+mapcol.get(board[i][8],0)

#         print("cOLUMS---")
#         if 2 in mapcol.values():
#             print(False)
#             break
#         else:
#             print(True)
        

 







