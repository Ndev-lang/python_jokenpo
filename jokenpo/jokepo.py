from random import randint
import emoji
from time import sleep
rsp = (emoji.emojize(':new_moon:'), (emoji.emojize(':page_facing_up:')), (emoji.emojize(':scissors:')))
pc = randint(0, 2)
print('[options]')
print(emoji.emojize('[ 0 ]:new_moon:'))
print(emoji.emojize('[ 1 ]:page_facing_up:'))
print(emoji.emojize('[ 2 ]:scissors:'))
player = int(input('choice one: '))
sleep(1)
print('jo')
sleep(1)
print('ken')
sleep(1)
print('po')
sleep(1)
print('-=' * 10)
print('the pc choice {}'.format(rsp[pc]))
print('player choice {}'.format(rsp[player]))
print('-=' * 10)
if pc == 0:#rock
    if player == 0:
        print('a tie')
    elif player == 1:
        print('player wins')
    elif player == 2:
        print('player lose')
    else:
        print('invalid option')

elif pc == 1:#paper
    if player == 0:
        print('player lose')
    elif player == 1:
        print('a tie')
    elif player == 2:
        print('player wins')

    else:
        print('invalid option')

elif pc == 2:#scissors
    if player == 0:
        print('player wins')
    elif player == 1:
        print('player lose')
    elif player == 2:
        print('a tie')
    else:
        print('invalid option')
