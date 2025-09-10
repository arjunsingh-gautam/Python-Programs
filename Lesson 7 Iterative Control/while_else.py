#In this program we are goin to see the use of 'break' keyword 
""" Write a program to ask user to enter an even number at most 3times
.If user failed to enter an even number in all the three chances
he has lost the game.if user enter an even number then no more chances
and he is winner."""

i=1
while i<4:
    num = int(input("Enter an even number : "))
    if (num %2) ==0:
        print("\nYou have won the game !!!")
        break
    i+=1
else:
    print("\nYou have lost the game.")

    

# else:Else block will when Normal life of loop ends
# It will not executed when loop end it's life due to break statement