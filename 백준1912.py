n = int(input())
if n > 0:
    nList = list(map(int,input().split()))

    maxValue = nList[0]
    result = maxValue

    for i in range(1,n):
        if maxValue > 0 and maxValue + nList[i] > 0:
            maxValue += nList[i]

        else:
            maxValue = nList[i]
        
        result = max(maxValue, result)

    print(result)