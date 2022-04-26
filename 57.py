set={'1A':'127','2A':'117','3A':'137','4A':'99','5A':'115','1B':'140','2B':'130','3B':'150','4B':'112','5B':'128'}
for i in range(3):
    upgradeset=input("選擇主餐及升級的套餐:")
    larger=str(input("是否升級大杯飲料:"))
    change=str(input("是否換成大薯:"))
    if larger=="是":
        if change=="是":
            print("總共為",int(set.get(upgradeset))+7+13,"元")
        else:
            print("總共為",int(set.get(upgradeset))+7,"元")
    else:
        if change=="是":
            print("總共為",int(set.get(upgradeset))+13,"元")
        else:
            print("總共為",int(set.get(upgradeset)),"元")