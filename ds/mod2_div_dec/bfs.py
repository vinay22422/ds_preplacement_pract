class node:
    def __init__(self,d):
        self.data=d
        self.left=None
        self.right=None


def bfs(r1):

    q=[]

    q.append(r1)
    while len(q)>0:
        d=q.pop(0)
        print(d.data)
        if d.left!=None:
            q.append(d.left)
        if d.right!=None:
            q.append(d.right)


r=node(8)
r.left=node(3)
r.right=node(10)
r.right.right=node(14)
r.right.right.left=node(13)
r.left.left=node(1)
r.left.right=node(6)
r.left.right.right=node(7)
bfs(r)

#8 3 10 1 6 14 4 7 13