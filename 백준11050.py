N, K = map(int, input().split())

n1 = 1
n2 = 1

for i in range(N, N-K, -1):
    n1 *= i

for i in range(1, K+1):
    n2 *= i
    
print(n1//n2)