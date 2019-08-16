#10:19

def bs(a,k,s,e):
    if s<=e:
        mid=(s+e)//2
        if k==a[mid]:
            return mid
        elif k>a[mid]:
            return bs(a,k,mid+1,e)
        else:
            return bs(a, k, s, mid)





a=list(map(int,input().split()))
k=int(input())
a=sorted(a)
print(bs(a,k,0,len(a)-1))
#123
#3














