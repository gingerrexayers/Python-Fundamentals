import random
heads = 0
tails = 0
flip = ""

for i in range(1, 5001):
    coin = round(random.random())
    if coin == 1:
        heads += 1
        flip = "heads"
    else:
        tails += 1
        flip = "tails"
    print "Attempt #" + str(i) + ": Throwing a coin... It's " + flip + "! ... Got " + str(heads) + " heads and " + str(tails) +  " tails so far"
