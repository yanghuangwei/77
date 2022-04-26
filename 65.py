for i in range(3):
    inpa=list(input("請輸入A的好友:").split())
    inpb=list(input("請輸入B的好友:").split())
    add=inpa+inpb
    num = 0
    for i in add:
        if add.count(i) == 2:
            num += 1
    print(int(num/2))