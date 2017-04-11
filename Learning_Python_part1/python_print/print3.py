var1 = "just print this %r"     #%r displays the raw data used for debugging usually
var2 = False
var3 = "line"
var4 = "just print this %s" 

print var1 %var2
print var1+var3


print var3*3
print var3*var2 #prints empty line
print var3*True #prints once

#print var1*var3 #error:TypeError: can't multiply sequence by non-int of type 'str'

print var1 % var1
print var4 % var4

print"""

twinkle twinkle.............
.
.
.


"""
