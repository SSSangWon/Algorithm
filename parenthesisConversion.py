'''
출처 : https://programmers.co.kr/learn/courses/30/lessons/60058

입출력 예

p	            result
"(()())()"    "(()())()"
")("	         "()"
"()))((()"	  "()(())()"
'''





def solution(p):
    answer = ''
    cnt=0
    u=''
    v=''

    #1단계
    if not p:
        return answer


    #2단계
    for i,j in enumerate(p):
        if j =='(':
            cnt+=1
        else:
            cnt-=1
        if cnt==0:
            u=p[0:i+1]
            v=p[i+1:]
            break
    #3단계   
    if u[0] == '(':
        u+=solution(v)

    #4단계
    else:
        #4-1
        p='('
        #4-2
        p+=solution(v)
        #4-3
        p+=')'

        #4-4
        u=u[1:-1]
        p+=u.translate(str.maketrans('()',')('))
        return p

    return u
    
    

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))

print(3==0)