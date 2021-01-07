import sys

N = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

answer = 0
min = price[0]
for i in range(N-1):
    if min > price[i]:
        min = price[i]
    answer = answer + min * distance[i]

print(answer)