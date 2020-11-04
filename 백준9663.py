N = int(input())
cnt = 0

a = [True for i in range(N)]
b = [True for i in range(2*N-1)]
c = [True for i in range(2*N-1)]

def Q(n):
    global cnt
    
    if n==N:
        cnt+=1
        return
    
    for i in range(N):
        if a[i] and b[n+i] and c[N-1+n-i]:
            a[i]=b[n+i]=c[N-1+n-i]=False
            Q(n+1)
            a[i]=b[n+i]=c[N-1+n-i]=True

Q(0)
print(cnt)