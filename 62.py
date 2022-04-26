fruit={'蘋果':'紅色','香蕉':'黃色','葡萄':'紫色','藍莓':'藍色','橘子':'橘色'}
for i in range(2):
    inp=str(input("請輸入水果:"))
    print(inp+"是"+fruit.get(inp))