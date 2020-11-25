n = list(map(int,input().split()))
cnt = 0
nList = []
for i in range(n[0]):
    nList.append(int(input()))

while n[1] != 0:
    result = n[1]//nList[-1]
    p = n[1]%nList[-1]
    
    if result == 0:
        nList.pop()
    
    elif result > 0:
        n[1] = p
        cnt += result

print(cnt) 