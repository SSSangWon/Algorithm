'''
출처 : https://programmers.co.kr/learn/courses/30/lessons/42629
'''

import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    h=[]
    for i,j in enumerate(dates):
        if j<=stock:
            heapq.heappush(h, (-supplies[i],supplies[i]))
        else:
            while stock<j:
                stock += heapq.heappop(h)[1]
                answer+=1
                if stock>k-1:
                    return answer
            heapq.heappush(h, (-supplies[i],supplies[i]))


    while stock<k: 
        stock += heapq.heappop(h)[1]
        answer+=1
        if stock>k-1:
            return answer

print(solution(4,[4,10,15],[20,5,10],30)) #return 2
