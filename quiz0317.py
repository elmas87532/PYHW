def isPrime(N):
    for x in range(2,(N-1)):
        if N%x==0:
            return 0
    return 1

total=0
for x in range(2,1001):
    if isPrime(x):
        total=total+x

print total

