a = 'rat','ox','tiger','rabbit','dragon','snake','horse','sheep','monkey','rooster','dog','pig'
y = int(input("請輸入你的出生西元年："))
print("{} {}".format(y,a[(y-2020) % 12]))