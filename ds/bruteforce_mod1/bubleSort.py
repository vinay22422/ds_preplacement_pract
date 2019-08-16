f='''

i = 0 to n-1
pratisalanu i inda munde iro elemntsalli min select madi we will exchange it with A[i]

'''
def bubsort(m):
    for i in range(0,len(m)-1):

        for j in range(0,len(m)-1-i):
            if m[j+1] < m[j]:
                m[j+1],m[j]=m[j],m[j+1]
            print(m)

    print(m)







mylist=[109,7,8,1,9,2,4,5,6,33,44,55,77,88,99]
print(bubsort(mylist))

