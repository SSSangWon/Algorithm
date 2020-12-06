s1 = input()
s2 = input()

def solution(str1, str2):
    answerList = [[0 for i in range(len(str1)+1)]for j in range(len(str2)+1)]

    for i, iv in enumerate(str1):
        for j, jv in enumerate(str2):
            if iv == jv:
                answerList[i+1][j+1] = answerList[i][j]+1
            
            else:
                answerList[i+1][j+1] = max( answerList[i+1][j], answerList[i][j+1])
        
    return answerList

print(solution(s2, s1))