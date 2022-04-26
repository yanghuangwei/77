number=[["123","456","9000"],["456","789","5000"],["789","888","6000"],["775","666","12000"],["566","221","7000"]]
a=int(input("輸入查詢組數N為:"))
for i in range(a):
    act=input("帳:")
    num=input("密:")
    if act==number[i][0] and num==number[i][1]:
        print(number[i][2])
    else:
        print("error")
