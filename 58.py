listnum=[]
for i in range(1,11):
    inp=int(input(f"請輸入第 {i} 個數字："))
    listnum.append(inp)
listnum.sort()
listnum.reverse()
print("最大的3個數為:",listnum[0],",",listnum[1],",",listnum[2])
print("最小的3個數為:",listnum[7],",",listnum[8],",",listnum[9])