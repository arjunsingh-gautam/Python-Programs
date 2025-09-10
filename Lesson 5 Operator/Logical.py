# Logical operator

#1 not
print(not 3>4)

#2 and
print( 4>3 and 5>4)
#print(4>0 and 5/0) -> error
print(4<3 and 5/0) #-> False
print("Seeta" and "Geeta")
# wo evaluate honga jispar 'and; ka ans depend kar raha ho 
# yaha and  ka ans Geeta pe depend kar raha hai seeta-->t  and geeta-->t ==> t and t/f -->t/f


#3 or
print(4>2 or 5<4)
print("Seeta" or "Geeta") # when operands are non bool then evaluation also non bool
# wo evaluate honga jispar 'or; ka ans depend kar raha ho 
# yaha or ka ans Seeta pe depend kar raha hai seeta-->t ==> t or X -->t

