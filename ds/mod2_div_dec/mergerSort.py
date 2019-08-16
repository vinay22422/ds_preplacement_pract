def merge(a, b, no):
    c = list()
    i, j, k = 0, 0, 0
    while i < len(a) and j < len(b) and k < no:
        if int(b[j]) < int(a[i]):
            c.append(b[j])
            j += 1
        elif int(a[i]) <= int(b[j]):
            c.append(a[i])
            i += 1

        k += 1
    if i == len(a):
        c.extend(b[j:len(b)])
    if j == len(b):
        c.extend(a[i:len(a)])
    return c


def ms(noo):
    if len(noo) > 1:
        mid = int(len(noo) / 2)
        #observe the way array is indexed\
        a = ms(list(noo[:mid]))
        b = ms(list(noo[mid:]))
        c = merge(a, b, len(noo))
        return c
    return noo


no1 = list(map(int,input().split()))
print(*ms(no1))
