num=int(input("搭了幾次電梯:"))
floor=1
sum=0
for i in range(num):
    arrivefloor=int(input())
    if arrivefloor-floor>0:
        sum1=(arrivefloor-floor)*20
        floor=arrivefloor
        sum=sum1+sum
    elif arrivefloor-floor<0:
        sum2=abs((arrivefloor-floor))*10
        floor=arrivefloor
        sum=sum2+sum
print(sum,"元")