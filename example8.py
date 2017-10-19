def player_input(playerNumber):
    p1Input = raw_input("Player %s's move: " % playerNumber)
    if p1Input == 'r' or p1Input == 'rock':
        return "r"
    elif p1Input == 'p' or p1Input == 'paper':
        return "p"
    elif p1Input == 's' or p1Input == 'scissors':
        return "s"


def print_winner(playerNumber):
    print "Player %s wins the round." % playerNumber


print "possible actions are ((r)ock, (p)aper, (s)cissors"
while 1:
    p1 = player_input("1")
    p2 = player_input("2")
    if p1 == p2:
        print "Tie game"
    elif p1 == 'r' and p2 == 's':
        print_winner("1")
    elif p1 == 'p' and p2 == 'r':
        print_winner("1")
    elif p1 == 's' and p2 == 'p':
        print_winner("1")
    else:
        print_winner("2")
    playAgain = raw_input("Play again?!")
    if playAgain == 'n' or playAgain == 'no':
        break
