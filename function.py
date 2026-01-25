import random

rand_seed = 0

def random_call(min, max):
    """
    calls the random number between two values, 
    fixed seed so produces the same results every time, order dependant
    seed is incremented every use, only on use

    :param min: min value int
    :param max: max value int excluding this value
    """
    global rand_seed
    random.seed(rand_seed)
    rand_seed += 1
    return random.randrange(min, max)
