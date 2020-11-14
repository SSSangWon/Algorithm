from os import name


n = int(input())
nList = list(map(int, input().split()))
oper = list(map(int, input().split()))

maxNum = -10000000000
minNum = 10000000000

def solution(index, value):

    global maxNum, minNum

    if index == n:

        # 최대값 갱신
        if value > maxNum:
            maxNum = value

        # 최소값 갱신
        if value < minNum:
            minNum = value

        return

    else:

        # 더하기
        if oper[0]>0:
            v = value + nList[index]
            oper[0] -= 1
            solution(index+1,v)
            oper[0] += 1

        # 빼기
        if oper[1]>0:
            v = value - nList[index]
            oper[1] -= 1
            solution(index+1,v)
            oper[1] += 1

        # 곱하기
        if oper[2]>0:
            v = value * nList[index]
            oper[2] -= 1
            solution(index+1,v)
            oper[2] += 1

        # 나누기
        if oper[3]>0:
            if value < 0:
                v = -(-(value) // nList[index])
            else:
                v = value // nList[index]

            oper[3] -= 1
            solution(index+1,v)
            oper[3] += 1

solution(1,nList[0])
print(maxNum)
print(minNum)
