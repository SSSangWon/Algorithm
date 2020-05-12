'''
출처 : https://programmers.co.kr/learn/courses/30/lessons/42841
'''
import itertools

def checkSB(a,b):
    strick=0
    ball=0
    
    for i in range(0, 3):
        for j in range(0, 3):
            if(a[i] == b[j] and i == j):
                strick += 1
            elif(a[i] == b[j] and i != j):
                ball += 1
    return (strick,ball)

def solution(baseball):
    answer=0

    a=['1','2','3','4','5','5','6','7','8','9']
    s=list(set(map(''.join,itertools.permutations(a,3))))

    for i in s:
        for j in baseball:
            if checkSB(i,str(j[0])) != (j[1],j[2]):
                break
        else:
            print(i)
            answer+=1

    return answer

print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]])) # return 2
