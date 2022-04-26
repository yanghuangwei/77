m=int(input("輸入階層值M:"))
total=1
n=1
while total<=m:
    n+=1
    total*=n
print("超過 M 為",m,"的最小階層的最小階層 N 值為",n)