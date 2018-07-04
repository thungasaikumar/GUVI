a=input()
b=input()
c=input()
if a.isalpha() or b.isalpha() or c.isalpha():
    print("Invalid")
else:
    a=int(a)
    b=int(b)
    c=int(c)
    if a>=b and a>=c:
        print(a)
    elif b>=a and b>=c:
        print(b)
    elif c>=a and c>=b:
        print(c)
