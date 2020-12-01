def Eratos(n):
    rn = int(n ** 0.5)
    prime = [True]*n

    for i in range(2, rn+1):
        if prime[i]:
            for j in range(i+i, n, i):
                prime[j] = False
    
    return [i for i in  range(2, n) if prime[i]]

n = int(input())

primeList = Eratos(n+1)

i = 0

while n != 1:
    if n%primeList[i] == 0:
        n //= primeList[i]
        print(primeList[i])
    else:
        i += 1
