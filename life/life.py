import random
global PROBABILITY
PROBABILITY = 100000


def check() -> bool:
    if random.randint(1, PROBABILITY) == PROBABILITY:
        return True
    return False


def get_a_life():
    global PROBABILITY
    PROBABILITY -= 1
