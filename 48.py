animal={}
num=int(input("輸入筆數:"))
for i in range(num):
    english=str(input())
    chiness=str(input())
    animal[english]=chiness
search=input("輸入欲查詢單字:")
print(search,"的中文意思為",animal.get(search))