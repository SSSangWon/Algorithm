import sys
while(1):
    n, *nList = list(map(int, sys.stdin.readline().split()))
    nList.insert(0, 0)
    nList.append(0)
    
    if n == 0:
        break

    v = 0
    tC = [0]

    for i in range(1, n+2):
        while tC and nList[i] < nList[tC[-1]]:
            top = tC.pop()
            v = max(v, (i-1-tC[-1]) * nList[top])

        tC.append(i)
     
    print(v)

'''
def histo_sqr(histo_data):
    histo_data.append(0)
    max_sqr = 0
    tmp = []
    for i, h in enumerate(histo_data):
        # tmp 가 없거나, 현재 높이가 전의 높이보다 작을 때
        while tmp and histo_data[tmp[-1]] > h:
            # 높이
            ih = histo_data[tmp.pop()]
            # 너비
            iw = i - tmp[-1] - 1 if tmp else i
            if ih * iw > max_sqr:
                max_sqr = ih * iw
        tmp.append(i)
    return max_sqr


if __name__ == "__main__":
    while True:
        N, *histo_data = list(map(int, sys.stdin.readline().split()))
        if N == 0:
            break
        print(histo_sqr(histo_data))
'''