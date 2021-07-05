from random import randint
import emoji
from time import sleep
rsp =  (emoji.emojize(':new_moon:'), (emoji.emojize(':page_facing_up:')), (emoji.emojize(':scissors:')))
pc = randint(0,2)
print('[options]')
print(emoji.emojize('[ 0 ]:new_moon:'))
print(emoji.emojize('[ 1 ]:page_facing_up:'))
print(emoji.emojize('[ 2 ]:scissors:'))
player = int(input('choice one: '))