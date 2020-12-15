import sys
from collections import deque

n = int(sys.stdin.readline())

for i in range(n):
    n1, n2 = map(int, sys.stdin.readline().split())
    dq = deque(list(map(int, sys.stdin.readline().split())))
    cnt = 0
    while True:
        if dq[n2] == max(dq) and n2 == 0:
            print(cnt+1)
            break
        else:
            if dq[0] == max(dq):
                dq.popleft()
                cnt += 1
            else: 
                dq.append(dq.popleft())
            
            if n2 == 0:
                n2 = len(dq)-1
            else:
                n2 -= 1
