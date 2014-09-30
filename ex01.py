import random
def guessGame():
    name = raw_input("Hi! What's your name?")
    print "Hi %s, thanks for playing our guessing game. " % name

    number = random.randrange(1, 101)
    count = 1
   
    while True:
        guess = input("I am thinking of a number between 1 and 100. What do you think it is?")
        if guess > number:
            print "Your guess is too high, try again!"
            count = count + 1
        elif guess < number:
            print "Your guess is too low, try again!"
            count = count + 1
        else:
            print "Congratulations! You got it right! It took you", count, "times!"
            break

guessGame()