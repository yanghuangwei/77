medal=[]
medalnum=[]
num=int(input("輸入筆數:"))
for i in range(num):
    m=str(input())
    n=int(input())
    medal.extend(m)
    medalnum.append(n)
for j in range(len(medalnum)):
    print("%s得到 %d 面" % (medal[j],medalnum[0]))