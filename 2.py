a = int(input("請輸入度數"))
if a<120:
    b = a*2.10
    c = a*2.10
    print("Summer months:%.2f"%b)
    print("Non-Summer months:%.2f"%c)
elif a<=330 and a>120:
    b = (120*2.10)+((a-120)*3.02)
    c = (120*2.10)+((a-120)*2.68)
    print("夏月:%.2f"%b)
    print("Non-Summer months:%.2f"%c)
elif a<=500 and a>331:
    b = (120*2.10)+(210*3.02)+((a-330)*4.39)
    c = (120*2.10)+(210*2.68)+((a-330)*3.61)
    print("Summer months:%.2f"%b)
    print("Non-Summer months:%.2f"%c)
elif a<=700 and a>501:
    b = (120*2.10)+(210*3.02)+(170*4.39)+((a-500)*4.97)
    c = (120*2.10)+(210*2.68)+(170*3.61)+((a-500)*4.01)
    print("Summer months:%.2f"%b)
    print("Non-Summer months:%.2f"%c)
elif a>700:
    b = (120*2.10)+(210*3.02)+(170*4.39)+(200*4.97)+((a-700)*5.63)
    c = (120*2.10)+(210*2.68)+(170*3.61)+(200*4.01)+((a-700)*4.50)
    print("Summer months:%.2f"%b)
    print("Non-Summer months:%.2f"%c)