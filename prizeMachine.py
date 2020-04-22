'''
출처 : https://programmers.co.kr/learn/courses/30/lessons/64061

[제한사항]
board 배열은 2차원 배열로 크기는 5 x 5 이상 30 x 30 이하입니다.
board의 각 칸에는 0 이상 100 이하인 정수가 담겨있습니다.
0은 빈 칸을 나타냅니다.
1 ~ 100의 각 숫자는 각기 다른 인형의 모양을 의미하며 같은 숫자는 같은 모양의 인형을 나타냅니다.
moves 배열의 크기는 1 이상 1,000 이하입니다.
moves 배열 각 원소들의 값은 1 이상이며 board 배열의 가로 크기 이하인 자연수입니다.

[입출력 예]

board
[0,0,0,0,0]
[0,0,1,0,3]
[0,2,5,0,1]
[4,2,4,4,2]
[3,5,1,3,1]

moves
[1,5,3,5,1,2,1,4]

result
4

'''
def solution(board, moves):
    answer=0
    
    board2=[[i[j] for i in board if i[j]!=0] for j in range(len(board))]
    stack=[]

    for i in moves:
        if board2[i-1]:
            if stack and board2[i-1][0] == stack[-1]:
                stack.pop()
                answer+=2
                
            else :
                stack.append(board2[i-1][0])

            board2[i-1].pop(0)
            print(stack)

    return answer


#출력
board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]

print(solution(board, moves))
