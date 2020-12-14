n = int(input())
nList = []

for i in range(n):
    a = int(input())
    
    if a == 0:
        nList.pop()
        
    else:
        nList.append(a)
    
print(sum(nList))