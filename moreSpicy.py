'''
출처 : https://programmers.co.kr/learn/courses/30/lessons/42626

scoville	                   K	          return
[1, 2, 3, 9, 10, 12]	       7	            2
'''
# from collections import deque

# def scovilleScale(n1,n2):
#     return n1+(n2*2)

# def solution(scoville, K):
#     answer=0
#     s=deque(sorted(scoville))
    
#     while s[0]<K:

#         sS=s.popleft()+(s.popleft()*2)
#         for i,j in enumerate(s):
#             if j>sS:
#                 s.insert(i,sS)
#                 break
#         else:
#             s.append(sS)
#         answer+=1
        
#         if len(s)==1 and s[0]<K:
#             return -1
        
#     return answer

# #print(solution([1, 2, 3, 9, 10, 12],7))
# print(solution([1,1],9))


import heapq

def solution(s, K):
    answer=0
    heapq.heapify(s)

    while s[0]<K:

        sS=heapq.heappop(s)+(heapq.heappop(s)*2)

        heapq.heappush(s, sS)
        answer+=1
        
        # if len(s)==1 and s[0]<K:
        #     return -1
        
    return answer

print(solution([1, 2, 3, 9, 10, 12],7))
print(solution([1,1],9))
