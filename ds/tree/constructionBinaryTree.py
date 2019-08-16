import math
class node:
    def __init__(self,v):
        self.data=v
        self.left=None
        self.right=None

def construct(elementstoinset,root,i,n):
    if i<n:
        t=node(int(elementstoinset[i]))
        root=t

        root.left=construct(elementstoinset,root,(2*i)+1,n)
        root.right = construct(elementstoinset, root, (2*i) + 2, n)
        return root
    return None

def bfs(root):
    q=[]

    q.append(root)
    while len(q)!=0:
        c=q.pop(0)
        print(c.data)
        if c.left!=None:
            q.append(c.left)

        if c.right != None:
            q.append(c.right)

def dfs(root):
    if root==None:
        return
    print(root.data)
    dfs(root.left)
    dfs(root.right)


elementstoinset=['6','7','8','9']
n=len(elementstoinset)
nooflevels=math.floor(   math.log2(n+1)               )
root=None
root = construct(elementstoinset,root,0,n)

bfs(root)
print()
dfs(root)















