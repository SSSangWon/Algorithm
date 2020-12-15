import sys
from collections import deque

n = int(sys.stdin.readline())

for i in range(n):
    order = sys.stdin.readline()
    orLen = int(sys.stdin.readline())

    if orLen == 0:
        sys.stdin.readline()
        dq = deque() 
    else:
        dq = deque(map(int, sys.stdin.readline()[1:-2].split(','))) 
    try:
        r = True
        for j in order:
            if j == 'R':
                if r:
                    r = False
                else:
                    r = True
            elif j == 'D':
                if r:
                    dq.popleft()
                else:
                    dq.pop()
        if r:
            print(str(list(dq)).replace(' ', ''))
        else:
            dq.reverse()
            print(str(list(dq)).replace(' ', ''))

    except:
        print('error')