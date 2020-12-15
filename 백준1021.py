import sys
from collections import deque

n, n1 = sys.stdin.readline().rsplit()
m = list(map(int, sys.stdin.readline().rsplit()))
cnt = 0

dq = deque([i for i in range(1,int(n)+1)])

for i in m:
    start = dq.index(i)
    while True:
        t = dq.index(i)
        if i == dq[0]:
            dq.popleft()
            break
        elif start > len(dq)//2:
            dq.appendleft(dq.pop())
            cnt+=1
        else:
            dq.append(dq.popleft())
            cnt+=1

print(cnt)
