#Find the number from player mind
import random
secret_number = random.randint(1,20) # Ask the  player to think number between 1 to 20
for guessTaken in range(1,4):
    print('Guess the number: ') # only 3 guesses are allowed
    guess = int(input())
    if guess > secret_number:
        print('Guess is too high')
    elif guess < secret_number:
        print('Guess is too low')
    else:
        break # For the right guess
if guess == secret_number:
    print(f"Hurrah! you found the correct number")
else:
    print(f"OOPs..you are out of shorts.The correct number is {str(guess)}")