a=int(input("輸入係數a:"))
b=int(input("輸入係數b:"))
c=int(input("輸入係數c:"))
ans=0
if b**2-(4*a*c)>0:
    print(((-b+(b**2-(4*a*c))**0.5))/2*a,((-b-(b**2-(4*a*c))**0.5))/2*a)
elif b**2-(4*a*c)==0:
    print(-b/(2*a))
else:
    print("0")
    