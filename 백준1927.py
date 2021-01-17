import sys
import heapq

r = sys.stdin.readline

N = int(r())
h = []

for i in range(N):
    n = int(r())
    if n == 0:
        if h:
            print(heapq.heappop(h))
        else:
            print(0)
    else:
        heapq.heappush(h, n)
