a=int(input())
b=a//2+1
for i in range(b):
    print((b-i)*" "+(2*i+1)*"*")
for j in range(b):
    print(" "*(j+2)+"*"*((a-2)-(2*j)))