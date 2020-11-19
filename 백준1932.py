# n = int(input())
# triangle = [list(map(int,input().split())) for i in range(n)]

# maxNum = 0 

# def maxValue(depth, value, select):
    
#     global maxNum

#     if depth == n:
#         if maxNum < value:
#             maxNum = value
#         return
    
#     else:
#         value += triangle[depth][select]
#         maxValue(depth+1, value, select)
#         value -= triangle[depth][select]

#         if select != depth:
#             value += triangle[depth][select+1]
#             maxValue(depth+1, value, select+1)
#             value -= triangle[depth][select+1]

#         elif select != 0:
            
#             value += triangle[depth][select-1]
#             maxValue(depth+1, value, select-1)
#             value -= triangle[depth][select-1]

# maxValue(0,0,0)
# print(maxNum)

n = int(input())

triangle = [list(map(int,input().split())) for i in range(n)]
answer=[]

for i in range(n):
    answer.append([0 for j in range(i+1)])

answer[0][0] = triangle[0][0]
for i in range(n-1):
    for j, v in enumerate(triangle[i]):
        answer[i+1][j] = max(answer[i+1][j],triangle[i+1][j]+answer[i][j])
        answer[i+1][j+1] = max(answer[i+1][j+1],triangle[i+1][j+1]+answer[i][j])
        # if answer[i+1][j] < triangle[i+1][j]+answer[i][j]:
        #     answer[i+1][j] = triangle[i+1][j]+answer[i][j]
        # if answer[i+1][j+1] < triangle[i+1][j+1]+answer[i][j]:
        #     answer[i+1][j+1] = triangle[i+1][j+1]+answer[i][j]

print(max(answer[n-1]))