import sys

while 1:
    while 1:   
        try:
            textInput = raw_input('enter a number: ')
            values = textInput.split()
            multiple = False
            if len(values) > 1:
                multiple = True
                # do multiple values logic
                num = int(values[0])
                div = int(values[1])
            else:
                number = int(textInput)
            break
        except ValueError:
            print 'Not a number try again.'
    if multiple:
        remainder = num / (div * 1.0)
        print 'remainder: %f' % remainder
        if (remainder % 1) == 0:
            print 'clean divider'
        else:
            print 'dirty divider'
    elif number == 999:
        sys.exit()
    elif (number % 4) == 0:
        print 'multiple of 4'
    elif (number % 2) == 0:
        print 'multiple of 2'
    else:
        print 'not a multiple of 2'
