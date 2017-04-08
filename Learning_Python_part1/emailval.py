str = raw_input("enter email: ")
length = len(str)-1
i=len(str)-1
z = 0;
print(i)
if i != 0 :
    while i > 0:
        if str[i] == '@':
            break;
        i-=1
    print(i)
    if i > 0:
        while i < length:
            if str[i] == '.':
                break;
            i+=1
    print(i)
if i != 0 and i < length:
    print("valid")
else :
    print("invalid")
