def toh(n,f,a,t):
    if n==1:
        print('move',1,'from rod',f,'to rod',t)
        return
    toh(n-1,f,t,a)
    print('move',n,'from rod',f,'to rod',t)
    toh(n-1,a,f,t)

n=int(input("enter no of disks"))
toh(n,'a','b','c')










