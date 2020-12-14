def a(s):
    ans = 0

    for j in s:
        if ans < 0:
            return False
        elif j == '(':
            ans += 1     
        else:
            ans -= 1

    if ans == 0:
        return True
    else:
        return False

n = int(input())

for i in range(n):
    s = input()
    
    if a(s):
        print('YES')
    else :
        print('NO')