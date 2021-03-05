import string
import random

possible_chars = list(string.ascii_uppercase)+list(string.ascii_lowercase)

while True:

    words = ""

    try:
        c = int(input("Enter how many words you want: "))
        for i in range(c):
            word = ""
            for j in range(random.randint(2,10)):
                word += random.choice(possible_chars)
            words = words + word + " "
        print(words)
        
    except TypeError:
        print("Enter an integer value.")
    except KeyboardInterrupt:
        break
