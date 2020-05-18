'''
출처 : https://programmers.co.kr/learn/courses/30/lessons/43165
'''
def solution(numbers, target):
    p=[0]
    for i in numbers:
        pp=[]
        for j in p:
            pp.append(j+i)
            pp.append(j-i)
        p=pp
    return p.count(target)
    
print( solution([1, 1, 1, 1, 1],3) ) #return 5
print( solution([1, 3, 3, 5, 1],3) ) #return 5