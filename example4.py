x = range(1, 1001)
y = []
while 1:
    try:
        textInput = raw_input('enter a number: ')
        number = int(textInput)
        break
    except ValueError:
        print 'Not a number try again.'
for item in x:
    if (item % number) == 0:
        y.append(item)
print y
