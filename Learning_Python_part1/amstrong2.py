no =raw_input("enter a no: ")

sum =0
for i in no:
    sum += int(i) ** 3

print(sum)    
if int(no) == sum:
    print("amstrong")
else:
    print("not amstrong")
    
