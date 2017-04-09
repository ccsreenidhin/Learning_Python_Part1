no=int(input("enter phone no: "))
temp =no

count=0
while no !=0:
    no/=10
    count+=1

if count==10:
    temp/=1000000000
    if temp == 8 or temp == 9 or temp == 7:
        print("valid")

else:
    print("invalid")

# if len(no) == 11:
    
    
