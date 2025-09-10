s1="Arjun"
print(len(s1))
print(min(s1))
print(max(s1))
print(sorted(s1,reverse=True)) # sorted(s1) return a sorted list

"""print(min(s1)):
This prints the minimum character in the string "Arjun" based on their ASCII values.
ASCII values: 'A' is 65, 'r' is 114, 'j' is 106, 'u' is 117, 'n' is 110.
The minimum ASCII value is for 'A', so it prints 'A'.

print(max(s1)):
This prints the maximum character in the string "Arjun" based on their ASCII values.
ASCII values: 'A' is 65, 'r' is 114, 'j' is 106, 'u' is 117, 'n' is 110.
The maximum ASCII value is for 'u', so it prints 'u'.

print(sorted(s1)):
This prints a sorted list of characters from the string "Arjun" based on their ASCII values.
ASCII values: 'A' is 65, 'r' is 114, 'j' is 106, 'u' is 117, 'n' is 110.
The sorted list is ['A', 'j', 'n', 'r', 'u']"""
# sum()
s2="1234"
#print(sum(s2))  # gives error
print(sum([int(e) for e in s2])) # list comprehension can be applied

s3="1a2b3c4"
print(sum([int(e) for e in s3 if ord(e)>=49 and ord(e)<=57]))