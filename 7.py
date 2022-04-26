cost=input("輸入月租費形式及通話時間:")
costspe=cost.split(",")
print("通話費為:",round(int(costspe[1])*0.08*0.7))