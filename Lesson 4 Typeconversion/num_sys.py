x=25
y=bin(x) #bin():convert integer to binary
z=oct(x) #oct():convert integer to octal
q=hex(x) #hex():convert integer to hexadecimal
print(x,y,z,q,sep=' ,')

a=0b1100101
b=0o35
c=0xef
print(a,b,c,sep=' ,') # give integer output 

l='A'
print(ord(l))
m=65
print(chr(m))
# The ord() function returns the Unicode code point of a given character.
# It takes a single character (a string of length 1) as an argument and returns an integer.
# For example, ord('A') returns 65, which is the Unicode code point for the capital letter 'A'.

# The chr() function returns a character string from a given Unicode code point.
# It takes an integer representing a Unicode code point as an argument and returns the corresponding character.
# For example, chr(65) returns 'A', as 65 is the Unicode code point for 'A'.
