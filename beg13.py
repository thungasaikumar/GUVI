x=input()
count=0
if x.isalpha():
    print("Invaild")
elif int(x)==1:
    print("no")
else:
    x=int(x)
    for i in range(2,x):
        if x%i==0:
            count=1
    if count==1:
        print("no")
    else:
        print("yes")
