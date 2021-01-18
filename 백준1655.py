import sys
import heapq
r = sys.stdin.readline

N = int(r())

lh = []
rh = []
 
for i in range(N):
    n = int(r())
    sw = True
    
    if (i+1)%2 == 1:
        heapq.heappush(lh, -n)
        sw = False
    else:
        heapq.heappush(rh, n)
    
    if lh and rh:
        if -lh[0] > rh[0]:
            heapq.heappush(rh, -heapq.heappop(lh))
            heapq.heappush(lh, -heapq.heappop(rh))

    if sw:
        print(min(-lh[0], rh[0]))
    else:
        print(-lh[0])