# n = int(input())
# minCount = 100000
# def solution(value,cnt):
#     global minCount

#     if value == 1:
#         minCount = min(minCount,cnt)
#         return
    
#     else:
#         if value%3 == 0:
#             solution(value/3,cnt+1)
#         if value%2 == 0:
#             solution(value/2,cnt+1)
#         solution(value-1, cnt+1)

# solution(n,0)
# print(minCount)

n = int(input())

nList = [0]*(n+1)
nList[1] = 0
nList[2] = 1
nList[3] = 1

for i in range(4,n+1):
    if i%3 == 0:
        nList[i] = min(nList[i//3]+1, nList[i-1]+1)
    elif i%2 == 0:
        nList[i] = min(nList[i//2]+1, nList[i-1]+1)
    else:
        nList[i] = nList[i-1]+1
    

print(nList[n]) 
