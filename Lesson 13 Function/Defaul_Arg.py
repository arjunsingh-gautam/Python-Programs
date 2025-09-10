def Add(a,b,c=0): # non default args cannot be followed by default args---> very imp while defining functions i.e Add(a,c=0,b)--> will generate error
    d=a+b+c
    return d

print("Sum is:",Add(3,4)) # Here default argument is used since no arg is passed for c while calling it.
print("Sum is:",Add(3,43,2))

# This default argument functionality not available in C lang
