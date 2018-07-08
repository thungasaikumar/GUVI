x=input()
if x.isalpha():
    print("Invaild")
else:
    x=int(x)
    y=int(x)
    arm=int(0)
    while y!=0:
        z=y%10;
        arm=arm+(z**3)
        y=int(y/10)
  
    if arm==x:
        print("yes")
    else:
        print("no")
