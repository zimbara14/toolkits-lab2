import random

x = random.randint(1, 100)
print("You have 5 chances to guess the number between 1 and 100.")

count = 0

while count < 5:
    guess = int(input("Your guess: "))
    if count == 3:
        print("Warning! One more guess left.")
    if count == 4 and x is not guess:
        print("Oops! Game over. The number you failed to guess was: " + str(x))
    if x == guess:
        print("Congratulations! You guessed the number, and it's: " + str(guess))
        break
    if guess < x:
        print("Try with a number bigger than " + str(guess))
    if guess > x:
        print("Try with a number smaller than " + str(guess))
    count += 1
