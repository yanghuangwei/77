mom=['a','e','i','o','u']
dot=""
inp=input("請輸入一串小寫英文:")
for i in inp:
    if i in mom:
        dot+="."
    else:
        dot+=i
print(dot)