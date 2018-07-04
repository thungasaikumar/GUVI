a=input()
if a.isalpha():
    print("Invalid")
else:
    a=int(a)
    sum=0
    for i in range(a):
        sum=sum+(i+1)
    print(sum)
