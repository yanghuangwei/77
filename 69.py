num={"-----":"0",".----":"1","..---":"2","...--":"3","....-":"4",".....":"5","-....":"6","--...":"7","---..":"8","----.":"9"}
inp=input("輸入摩斯密碼:")
sep=inp.split()
for k in sep:
    store=num.get(k)
    print(store,end='')