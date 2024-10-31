
import random as r

print("Guess a number between 1 and 100.")

a = -1
guesses = 0
n = r.randint(1, 100) 

while a != n:
    guesses += 1
    a = int(input("Guess the number: "))
    
    if a > n:
        print("Lower the number, please.")
    elif a < n:
        print("Higher number, please.")
    else:
        print(f"You guessed the number correctly in {guesses} attempts!")
