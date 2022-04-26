for i in range(2):
    count=1
    num=input("輸入第一行正整數為:")
    inpnum=input("第二行中數列中的數字為:")
    inpunmspe=inpnum.split()
    for k in inpunmspe:
        if inpunmspe.count(k) > count:
            count=inpunmspe.count(k)
            j=k
    if count==1:
        print("每個數字剛好只出現 1 次")
    else:
        print("最大出現次數的數字為:",int(j),"，出現次數為:",count)