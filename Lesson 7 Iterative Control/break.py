#In this program we are goin to see the use of 'break' keyword 
""" Write a program to ask user to enter an even number at most 3times
.If user failed to enter an even number in all the three chances
he has lost the game.if user enter an even number then no more chances
and he is winner."""

i=1
while i<4:
    num = int(input("Enter an even number : "))
    if (num %2) ==0:
        break
    i+=1
if i==4:
    print("\nYou have lost the game.")
else:
    print("\nYou have won the game !!!")

# Using 'break' statement to exit a loop prematurely
# It terminates the loop immediately when a specific condition is met