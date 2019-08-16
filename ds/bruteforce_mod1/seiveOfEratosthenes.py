n=int(input())
myl=[x for x in range(1,n+1)]
myset=set(myl)
loop=int(n**0.5)

#function
for i in range(2,loop+1):
    j=2
    while i*j<=n:
        if i*j in myset:
            myset.remove(i*j)
        j+=1

print(myset)










