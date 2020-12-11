def cntNum(n1,n2):
    cnt = 0

    while n1 != 0:
        n1 //= n2
        cnt += n1

    return cnt

N, K = map(int, input().split())

five = cntNum(N, 5)
five -= cntNum(N-K, 5)
five -= cntNum(K, 5) 

two = cntNum(N, 2)
two -= cntNum(N-K, 2)
two -= cntNum(K, 2)

print(min(five, two))
