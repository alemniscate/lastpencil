import random

def positive_input():
    while True:
        try:
            n = int(input())
            if n > 0:
                return n
            print('The number of pencils should be positive')
        except:
            print('The number of pencils should be numeric')

def human_input(n):
    while True:
        try:
            d = int(input())
            if d > 3 or d < 1:
                print("Possible values: '1', '2' or '3'")
                continue
            if d > n:
                print('Too many pencils were taken')
            else:
                return d
        except:
            print("Possible values: '1', '2' or '3'")

def bot_input(n):
    r = n % 4
    if r == 1:
        d = random.choice(range(1, min(3, n) + 1))
    else:
        d = (n + 3) % 4
    print(d)
    return d

def playername_input(players):
    while True:
        player = input()
        if player in players:
            return player
        print(f'Choose between {players[0]} and {players[1]}') 

if __name__ == '__main__':

    print('How many pencils would you like to use:')
    n = positive_input()
    players = ("John", "Jack")
    print(f'Who will be the first ({players[0]}, {players[1]}):')
    player = playername_input(players)
    c = 0 if player == players[0] else 1
    while n > 0:
        print(['|' * n][0])
        print(f"{players[c]}'s turn:")
        d = bot_input(n) if c == 1 else human_input(n)
        n -= d
        c = (c + 1) % 2
    print(f'{players[c]} won!')