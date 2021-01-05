import sys

n = int(sys.stdin.readline())
nList = list(map(int, sys.stdin.readline().rsplit()))

answer = [-1 for i in range(n)]
st = []

for i in range(n):
    while st and nList[st[-1]] < nList[i]:
        answer[st.pop()] = nList[i]
    
    st.append(i)

print(*answer)
