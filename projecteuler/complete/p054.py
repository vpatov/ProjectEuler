"""
 https://projecteuler.net/problem=54
 Poker hands

 In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way: 
 High Card : Highest value card. 
 One Pair : Two cards of the same value. 
 Two Pairs : Two different pairs. 
 Three of a Kind : Three cards of the same value. 
 Straight : All cards are consecutive values. 
 Flush : All cards of the same suit. \
 Full House : Three of a kind and a pair. 
 Four of a Kind : Four cards of the same value. 
 Straight Flush : All cards are consecutive values of same suit. 
 Royal Flush : Ten, Jack, Queen, King, Ace, in same suit. 

 The cards are valued in the order: 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace. 
 If two players have the same ranked hands then the rank made up of the highest value wins; for example, a 
 pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a 
 pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie
 then the next highest cards are compared, and so on. 

 Consider the following five hands dealt to two players: 
 
        Player 1                                          Player 2                                          Winner 
5H 5C 6S 7S KD Pair of Fives                          2C 3S 8S 8D TD  Pair of Eights                      Player 2 
5D 8C 9S JS AC Highest card Ace                       2C 5C 7D 8S QH  Highest card Queen                  Player 1 
2D 9C AS AH AC Three Aces                             3D 6D 7D TD QD  Flush with Diamonds                  Player 2 
4D 6S 9H QH QC Pair of Queens Highest card Nine       3D 6D 7H QD QS  Pair of Queens Highest card Seven   Player 1 
2H 2D 4C 4D 4S Full House With Three Fours           3C 3D 3S 9S 9D  Full House with Three Threes        Player 1 
 
 The file, poker.txt , contains one-thousand random hands dealt to two players. 
 Each line of the file contains ten cards (separated by a single space): the first five are 
 Player 1\'s cards and the last five are Player 2\'s cards. You can assume that all hands are 
 \valid (no invalid characters or repeated cards), each player\'s hand is in no specific order, and in 
 each hand there is a clear winner. 
 How many hands does Player 1 win?
"""

import time
from collections import Counter
from projecteuler.utils.getinput import getinput
startTime = time.perf_counter()

f = getinput(54)
hands = [(hand.split()[:5],hand.split()[5:]) for hand in f.readlines() if len(hand) > 1]

face_order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


def greater_face(f1,f2):
    return face_order.index(f1) > face_order.index(f2)


def find_highest_face(hand):
    return face_order.index(max(sort_by_face([card[0] for card in hand]),key=lambda x: face_order.index(x)))

def find_smallest_face(faces):
    return min(faces,key=lambda x: face_order.index(x))

def sort_by_face(faces):
    return sorted(faces,key=lambda x: face_order.index(x))


def highcard(hand):
    faces = sort_by_face([card[0] for card in hand])
    return face_order.index(faces[-1])

def highcardfaces(faces):
    return face_order.index(faces[-1])

def isonepair(hand):
    faces = sort_by_face([card[0] for card in hand])
    count_faces = Counter(faces)
    if [c[1] for c in count_faces.most_common()] == [2,1,1,1]:
        return face_order.index(count_faces.most_common()[0][0])
    return False

def istwopairs(hand):
    faces = sort_by_face([card[0] for card in hand])
    count_faces = Counter(faces)
    if [c[1] for c in count_faces.most_common()] == [2,2,1]:
        f1,f2 = count_faces.most_common()[0][0], count_faces.most_common()[1][0]
        return face_order.index(f1) if greater_face(f1,f2) else face_order.index(f2)
    return False


def isthreeofakind(hand):
    faces = sort_by_face([card[0] for card in hand])
    count_faces = Counter(faces)
    if count_faces.most_common()[0][1] == 3:
        return face_order.index(count_faces.most_common()[0][0])
    return False

def isstraight(hand):
    faces = sort_by_face([card[0] for card in hand])
    index = face_order.index(faces[0])
    if faces == face_order[index:index+5]:
        return face_order.index(faces[-1])
    else:
        return False

def isflush(hand):
    faces = sort_by_face([card[0] for card in hand])
    suits = set([card[1] for card in hand])
    if len(suits) != 1:
        return False

    return face_order.index(faces[-1])

def isfullhouse(hand):
    faces = sort_by_face([card[0] for card in hand])
    counter = Counter(faces)
    if counter.most_common()[0][1] == 3 and counter.most_common()[1][1] == 2:
        return counter.most_common()[0][0]
    else:
        return False

def isfourofakind(hand):
    faces = sort_by_face([card[0] for card in hand])
    return faces.count(faces[0]) == 4 or faces.count(faces[-1]) == 4

def isstraightflush(hand):
    faces = sort_by_face([card[0] for card in hand])
    suits = set([card[1] for card in hand])
    if len(suits) != 1:
        return False

    index = face_order.index(faces[0])
    return faces == face_order[index:index+5]

def isroyalflush(hand):
    # are cards of same suit?
    faces = set([card[0] for card in hand])
    suits = set([card[1] for card in hand])
    if len(suits) != 1:
        return False

    # check for Ten, Jack, Queen, King, Ace
    royal = set(['T','J','Q','K','A'])
    return royal == faces


precedence = [
    isroyalflush,isstraightflush,isfourofakind,
    isfullhouse,isflush,isstraight,isthreeofakind,
    istwopairs,isonepair
]

def player_one_wins(hand1, hand2):
    for f in precedence:
        # res is a value if the hand is of the current function (royal flush, etc.), otherwise False
        res1,res2 = f(hand1),f(hand2)

        # if res1 is False, keep going
        if not res1:
            if res2:
                return False
            else:
                continue

        # if res1 is not False, make sure it beats the other hand
        if res1 > res2:
            return True

        # if res1 is not False, and is equal to res2, we have a genuine tie on our hands. investigate.
        elif res1 == res2:
            f1,f2 = find_highest_face(hand[0]),find_highest_face(hand[1])
            if f1 > f2:
                return True
            elif f1 == f2:
                break
            else:
                return False
        else:
            return False


    faces1 = sort_by_face([card[0] for card in hand1])
    faces2 = sort_by_face([card[0] for card in hand2])

    current = len(faces1) - 1

    while(current >= 0 and faces1[current] == faces2[current]):
        current -= 1;

    return greater_face(faces1[current],faces2[current])



"""
Right now sample hands are calculated incorrectly - use debugger to step through and see at what point the incorrect
decision is made.
"""



count_wins = 0
for hand in hands:
    if player_one_wins(hand[0],hand[1]):
        count_wins += 1
    
        
print(count_wins)

endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")

