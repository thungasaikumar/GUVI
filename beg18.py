x,y=input().split()
if x.isalpha():
    print("Invaild")
else:
     x=int(x)
     y=int(y)
     arm=int(0)
     for i in range(x,y):
         chk=int(i)
         arm=0

         while chk!=0:
                 z=chk%10;
                
                 arm=arm+(z**3)
                 chk=int(chk/10)

         if arm==i:
             print(i)
