import sys

def sS(s):
    st = []
    
    for i in s:
        if i == '(' or i == '[':
            st.append(i)
        
        elif i == ')':
            if not st or st[-1] == '[':
                return 'no'
            st.pop()
            
        elif i == ']':
            if not st or st[-1] == '(':
                return 'no'
            st.pop()
            
    
    if st:
        return 'no'
    else:
        return 'yes'

while 1:
    s = sys.stdin.readline().rstrip()
    
    if s == '.':
        break

    print(sS(s))