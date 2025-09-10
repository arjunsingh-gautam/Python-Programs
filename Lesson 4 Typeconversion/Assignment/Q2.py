# Write a python script to print Unicode of the character 'm'
ch='m'
print(ord(ch))

# Write a python script to print to given unicode
a=100
print(chr(a))

# Write a python code to print any number and is binary,octal and hexadecimal equivalent
c=76
print(c,bin(c))
print(c,oct(c))
print(c,hex(c))

# Write a python script to store 1100101,2F,125 convert decimal form
b=0b1100101
h=0x2F
o=0o125
print(b,oct(h),bin(o),sep='\n')

# Write program to add 25(octal) and 39(hexadecimal) print ans in binary
o=0o25
h=0x39
add=int(o)+int(h)
print(bin(add))