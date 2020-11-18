nList = [0 for i in range(100)]

nList[0] = 1
nList[1] = 1
nList[2] = 1
nList[3] = 2
nList[4] = 2

for i in range(5,100):
    nList[i] = nList[i-2]+nList[i-3]

a = int(input())

for i in range(a):
    n = int(input())
    print(nList[n-1])
