x=input()
y=input()
if x.isalpha() or y.isalpha():
    print("Invaild")
else:
    x=int(x)
    y=int(y)
    z=int(x)
    for i in range(y-1):
        x=x*z
    print(x)
