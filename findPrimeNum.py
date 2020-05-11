'''
출처 : https://programmers.co.kr/learn/courses/30/lessons/42839

입출력 예
numbers	return
  17	  3
  011	  2
'''
# import itertools
# import math

# def primeNum(num):
#     n=""
#     for i in range(len(num)):
#         n+=max(num)
#     n=int(n)+1

#     p=[True]*n
#     l=math.ceil(math.sqrt(n))

#     for i in range(2,l):
#         if p[i]:
#             for j in range(i+i,n,i):
#                 p[j]=False
#     return [str(i) for i in range(2,n) if p[i]]

# def permutations(n):
#     p=[]
#     for i in range(1,len(n)+1):
#         p+=list(set(map(''.join, itertools.permutations(n, i))))

#     return p

# def solution(numbers):
#     answer = 0
#     p=permutations(numbers)
#     pN=primeNum(numbers)
#     print(p,pN)
#     for i in p:
#         if i in pN:
#             answer+=1
#     return answer

from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    print("1",a)
    a -= set(range(0, 2))
    print("2",a)
    for i in range(2, int(max(a) ** 0.5) + 1):
        print("2-1",i)
        a -= set(range(i * 2, max(a) + 1, i))
    print("3",a)
    return len(a)

print(solution("17"))
print(solution("011"))

