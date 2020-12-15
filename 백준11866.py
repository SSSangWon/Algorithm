import sys
from collections import deque

n = list(map(int,sys.stdin.readline().split()))
dq = deque([i for i in range(1, n[0]+1)])

print('<', end='')
while len(dq) != 1:
    for i in range(n[1]-1):
        dq.append(dq.popleft())
    print(dq.popleft(), end=', ')

print(dq[0], end='')
print('>')