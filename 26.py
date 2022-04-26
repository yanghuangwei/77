while True:
    a=""
    i=0
    s=[]    
    h=""
    a=input("檢測的字串(end結束)")
    if(a=="end"):
        break
    else:
        b=input("檢測的單一字元")
        while True:
            if h!=a:
                h+=a[i]
                s.append(a[i])
                i+=1
            else:
                break
    print(s.count(b))