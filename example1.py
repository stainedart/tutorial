import sys

while 1:
    name = raw_input('what is your name? ')
    if name == 'exit':
        sys.exit()
    while 1:
        try: 
            age = float(raw_input('how old are you? '))
            break
        except ValueError:
            print('That''s not your age try again!')

    oldAge = 100 - age

    if oldAge < 0:
        print('Dam %s you are already old!' % name)
    else:
        print 'Hi %s you will be 100 in %d but currently you are %d enjoy!!' % (name, oldAge, age)
