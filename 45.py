from re import S


month=int(input("輸入月份:"))
day=int(input("輸入日期:"))
s=(month*2+day)%3
if 0<=s<1:
    print("普通")
elif 1<=s<2:
    print("吉")
else:
    print("大吉")