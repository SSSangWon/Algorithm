n = int(input())
nList = [0]+[int(input()) for i in range(n)]
result = [0 for i in range(n+1)]


if n == 0:
    print(0)

elif n == 1:
    print(nList[1])

elif n == 2:
    print(nList[1]+nList[2])

else:
    result[1] = nList[1]
    result[2] = nList[1]+nList[2]
    result[3] = max(nList[1]+nList[3], nList[2]+nList[3])

    for i in range(4, n+1):
        result[i] = max(result[i-3]+nList[i-1], result[i-2], result[i-4]+nList[i-1])+nList[i]

    print(max(result[-1], result[-2], result[-3]))
