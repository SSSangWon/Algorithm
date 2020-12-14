import sys 

def push(x):
    stack.append(x)

def pop():
    if stack:
        return stack.pop()
    else:
        return -1

def size():
    return len(stack)

def empty():
    if stack:
        return 0
    else:
        return 1

def top():
    if stack:
        return stack[-1]
    else:
        return -1

n = int(sys.stdin.readline())

stack = []

for i in range(n):
    k = sys.stdin.readline().split()

    if k[0] == 'push':
        push(int(k[1]))
    
    elif k[0] == 'pop':
        print(pop())

    elif k[0] == 'size':
        print(size())   

    elif k[0] == 'empty':
        print(empty())   

    elif k[0] == 'top':
        print(top())   