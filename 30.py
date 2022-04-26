a=input("答案")
s=[]
h=""
i=0
while (True):
    if h==a:
        break
    else:
        h+=a[i]
        s.append(a[i])
        i+=1
while(True):
    b=input("猜")
    if(b=='0000'):
        break
    else:
        d=""
        u=0
        g=[]
        A=0
        B=0 
        while True:
            if d==b:
                break
            else:
                d+=b[u]
                g.append(b[u])
                u+=1
        for y in range(0,4):
            if s[y]==g[y]:
                A+=1
        for t in range(0,4):
            for o in range(0,4):
                if s[t]==g[o]:
                    B+=1
        print(A,"A",B-A,"B")