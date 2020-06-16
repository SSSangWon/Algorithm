'''
출처 : https://programmers.co.kr/learn/courses/30/lessons/12905
'''

def solution(board):
    for i in range(1,len(board)):
        for j in range(1,len(board[i])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j],board[i][j-1],board[i-1][j-1])+1
    
    m=max(map(max, board))

    return m*m

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])) #result 9
print(solution([[0,0,1,1],[1,1,1,1]])) #result 4
print(solution([[0,1,1,1],[1,1,0,1],[0,1,1,1],[0,0,1,0],[0,0,1,1],[1,1,1,1]])) #result 9
#a=[[0,0,1,1],[1,1,1,1]]
#for i in range(2,4):
#    for j in range(0,2):
#            print(a[j][i])
