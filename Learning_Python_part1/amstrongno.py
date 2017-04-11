

no =int(input("enter a no: "))
sum =0
temp = no
while temp >0:
   n=temp % 10
   sum+=n ** 3
   temp//=10


if no == sum:
    print("amstrong")
else:
    print("not amstrong")
    
