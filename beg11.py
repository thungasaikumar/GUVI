x=input()
y=int(0)
if x.isalpha():
    print("Invaild")
else:
    ck=int(x)
    while ck!=int(0):
        z=int(ck%10)
        y=y*10+(z)
        ck=int(ck/10)
    if y==int(x):
        print("yes")
    else:
        print("no")
