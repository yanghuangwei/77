for i in range(2):
    sum=input("輸入金額:")
    print("所需最少紙鈔及硬幣的量:",(int(sum)//100)+((int(sum)%100)//50)+(((int(sum)%100)%50)//10)+(((int(sum)%100)%10)//5)+((((int(sum)%100)%10)%5)//1))