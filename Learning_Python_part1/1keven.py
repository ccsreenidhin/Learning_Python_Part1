no=int(input("enter a no: "))
temp=0
count=0
if no>1000 and no<3000:
    while no!=0:
        count +=1
        temp=no%10
        no=no/10
        if(temp%2 != 0):
            print("digit at place %d is odd", count)
        else:
            print("digit at place %d is even", count)

else:
    print("not in range 1k to 3k")
    
