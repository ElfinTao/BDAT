
# -*- encoding:UTF-8 -*-

import random

class Card:
    suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    suits.reverse()
    values = [str(n) for n in range(2,11)] + list('JQKA')

full_deck = []
for suit in Card.suits:
    for value in Card.values:
        full_deck.append(suit + ' ' + str(value))

def draw_card():
    return full_deck.pop()
draw_card()

def deal_war():
    answer = input('Press Enter To Continue, or press any key to exit...')
    while answer == "":
        Elfin = random.choice(full_deck)
        Computer = random.choice(full_deck)
        print ('Elfin_card: %s' % Elfin)
        print ('Computer_card: %s' % Computer)
        if full_deck.index(Elfin) > full_deck.index(Computer):
            print ('Elfin wins!')
        elif full_deck.index(Elfin) < full_deck.index(Computer):
            print ('Computer wins!')
        else:
            print ('WAR!')
        answer = input('Press Enter To Continue, or press any key to exit...')
deal_war()
