full=250
half=175
n=int(input("組數為"))
for i in range(n):
    com=input("第"+str(i+1)+"組(以空白間隔開)：")
    comp=com.split()
    print("第"+str(i+1)+"組應收費用:",(int(comp[0])*250)+(int(comp[1])*175),"元")
