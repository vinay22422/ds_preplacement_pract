f='''

i = 0 to n-1
pratisalanu i inda munde iro elemntsalli min select madi we will exchange it with A[i]

'''
def selectionsort(m):
    for i,d in enumerate(m):
        min=i
        for j in range(i+1,len(m)):
            if m[j]<m[min]:
                min=j
        m[i],m[min]=m[min],m[i]
    print(m)







mylist=[7,8,1,9,2,4,5,6,33,44,55,77,88,99]
print(selectionsort(mylist))

