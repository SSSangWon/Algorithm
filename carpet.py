'''
출처 : https://programmers.co.kr/learn/courses/30/lessons/42842
'''

def solution(brown, yellow):
    answer = []
    p=int(yellow**0.5)+1
    for i in range(1,p):
        if yellow%i==0:
            w=(yellow//i)+2
            h=i+2
            if w+w+h+h-4 == brown:
                return [w,h]
    return answer

print(solution(10,2))  # return [4,3]
print(solution(8,1))   # return [3,3]
print(solution(24,24)) # return [8,6]