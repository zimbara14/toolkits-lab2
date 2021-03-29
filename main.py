import random

x = random.randint(1, 100)
print("You have 5 chances to guess the number between 1 and 100.")

count = 0
flag = None

while count < 5:
    guess = int(input("Your guess: "))
    if count == 3:
        print("Warning! One more guess left.")
    if count == 4 and x is not guess:
        print("Oops! Game over. The number you failed to guess was: " + str(x) + ".")
        flag = False
        break
    if x == guess:
        print("Congratulations! You guessed the number, and it's: " + str(guess) + ".")
        flag = True
        break
    if count < 1:
        if guess < x:
            print("Try with a number bigger than " + str(guess) + ".")
        else:
            print("Try with a number smaller than " + str(guess) + ".")
    elif 1 <= count <= 2:
        g1 = None
        g2 = None
        if x % 10 != 0:
            temp = x % 10
            g1 = x - temp
            g2 = g1 + 10
        else:
            if x != 100:
                g1 = x
                g2 = x + 10
            else:
                g1 = 90
                g2 = 100
        print("Try with a number between " + str(g1) + " and " + str(g2) + ".")
    else:
        g1 = None
        g2 = None
        if x % 10 != 0:
            temp = x % 10
            g1 = x - temp
            g2 = g1 + 10
        else:
            if x != 100:
                g1 = x
                g2 = x + 10
            else:
                g1 = 90
                g2 = 100
        temp2 = (g1 + g2) // 2
        if guess >= temp2:
            print("Try with a number between " + str(g1) + " and " + str(temp2) + " (including).")
        else:
            print("Try with a number between " + str(temp2) + " and " + str(g2) + ".")
    count += 1


def result():
    return flag
