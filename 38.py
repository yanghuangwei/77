list=[]
place=int(input("輸入整數n:"))
for i in range(place):
    k=int(input("輸入整數k:"))
    list.append(k)
print("第",(list.index(18)+1),"個點",list[1])
print("第",(list.index(99)+1),"個點",list[4])