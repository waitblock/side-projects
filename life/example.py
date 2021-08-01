import life, time


while True:
    life.get_a_life()
    time.sleep(0.00001)
    if life.check() is True:
        print(f"You got a life after sleeping {100000-life.PROBABILITY} times!")
        break
    else:
        print(f"You didn't get a life, but the probability of you getting one is now 1/{life.PROBABILITY}")
