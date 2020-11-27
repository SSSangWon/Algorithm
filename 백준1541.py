n = input()
cnt = 0
sw = 0

nList = list(map(str, n.split('-')))

if nList[0] == '':
    nList.pop(0)
    sw = 1

# 첫번째 수 양수이면 cnt+= 음수이면 cnt-=
if sw == 0:
    cnt += sum(map(int, nList[0].split('+')))
else:
    cnt -= sum(map(int, nList[0].split('+')))

for i in nList[1:]:
    cnt -= sum(map(int, i.split('+')))

print(cnt)