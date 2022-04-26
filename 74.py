a=["red","blue","red","green"]
while True:
    b=input("猜")
    if(b=="red blue red green"):
        print("正確答案")
        break
    else:
        h=""
        d=b.split(" ")
        for t in range(4):
            if a[t]==d[t]:
              h+="1"
            elif a[t]!=d[t] and a.count(d[t])>0:
                h+="2"
            else:
                h+="3"
        print(h)