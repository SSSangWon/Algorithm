# n = int(input())
# cnt = 0

# def solution(index):

#     global cnt
    
#     if index==0:
#         cnt+=1
#         return

#     else:
#         if index>1:
#             solution(index-2)
#         if index>0:
#             solution(index-1)

# if n != 0:
#     solution(n)

# print(cnt%15746)

n = int(input())
if n<1:
    print(0)
elif n==1:
    print(1)
elif n==2:
    print(2)
else:
    nList = [0 for i in range(n+1)]

    nList[1] = 1
    nList[2] = 2

    for i in range(3, n+1):
        nList[i] = (nList[i-1] + nList[i-2])%15746

    print(nList[n])