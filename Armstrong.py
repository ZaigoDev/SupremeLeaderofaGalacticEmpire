n = int(input("I am magic box, enter a number and I will check if it is an Armstrong's number.-  "))
p=q=n
cnt=0
while q>0:
    q=q//10
    print(q)
    cnt+=1
print("Number of digits indentified: " , cnt)
x=0
while p>0:
    d=p%10
    p=p//10
    x+=d**cnt
if x==n:
    print("It's an armstrong number sir")
else:
    print("It's not a armstrong number ma'am")