
def partition(no ,l ,r):
    p = no[l]
    i, j= 0, r
    while True:
        while i <=r :
             if not no[i] <= p:
                 break
             i += 1
        while j >= 0:
            if not no[j] >= p:
                break
            j -= 1
        if i>j :
            break
        #print(i,'=i and j=',j)
        no[i], no[j]= no[j],no[i]
    no[l], no[j] = no[j], no[l]
    return j



def qs(no, l, r):
    if l < r:
        s = partition(no, l, r)
        qs(no, l, s - 1)
        qs(no, s + 1, r)



no1 = list(map(int, input().split()))
qs(no1, 0, len(no1) - 1)
print(*no1)

