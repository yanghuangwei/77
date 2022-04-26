number=0
drinklist=[]
dollors=input("小明身上有幾元:")
drink=int(input("販賣機上有幾種飲料:"))
for i in range(drink):
    price=int(input("依序每種飲料的價格:"))
    drinklist.append(price)
    if drinklist[price]<=dollors:
        number+1
print(number)