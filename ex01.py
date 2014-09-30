import random

name = raw_input("Hi! What's your name?")
print "Hi %s, thanks for playing our guessing game. " % name

def guessGame():

    number = random.randrange(1, 101)
    count = 1
    
    while True:

        guess = raw_input("I am thinking of a number between 1 and 100. What do you think it is?")
        try:
            guess = int(guess)
        except ValueError:
            print "Please give us a real number, dummy."
        
        if type(guess) == int:
            if guess > 100 or guess < 1:
                print "Your number is not in the range!"
            elif guess > number:
                print "Your guess is too high, try again!"
                count = count + 1
            elif guess < number:
                print "Your guess is too low, try again!"
                count = count + 1
            else:
                print "Congratulations! You got it right! It took you", count, "times!"
                playAgain = raw_input("Do you want to play again? Y or N")
                if playAgain == "Y":
                    guessGame()
                else:
                    break

guessGame()