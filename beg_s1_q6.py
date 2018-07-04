a=input()
if a.isalpha():
    print("Invalid")
else:
    a=int(a)
    if a%4==0:
        print("Yes")
    else:
        print("No")
