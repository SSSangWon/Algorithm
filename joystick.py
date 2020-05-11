'''
출처 : https://programmers.co.kr/learn/courses/30/lessons/42860

문제 설명
조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

조이스틱을 각 방향으로 움직이면 아래와 같습니다.

▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동
예를 들어 아래의 방법으로 JAZ를 만들 수 있습니다.

- 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

제한 사항
name은 알파벳 대문자로만 이루어져 있습니다.
name의 길이는 1 이상 20 이하입니다.
입출력 예
name	return
JEROEN	56
JAN	23
출처

※ 공지 - 2019년 2월 28일 테스트케이스가 추가되었습니다.
'''

  #alpa=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def zeroCount(p):
    mcnt=0 # 젤 높은 개수
    cnt=0  # 개수
    for i in p:
        if i==0:
            cnt+=1
            if cnt>mcnt:
                mcnt=cnt
        else:
            cnt=0
    return mcnt


def solution(name):
    fcnt=0 # 앞에서 세는 0
    bcnt=0 # 뒤에서 세는 0
    answer=0
    p=[min(ord(i)-ord("A"), ord("Z")-ord(i)+1)  for i in name]
    zc=zeroCount(p)

    for i in range(len(p)):
        if zc==0:
            print(p)
            return sum(p)+len(p)-1
        else:# 0이 연결되어있는 개수보다 지나온 길의 개수가 더 많으면 한쪽으로 가다가 돌아가는거 없음
            if p[i] == 0 and i<=zc: #첫번째가 0이면 뒤로 돌아가는게 빠름
                for j in range(i,len(p)):
                    if p[j] == 0:
                        fcnt+=1
                        if fcnt==zc:
                            print("zc",p,zc)
                            if answer ==0: answer=sum(p)+len(p)-zc+i-2 
                            else : min(answer,sum(p)+len(p)-zc+i-2 )
                    else:
                        break
            elif p[i] == 0 and i>=zc: #첫번째가 0이면 뒤로 돌아가는게 빠름
                for j in range(i,len(p)-1):
                    if p[j] == 0:
                        fcnt+=1
                        if fcnt==zc:
                            print("bzc",p,zc)
                            if answer ==0: answer=sum(p)+len(p)-zc+(len(p)-i-2)-2 
                            else : min(answer,sum(p)+len(p)-zc+(len(p)-i-2)-2 )
                    else:
                        break
            elif p[-1] == 0:
                for j in range(len(p)-1,0,-1):
                    if p[j] == 0:
                        bcnt+=1
                    else:
                        break
            
                if fcnt>bcnt: #뒤로가야함
                    print("fcnt",p,fcnt)
                    if answer ==0: answer=sum(p)+len(p)-1-fcnt
                    else : min(answer,sum(p)+len(p)-1-fcnt)
                else: #앞으로가야함
                    print("bcnt",p,bcnt)
                    if answer ==0: answer=sum(p)+len(p)-1-bcnt
                    else : min(answer,sum(p)+len(p)-1-bcnt)
    return answer



n1="JEROEN"
n2="JAN"
n3="BBABAAAAAB" #9
n4="BAAABABB" #8
print(solution(n3))
