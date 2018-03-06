# pylint: disable=print-statement

def RandomCoin(): # heads =1 and tails = 0
    headscount = 0
    tailscount = 0
    for toss in range(1,5001):
        import random
        cointoss = round(random.random())
        if cointoss == 1:
            headscount += 1
            print "Attempt #" + str(toss) + ": " + "Throwing a coin...It's a head! ... Got " + str(headscount) + " heads(s) so far and " + str(tailscount) + " tails(s) so far" 
        if cointoss == 0:
            tailscount += 1
            print "Attempt #" + str(toss) + ": " + "Throwing a coin...It's a tail! ... Got " + str(headscount) + " head(s) so far and " + str(tailscount) + " tail(s) so far"
    print "Ending Program, thank you!"
RandomCoin()