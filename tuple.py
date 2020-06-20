'''
def solution(s):
    answer=[]
    a=[]
    p=[]
    s=s[1:-1]
    s=s.replace('},','-')
    s=s.replace('}','')
    s=s.replace('{','')
    a=s.split('-')
    a.sort(key=len)

    for i in a:
        p.append(i.split(','))
    
    for i in p:
        for j in i:
            if int(j) in answer:
                continue
            else:
                answer.append(int(j))

    return answer
'''

def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

import re
from collections import Counter

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")) #[2, 1, 3, 4]
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")) #[2, 1, 3, 4]
print(solution("{{20,111},{111}}")) #[111, 20]
print(solution("{{123}}")) #[123]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")) #[3, 2, 4, 1]