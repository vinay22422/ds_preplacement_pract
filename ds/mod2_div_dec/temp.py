# Enter your code here. Read input from STDIN. Print output to STDOUTdef
from math import sqrt


def isprime(n):
    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True


def sumdiv(n):
    vsum = 0
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            vsum += i
        i += 1
    vsum += (n + 1)
    return vsum


l1, r1 = input().split()
l2, r2 = input().split()
l1, r1, l2, r2 = int(l1), int(r1), int(l2), int(r2)
if (l1+r1)-(l2+r2)>1000 and ((r1-l1)*l1) > ((r2-l2)*l2):
    print('A')
    exit(0)
if (l2+r2)-(l1+r1)>1000 and ((r1-l1)*l1) < ((r2-l2)*l2):
    print('B')
    exit(0)

llfo1,llfo2,rlfo1,rlfo2=[],[],[],[]
if l1>l2:
    #1st one has more elements on left
    llfo1=list(range(l2,l1))
elif l2>l1:
    llfo2=list(range(l1,l2))
if r1 > r2:
    # 1st one has more elements on left
    rlfo1 = list(range(r2, r1))
elif r2 > r1:
    rlfo2 = list(range(r1, r2))

max1, max2 = 0, 0
for i in llfo1:
    if isprime(i) and i>3:
        continue
    t = sumdiv(i)
    if t > max1:
        max1 = t
for i in rlfo1:
    if isprime(i) and i>3:
        continue
    t = sumdiv(i)
    if t > max1:
        max1 = t

for i in llfo2:
    if isprime(i) and i > 3:
        continue
    t1 = sumdiv(i)
    if t1 > max2:
        max2 = t1
for i in rlfo2:
    if isprime(i) and i > 3:
        continue
    t1 = sumdiv(i)
    if t1 > max2:
        max2 = t1
if max1 > max2:
    print('A')
elif max1 < max2:
    print('B')
else:
    print('Draw')






