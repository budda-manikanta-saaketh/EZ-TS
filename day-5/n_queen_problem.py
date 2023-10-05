n=int(input("enter the number of queens:"))
board=[[0 for i in range (n)] for i in range (n)]
def is_safe(board,row,col):
    for i in range (col):
        if board[row][i]==1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    for i,j in zip(range(row,n,1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    return True
def solve(board,col):
    if col>=n:
        return True
    for i in range (n):
        if is_safe(board,i,col):
            board[i][col]=1
            if solve(board,col+1)==True:
                return True
            board[i][col]=0
    return False
if solve(board,0)==False:
    print("solution does not exist")
else:
    for i in board:
        print(i)
        