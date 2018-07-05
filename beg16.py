x=input()
y=input()
count=0
if x.isalpha() or y.isalpha():
    print("Invaild")
else:
    x=int(x)
    y=int(y)
    for i in range((x+1),y):
        for a in range(2,i):
            if i%a==0:
                count=1
        if count==0:
            print(i,end=' ')
        count=0
