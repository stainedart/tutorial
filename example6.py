while 1:
    textInput = raw_input('enter a word: ')
    i = 0

    while i < len(textInput):
        # print "first " + textInput[i]
        # print "last " + textInput[-1 * (i + 1)]
        if textInput[i] == textInput[-1 * (i + 1)]:
            i = i + 1
            if i == len(textInput):
                print "this is a palindrome"
        else:
            print "not a palindrome"
            break
