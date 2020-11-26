import random, string
from collections import deque

def main():
    suit_size = 10
    suits = 2
    deck = shuffle(suit_size, suits)

    deck = [1, 2, 10, 15, 19, 13, 3, 7, 'B', 6, 'A', 8, 14, 12, 16, 5, 4, 17, 20, 9, 18, 11]
 
    print(deck)
    
    plain = 'cupidshuffle'
    cipher = encrypt(deck, plain)
    print(cipher)

def encrypt(deck, plain):

    plain = plain.lower()

    cipher = ''
    a = ''
    key = ''
    key_nums = ''

    for letter in plain: # might run into issues here w 0 indexing
        if letter in string.punctuation or letter in string.whitespace:
            pass
        else:
            num = ord(letter) - 97
            deck, keystream_val = keystream(deck)
            key += chr(keystream_val + 97)
            key_nums += ' ' + str(keystream_val)
            new_num = (num + keystream_val) % 26
            cipher += chr(new_num + 97)
            a += letter

    print(key)
    print(key_nums)
    return cipher

def keystream(deck):
    a_loc = deck.index('A')
    deck = shift(deck, a_loc, 1)
    b_loc = deck.index('B')
    deck = shift(deck, b_loc, 2)

    a_loc = deck.index('A')
    b_loc = deck.index('B')

    low_joker = a_loc if a_loc < b_loc else b_loc
    high_joker = a_loc if a_loc > b_loc else b_loc

    deck = triple_cut(deck, low_joker, high_joker)
    deck = count_cut(deck)

    top = deck[0]
    if top in ['A', 'B']:
        top = len(deck) + 2

    result = deck[top % len(deck)]
    if result in ['A', 'B']:
        deck, result = keystream(deck)

    return deck, result


def count_cut(deck):
    count = deck[-1]
    if count in ['A', 'B']:
        count = len(deck)

    cut = deck[:count]
    rest = deck[count:-1]

    return rest + cut + [deck[-1]]


def triple_cut(deck, low_joker, high_joker):
    left = deck[:low_joker]
    middle = deck[low_joker:high_joker + 1]
    right = deck[high_joker + 1:]

    return right + middle + left


def shift(deck, index, spaces): # I just realized I could use list slices here :(
    value = deck[index]
    new_index = (index + spaces) % len(deck)
    wrap = new_index < index

    if new_index == 0: new_index += 1

    if wrap:
        for i in range(index - new_index):
            deck[index - i] = deck[index - i - 1]
    else:
        for i in range(new_index - index):
            deck[index + i] = deck[index + i + 1]
    deck[new_index] = value

    return deck


def shuffle(suit_size, suits):
    deck = [i for i in range(1, suit_size * suits + 1)]
    deck.extend(['A', 'B'])
    random.shuffle(deck)
    
    return deck

main()
