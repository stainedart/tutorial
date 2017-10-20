from random import randint

a = randint(1, 9)
again = "yes"
while again == 'yes' or again=='y':
    guesses = 1
    while 1:
        while 1:
            try:
                userValue = int(raw_input('Enter number'))
                break
            except ValueError:
                print 'Not a number try again.'
        if userValue == a:
            print "Good guess!!"
            break
        elif userValue > a:
            print "Too big"
        elif userValue < a:
            print "Too small"
        guesses = guesses + 1
    print "%d guesses" % guesses
    again = raw_input("Again?")
