str1 = raw_input("enter string: ")
str2 = reversed(str1)
if list(str1) == list(str2) :
    print("palindrome")
else:
    print("not palindrome")
