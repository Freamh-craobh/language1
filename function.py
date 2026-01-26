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

def vowel_selection():
    vowel_rates = {}
    with open("vowels.txt", "r") as f:
        for i,line in enumerate(f.readlines()):
         if i > 0:
            vowel_rates[i] = line.strip()
        return vowel_rates

vowel_init = vowel_selection()

def weights(vowel_rates=vowel_init):
    total = 0
    limits = []
    for i in vowel_rates:
        limits.append(total + int((1/i)*100))
        total += int((1/i)*100)
    
    rand_limit = random_call(0, total)
    #print(limits, rand_limit)
    for i in range(len(limits)):
        if rand_limit < limits[i]:
            return i+1 # THIS SHOULD BE DONE
   
def random_vowel():
    v_options = vowel_init[weights()].split(",")
    num_vowels = len(v_options)
    vowel_selection = random_call(0, num_vowels+1)
    return v_options[vowel_selection-1]


    

def dict_lister(self, addition, list_item):
    if addition not in self:
        self[addition] = []
    self[addition] = [list_item]
    