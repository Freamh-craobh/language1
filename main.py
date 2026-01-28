import random, function, io

#values = [function.random_call(1, 10) for i in range(500)]
#print(values)

#set up consonant and vowel lists
test = False
consonants = []
vowels = []

with open("consonants.txt", "r") as f:
    for i,line in enumerate(f.readlines()):
        if i > 0:
            consonants += [i for i in line if i != ","]
        
with open("vowels.txt", "r") as f:
    for i,line in enumerate(f.readlines()):
        if i > 0:
            vowels += [i for i in line if i != ","]
            try:
                vowels.remove("\n")
            except:
                continue

print(vowels)
with open("input.txt","r") as f:
    if test:
        for i,line in enumerate(f.readlines()):
            if i < 1:
                raw_input = line
    else: 
        raw_input = f.read().replace("-","")

#print(input.replace("\n",""))
wordlist_unclean = raw_input.replace("\n","").strip().split(sep=" ")

wordlist = list(dict.fromkeys(wordlist_unclean))

output = []

violations = {}


print(wordlist)


for word in wordlist:
    for i, char in enumerate(word):
        if char in vowels:
            continue
        elif char in consonants:
            try:
                if word[(i+1)] in vowels or word[(i+1)] == "h":
                    continue
                else:
                    #if char == "h":
                    #    continue
                        #print(f"{word[i-1]}{char} in {word} interal CV violation")
                    #else: 
                        #print(f"{char} in {word} interal CV violation")
                    if word not in violations:
                        violations[word] = []
                    violations[word] += [i]
            except:
                if char == "h":
                        continue
                        #print(f"{word[i-1]}{char} in {word} final consonant")
                else:
                    #print(f"{char} in {word} final consonant")
                    if word not in violations:
                        violations[word] = []
                    violations[word] += [i]
        else:
            print(f"{char} in {word} character error")
            raise Exception("Glyph not recognised, add to consonant/vowel list")

        #print(violations)    



for key, positions in violations.items():
    #print(key, positions)
    replaced = key
    for pos in sorted(positions, reverse=True):
        replaced = replaced[:pos+1] + function.random_vowel() + replaced[pos+1:]
    print(f"{key:<15} ->\t {replaced:<20}")
    output.append(replaced)

print(output)
with open("output.txt", "w") as f:
    f.writelines(line + "\n" for line in output)
