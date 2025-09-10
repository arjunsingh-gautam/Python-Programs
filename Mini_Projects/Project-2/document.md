# <span style="color:orange">Number Guessing Game</span>

## <span style="color:pink">Introduction</span>

The **Number Guessing Game** is a simple Python program where the user tries to guess a randomly generated number between **1 and 100**. The user gets a maximum of **10 attempts** to guess the correct number. The program provides hints if the guess is too high or too low and allows the user to exit anytime by entering **0**.

## <span style="color:pink">Features</span>

- Random number generation between **1 and 100**.
- **10 attempts limit** for guessing the correct number.
- **Hints provided** if the guessed number is too high or too low.
- **Exit option** by entering **0**.
- Uses **colorful output** for better readability.

## <span style="color:pink">Requirements</span>

- Python 3.x

## <span style="color:pink">Modules Used</span>

```python
import random
```

- **random**: Used to generate a random integer between **1 and 100**.

## <span style="color:pink">How It Works</span>

1. The program generates a **random number** between **1 and 100**.
2. The player is prompted to **enter a number** as their guess.
3. If the guess is **correct**, the program congratulates the player and displays the number of attempts taken.
4. If the guess is **incorrect**, the program provides hints:
   - If the guess is **too high**, it suggests guessing a **smaller number**.
   - If the guess is **too low**, it suggests guessing a **larger number**.
5. If the player enters **0**, the game exits with a goodbye message.
6. If the player **exceeds 10 attempts**, the game ends automatically.

## <span style="color:pink">Game Instructions</span>

- **Enter an integer between 1-100.**
- **You get a maximum of 10 attempts.**
- **Press 0 to exit the game.**

## <span style="color:pink">Code Explanation</span>

### <span style="color:yellow">1. Generating a Random Number</span>

```python
rand = random.randint(1, 100)
```

- This line generates a random integer between **1 and 100**.

### <span style="color:yellow">2. Main Game Loop</span>

```python
while(attempt < 11):
    guess = int(input("Enter a no. between 1-100 as your guess:"))
```

- The loop runs until the player **guesses the correct number** or **attempts exceed 10**.

### <span style="color:yellow">3. Checking the User Input</span>

```python
if(1 < guess < 100):
```

- Ensures that the user enters a valid number **between 1 and 100**.

### <span style="color:yellow">4. Handling Exit Condition</span>

```python
if(guess == 0):
    print("\033[31mThanks for playing the game!\033[0m")
    break
```

- If the player enters **0**, the game **exits immediately**.

### <span style="color:yellow">5. Checking Guess Accuracy</span>

- If the guess is **correct**, the program displays a success message.
- If the guess is **too high or too low**, hints are provided.

```python
if(guess == rand):
    print(f"\033[32mYour guess {guess} is correct and guessed in {attempt} attempts\033[0m")
    break
elif(guess > rand):
    print("\033[34mYou have guessed a bigger number pls guess again\033[0m")
    attempt += 1
elif(guess < rand):
    print("\033[34mYou have guessed a smaller number pls guess again\033[0m")
    attempt += 1
```

### <span style="color:yellow">6. Handling Invalid Inputs</span>

```python
else:
    print("\033[37mEnter number between 1-100 next time!\033[0m")
    attempt +=1
```

- If the player enters a number **outside the valid range**, an error message is displayed, and the attempt count is increased.

### <span style="color:yellow">7. Ending the Game When Attempts are Over</span>

```python
if(attempt > 10):
    print("\033[31mThanks for playing the game, your attempts are over!\033[0m")
```

- If the player **uses all 10 attempts**, the game **ends automatically**.

## <span style="color:pink">Example Gameplay</span>

```
Welcome to the Guessing Game!
Enter an integer between 1-100
You get a maximum of 10 attempts
Press 0 to exit the game.

Enter a number between 1-100 as your guess: 50
You have guessed a bigger number, please guess again.

Enter a number between 1-100 as your guess: 25
You have guessed a smaller number, please guess again.

Enter a number between 1-100 as your guess: 38
Your guess 38 is correct and guessed in 3 attempts!
```

## <span style="color:pink">Possible Enhancements</span>

- **Add difficulty levels** (easy, medium, hard) with different attempt limits.
- **Track highest scores** to record the best performance.
- **Use graphical interface** using Tkinter or PyGame.
- **Allow multiple rounds** instead of a single game session.

## <span style="color:pink">Conclusion</span>

This **Number Guessing Game** is a great beginner-friendly project to practice control statements, loops, and user input handling in Python. By adding more features, it can become even more engaging!

---

**Happy Coding! 🎯**
