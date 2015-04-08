import random

#greet player
print "Hello player number 1!"

#get player name
print "What is your name?"
name = raw_input()

#print name

#choose random number between 1 and 100
rando = random.randint(0, 101)
#print rando

print"Please guess a number between one and one hundred."
#While True
    #get guess
    #if guess is incorrect:
        #give hint
    #else:
        #congratulate player
#guess != rando:

#guess = raw_input()
#guess_int = int(guess)
#print guess_int
#print type(guess_int)


while rando == rando:
    guess = raw_input()
    guess_int = int(guess)

    if guess_int > rando:
        print "%r is too high! Guess again!" % guess
        continue
    if guess_int < rando:
        print "%r is too Low! Guess again!" % guess
        continue
    else: 
        print "Congradulations, %r" % name
        rando = False
        break