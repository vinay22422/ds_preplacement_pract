def eulidsfn(n,m):
    if m==0:
        return n
    return eulidsfn(m,n % m)




m,n=input().split()
m,n=int(m),int(n)
p1=min(m,n)
p2=max(m,n)
print(eulidsfn(p1,p2))














