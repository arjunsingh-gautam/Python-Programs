# Title: Number guessing game:

import random # Module used to generate a random no.
rand = random.randint(1, 100)  # Generates a random integer between 1 and 100 (inclusive)
attempt=1 # Store number of attempts
guess=None # Store the guess value
print("\033[31mWelcome to the Guessing Game!\033[0m")  # Red color

# Instructions of game:
print("\033[33mEnter an integer between 1-100\033[0m")
print("\033[33mYou get maximum 10 attempts\033[0m")
print("\033[33mPress 0 to exit the game.\033[0m")
while(attempt<11):
    guess=int(input("Enter a no. between 1-100 as your guess:")) 
    if(1<guess<100):
        if(guess==0):
            print("\033[31mThanks for playing the game!\033[0m")
            break
        else:
            if(guess==rand):
                print(f"\033[32mYour guess {guess} is correct and guessed in {attempt} attempts\033[0m")
                break
            elif(guess>rand):
                print("\033[34mYou have guessed a bigger number pls guess again\033[0m")
                attempt+=1
                continue
            elif(guess<rand):
                print("\033[34mYou have guessed a smaller number pls guess again\033[0m")
                attempt+=1
                continue
    else:
        print("\033[37mEnter number between 1-100 next time!\033[0m")
        attempt +=1
        continue
    
if(attempt>10):
    print("\033[31mThanks for playing the game your attempts are over!\033[0m")


