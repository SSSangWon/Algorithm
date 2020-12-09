bagN, bagK = map(int, input().split())

obj = list(list(map(int, input().split()))for i in range(bagN))
answer1 = [[0]*(bagK+1)]*(bagN+1)
answer = [[0 for i in range(bagK + 1)] for j in range(bagN + 1)]


for i in range(1, bagN+1):
    for j in range(1, bagK+1):
        w = obj[i-1][0]
        v = obj[i-1][1]
        
        if j < w:
            answer[i][j] = answer[i-1][j]

        else:
            answer[i][j] = max(v+answer[i-1][j-w], answer[i-1][j])
    #     print('%2d' % answer[i][j] ,end=' ')
    # print()

print(answer[bagN][bagK])