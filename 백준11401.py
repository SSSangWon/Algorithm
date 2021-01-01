# import sys

# N, K = map(int, sys.stdin.readline().rsplit())
# p = 1000000007

# def fac(n):
#     a = 1

#     for i in range(1, n+1):
#         a *= i
#         a %= p

#     return a

# def solution(a, b):
#     if b%2 > 0:
#         return solution(a, b-1) * a

#     elif b == 0:
#         return 1

#     elif b == 1:
#         return a
    
#     else:
#         half = solution(a, b//2)
#         return half**2 % p


# A = fac(N)
# B = (fac(K) * fac(N-K)) % p
# B = solution(B, (p-2)%p)

# print(A * B % p)



import sys

N, K = map(int, sys.stdin.readline().rsplit())
p = 1000000007

def fac(n):
    a = 1
    
    for i in range(1, n+1):
        a *= i
        a %= p

    return a

def solution(a, b, c=1000000007):
    if b == 1:
        return a % c
    
    else:
        p = solution(a, b//2, c)
        if b%2==0:
            return p * p % c
        else:
            return p * p * a % c

A = fac(N)
B = (fac(K) * fac(N-K)) % p
B = solution(B, (p-2)%p)

print(A * B % p)
