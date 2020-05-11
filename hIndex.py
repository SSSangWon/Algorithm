'''
출처 : https://programmers.co.kr/learn/courses/30/lessons/42747
'''

def solution(citations):
    c=sorted(citations)
    answer=1

    if c[-1]==0:
        return 0

    while c:
        if answer <= c[-1]: 
            c.pop()
            answer+=1
        else:
            break

    return answer-1

print(solution([3, 0, 6, 1, 5])) #return 3