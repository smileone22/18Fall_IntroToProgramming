import random
num = random.randint(1,11)

print("I'm thinking of a number between 1 and 11.")
print()
guess = int(input("Guess my number: "))

if guess == num:
    print("You got it!")
    print()
    print('The secret number was',num,'.')
    print('It took you 1 try to guess the number.')
    
elif guess > num:
    print("Too high, try again.")
    print()
    guess2 = int(input("Guess my number: "))
    if guess2 == num:
           print("You got it!")
           print()
           print('The secret number was',num,'.')
           print('It took you 2 tries to guess the number.')
    elif guess2 > num:
            print("Too high, try again.")
            print()
            guess3 = int(input("Guess my number: "))
            if guess3 == num:
                print("You got it!")
                print()
                print('The secret number was',num,'.')
                print('It took you 3 tries to guess the number.')
            else:
                print('Sorry, game over.')
                print()
                print('The secret number was',num,'.')
    else:
        print("Too low, try agian.")
        print()
        guess3 = int(input("Guess my number: "))
        if guess3 == num:
            print("You got it!")
            print()
            print('The secret number was',num,'.')
            print('It took you 3 tries to guess the number.')
        else:
            print('Sorry, game over.')
            print()
            print('The secret number was',num,'.')
           
else:
    print("Too low, try agian.")
    print()
    guess2 = int(input("Guess my number: "))
    if guess2 == num:
        print("You got it!")
        print()
        print('The secret number was',num,'.')
        print('It took you 2 tries to guess the number.')
    elif guess2 > num:
        print("Too high, try again.")
        print()
        guess3 = int(input("Guess my number: "))
        if guess3 == num:
                print("You got it!")
                print()
                print('The secret number was',num,'.')
                print('It took you 3 tries to guess the number.')
        else:
                print('Sorry, game over.')
                print()
                print('The secret number was',num,'.')
    else:
        print("Too low, try agian.")
        print()
        guess3 = int(input("Guess my number: "))
        if guess3 == num:
            print("You got it!")
            print()
            print('The secret number was',num,'.')
            print('It took you 3 tries to guess the number.')
        else:
            print('Sorry, game over.')
            print()
            print('The secret number was',num,'.')
           



