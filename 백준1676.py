import math

n = math.factorial(int(input()))

result = 0

while n % 10 == 0:
    n //= 10
    result+=1

print(result) 