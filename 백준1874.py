n = int(input())

nList = [int(input()) for i in range(n)]
rList = []
aList = []

x = 0

for i in nList:
    if i > x:
        for j in range(x+1, i):
            aList.append(j)
            rList.append('+')
        rList.append('+')
        rList.append('-')
        x = i

    elif i == aList[-1]:
        aList.pop()
        rList.append('-')

    else:
        rList.clear()
        break

if rList:
    for i in rList:
        print(i)

else:
    print('NO')