acount={}
num=int(input("輸入n值:"))
for i in range(num):
    name=str(input("請輸入姓名"))
    mail=str(input("請輸入電子郵件"))
    acount[name]=mail
search=input("輸入要查詢電子郵件的姓名:")
print(search,"電子郵件帳號為",acount.get(search))