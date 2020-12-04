n = list(map(int, input().split()))

def Gcd(num1, num2):
    p = min(num1, num2)
    p1 = 1
    answer = 1
    
    while answer%num1 != 0 or answer%num2 != 0:
        answer = p*p1
        p1+=1

    return answer

def Lcm(num1, num2):
    p = min(num1, num2)

    while num1%p != 0 or num2%p != 0:
        p -= 1
    
    return p

print(Lcm(n[0], n[1])) 
print(Gcd(n[0], n[1]))
