'''
출처 : https://programmers.co.kr/learn/courses/30/lessons/42578
'''

def solution(clothes):
    dic={}
    answer = 1
    for i in clothes:
        if i[1] in dic:
            dic[i[1]]+=1
        else:
            dic[i[1]]=1
    for i in dic.values():
        answer*=(i+1)
    return answer-1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
#return 5

print(solution([ ["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"] ]) )
#return 3