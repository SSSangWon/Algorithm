'''
출처 : https://programmers.co.kr/learn/courses/30/lessons/12909
'''

def solution(s):
    answer=True   
    p=0

    for i in s:
        if i=="(":
            p+=1
        elif i == ")":
            p-=1
        if p== -1:
            return False
    if p!=0:
        answer=False
    return answer

print(solution("()()")) # true
print(solution("(())()")) # true
print(solution(")()(")) # false
print(solution("(()(")) # false