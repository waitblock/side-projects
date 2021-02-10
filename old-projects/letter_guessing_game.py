loop=0
letter='e'
while loop==0:
    letter_guess = (raw_input("\nEnter a letter guess: "))
    if letter_guess==letter:
        print "You guessed the letter!"
        loop=1
    if letter_guess!=letter:
        print "Try again!"
