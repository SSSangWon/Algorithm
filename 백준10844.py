# n = int(input())

# cnt = 0

# def solution(index, value):
#     global cnt

#     if index == n:
#         cnt += 1
#         return
    
#     else:
#         if value == 0:
#             solution(index+1, value+1)
            
#         elif value == 9:
#             solution(index+1, value-1)

#         else:
#             solution(index+1, value-1)
#             solution(index+1, value+1)

# if n < 2:
#     print(9)
# else:
#     for i in range(1,10):
#         solution(1, i)
#     print(cnt)

# make dp

n = int(input())

nList = [[1 for i in range(10)]]
nList[0][0] = 0

for i in range(n-1):
    nList.append([0 for i in range(10)])

for i  in range(n-1):
    for j in range(10):
        if j == 0:
            nList[i+1][j+1] += nList[i][j]
        elif j == 9:
            nList[i+1][j-1] += nList[i][j]
        else:
            nList[i+1][j+1] += nList[i][j]
            nList[i+1][j-1] += nList[i][j]

print(sum(nList[n-1])%1000000000)