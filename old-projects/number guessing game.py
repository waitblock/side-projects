import random as r
n=int(r.randint(1, 2048))
answer='y'

while answer=='y':
        x=0
        while x==0:
                g = int(raw_input("\nGuess a number between 1 and 2048: "))
                if n == g:
                        print "you guessed it!"
                        x=1        
                if n > g:
                        print "higher"
                if n < g:
                        print "lower"
        
        answer=raw_input("\nDo you want to play again (enter y/n): ")
