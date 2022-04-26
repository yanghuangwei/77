for i in range(4):
    ans=input("請輸入第一組數字:")
    user=(input("請輸入第二組數字:"))
    a=0
    b=0
    for i in range(len(ans)):
        if ans[i]==user[i]:
            a+=1
        elif user[i] in ans:
            b+=1     
    if (a==4):
        print(a,"A",b,"B","全對")
    else:
        print(a,"A",b,"B","加油")
    
    
