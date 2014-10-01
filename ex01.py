import random   #imports random module

name = raw_input("Hi! What's your name?")   #ask user for name
print "Hi %s, thanks for playing our guessing game. " % name    #greets user by name

def guessGame(): #defines function that will run guessing game

    number = random.randrange(1, 3)  #generates a random number for user to guess
    count_current = 1 #starts the count of guesses at 1
    count_best = 1000 #defines best count as 1,000 so that it will be more than count_current for 
                      #first guess

    while True: #starts a while loop that will run while the condition is true

        guess = raw_input("I am thinking of a number between 1 and 100. What do you think it is?") 
        #asks user to pick a number and assigns that number to variable guess
        try: #begin of try except block which will allow program to run a certain way during a ValueError
            guess = int(guess) #turns variable guess into an integer
        except ValueError:
            print "Please give us a real number, dummy." 
            #prints message to user if they don't enter an int
        
        if type(guess) == int: # starts if else statement if the type of the guess is an integer
            if guess > 100 or guess < 1: #checks if the guess is in range between 1 and 100
                print "Your number is not in the range!"
                count_current = count_current + 1
            elif guess > number: # if they guess too high prints that they guess too high and adds a count 
                                 # for the guesses
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