list=[]
classroom=int(input("輸入任教班級數"))
for i in range(classroom):
    num=(int(input("輸入每班人數")))
    list.append(num)
print(max(list))