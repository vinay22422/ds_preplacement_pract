def bfsm(s,ss):
    for i,d in enumerate(s):
        if i>len(s)-1-len(ss):  # u can skip this statement
            break   # u can skip this statement
        for j in range(0,len(ss)):
            if ss[j]!=s[i+j]:
                break

            if j==len(ss)-1:
                return i
    return -1




s="i am siddesh. i'm a good oy"
ss="boy"
print(bfsm(s,ss))


