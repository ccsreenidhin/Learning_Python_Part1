str=raw_input("enter the line: ")

tmem=len(str)
i=tmem-1
print(tmem)
while i!=0:
    if str[i] == ' ':
        tmem-=1
    i-=1

print("no of letters: %d", tmem)
