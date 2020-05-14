'''
출처 : https://programmers.co.kr/learn/courses/30/lessons/42885
'''

from collections import deque
'''
def solution(people, limit):
    answer = 0
    p=sorted(people)

    while p:
        p1=p.pop()
        for i,j in enumerate(p):
            if p1+p[0]>limit:
                break
            if p1+p[-1]<=limit:
                return answer+(-(-(len(p)+1)//2))
            if p1+j>limit:
                p.pop(i-1)
                break
        answer+=1
    return answer
'''

def solution(people, limit):
    answer = 0
    p=deque(sorted(people))

    while p:
        p1=p.pop()
        if p and p1+p[-1]<=limit:
            return answer+(-(-(len(p)+1)//2))
        if p and p1+p[0]<=limit:
            p.popleft()
        answer+=1
    return answer

'''
def solution(people, limit):
    answer = 0
    p=sorted(people)

    p1=-1
    p2=0
    
    while True:
        if p[p1] + p[p1-1]<=limit:
            return answer+(-(-len(p)//2))
'''    

            

print(solution([70, 50, 80, 50],100)) #return 3
print(solution([70, 80, 50],100)) #return 3
print(solution([40, 40, 40],160)) #return 3