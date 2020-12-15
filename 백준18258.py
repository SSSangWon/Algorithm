import sys
from collections import deque

# class Que():
#     def __init__(self):
#         self.q = []
#         self.cnt = 0

#     def push(self, x):
#         self.q.append(x)
#         self.cnt += 1

#     def pop(self):
#         if self.cnt != 0:
#             self.cnt-=1
#             return(self.q.pop(0))
#         else:
#             return -1

#     def size(self):
#         return self.cnt

#     def empty(self):
#         return 0 if self.cnt != 0 else 1

#     def front(self):
#         if self.cnt != 0:
#             return self.q[0]
#         else:
#             return -1

#     def back(self):
#         if self.cnt != 0:
#             return self.q[self.cnt-1]
#         else:
#             return -1

n = int(sys.stdin.readline())
que = deque([])
# que = Que()

for i in range(n):
    order = sys.stdin.readline().rsplit()

    if order[0] == 'push':
        que.append(order[1])

    elif order[0] == 'pop':
         sys.stdout.write(str(que.popleft() if que else -1) + '\n')
    
    elif order[0] == 'size':
        sys.stdout.write(str(len(que)) + '\n')
    
    elif order[0] == 'empty':
         sys.stdout.write(str(0 if que else 1) + '\n')

    elif order[0] == 'front':
         sys.stdout.write(str(que[0] if que else -1) + '\n')

    elif order[0] == 'back':
         sys.stdout.write(str(que[-1] if que else -1) + '\n')
