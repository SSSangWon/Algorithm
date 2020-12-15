import sys
from collections import deque

n = int(sys.stdin.readline())
dequeue = deque()

for i in range(n):
    order = sys.stdin.readline().rsplit()

    if order[0] == 'push_front':
        dequeue.appendleft(order[1])
    
    elif order[0] == 'push_back':
        dequeue.append(order[1])

    elif order[0] == 'pop_front':
         sys.stdout.write(str(dequeue.popleft() if dequeue else -1) + '\n')
    
    elif order[0] == 'pop_back':
         sys.stdout.write(str(dequeue.pop() if dequeue else -1) + '\n')

    elif order[0] == 'size':
        sys.stdout.write(str(len(dequeue)) + '\n')
    
    elif order[0] == 'empty':
         sys.stdout.write(str(0 if dequeue else 1) + '\n')

    elif order[0] == 'front':
         sys.stdout.write(str(dequeue[0] if dequeue else -1) + '\n')

    elif order[0] == 'back':
         sys.stdout.write(str(dequeue[-1] if dequeue else -1) + '\n')