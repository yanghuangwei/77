number=[["123","Tom","DTGD"],["456","cat","CSIE"],["789","Nana","ASIE"],["321","Lim","DBA"],["654","Won","FDD"]]
inp=input("輸入學號為:")
for i in range(5):
    if inp==number[i][0]:
        print("學生資料為:"+number[i][0] +number[i][1] +number[i][2])