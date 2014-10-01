import random

name = raw_input("Hi! What's your name?")
print "Hi %s, thanks for playing our guessing game. " % name

def guessGame():

    number = random.randrange(1, 101)
    count_current = 1
    count_best = 1000

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
                count_current = count_current + 1
            elif guess < number:
                print "Your guess is too low, try again!"
                count_current = count_current + 1
            else:
                print "Congratulations! You got it right! It took you", count_current, "times!"
                if count_current < count_best:
                    print "You have a new high score of", count_current
                    count_current == count_best
                elif count_current == count_best:
                    print "You matched your high score of", count_best, ". Keep playing!"
                else: 
                    print "The current high score is", count_best 
                playAgain = raw_input("Do you want to play again? Y or N")
                if playAgain == "Y":
                    guessGame()
                else:
                    print "Thanks for playing! We hope you come back."
                    break

guessGame()