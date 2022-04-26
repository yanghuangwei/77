fare=75
for i in range(5):
    dis=float(input("請輸入路程公里數(km):"))
    if dis<1.5:
        print("所需車資為:75")
    elif 1.5<dis<=1.75:
        print("所需車資為:"+str(fare+5))
    elif ((dis-1.5)*1000)%250==0:
        print("所需車資為:"+str(fare+(((dis-1.5)*1000)/250)*5))
    elif ((dis-1.5)*1000)%250!=0:
        print("所需車資為:"+str(fare+((((dis-1.5)*1000)//250)+1)*5))