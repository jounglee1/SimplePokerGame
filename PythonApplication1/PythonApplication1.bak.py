
"""

창의적 공학설계 입문 10분반 기말 프로젝트
Program: Py-Poker
Editor: 전북대학교 컴퓨터공학부 201614875 이정
Language: Python 3.8

파이썬으로 구현된 포커 게임

Image Source from https://github.com/deltacluse/Tkinter_Poker

"""

import random
import tkinter
import PIL.Image
import PIL.ImageTk


""" Initialize Poker Cards """
class PokerGame:

    def __init__(self):
        
        self.deck = []

        self.deck.append(Card("Spade", 1, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/S01.png')))
        self.deck.append(Card("Spade", 2, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/S02.png')))
        self.deck.append(Card("Spade", 3, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/S03.png')))
        self.deck.append(Card("Spade", 4, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/S04.png')))
        self.deck.append(Card("Spade", 5, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/S05.png')))
        self.deck.append(Card("Spade", 6, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/S06.png')))
        self.deck.append(Card("Spade", 7, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/S07.png')))
        self.deck.append(Card("Spade", 8, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/S08.png')))
        self.deck.append(Card("Spade", 9, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/S09.png')))
        self.deck.append(Card("Spade", 10, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/S10.png')))
        self.deck.append(Card("Spade", 11, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/S11.png')))
        self.deck.append(Card("Spade", 12, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/S12.png')))
        self.deck.append(Card("Spade", 13, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/S13.png')))
        
        self.deck.append(Card("Club", 1, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/C01.png')))
        self.deck.append(Card("Club", 2, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/C02.png')))
        self.deck.append(Card("Club", 3, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/C03.png')))
        self.deck.append(Card("Club", 4, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/C04.png')))
        self.deck.append(Card("Club", 5, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/C05.png')))
        self.deck.append(Card("Club", 6, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/C06.png')))
        self.deck.append(Card("Club", 7, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/C07.png')))
        self.deck.append(Card("Club", 8, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/C08.png')))
        self.deck.append(Card("Club", 9, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/C09.png')))
        self.deck.append(Card("Club", 10, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/C10.png')))
        self.deck.append(Card("Club", 11, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/C11.png')))
        self.deck.append(Card("Club", 12, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/C12.png')))
        self.deck.append(Card("Club", 13, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/C13.png')))

        self.deck.append(Card("Heart", 1, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/H01.png')))
        self.deck.append(Card("Heart", 2, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/H02.png')))
        self.deck.append(Card("Heart", 3, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/H03.png')))
        self.deck.append(Card("Heart", 4, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/H04.png')))
        self.deck.append(Card("Heart", 5, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/H05.png')))
        self.deck.append(Card("Heart", 6, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/H06.png')))
        self.deck.append(Card("Heart", 7, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/H07.png')))
        self.deck.append(Card("Heart", 8, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/H08.png')))
        self.deck.append(Card("Heart", 9, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/H09.png')))
        self.deck.append(Card("Heart", 10, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/H10.png')))
        self.deck.append(Card("Heart", 11, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/H11.png')))
        self.deck.append(Card("Heart", 12, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/H12.png')))
        self.deck.append(Card("Heart", 13, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/H13.png')))

        self.deck.append(Card("Diamond", 1, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/D01.png')))
        self.deck.append(Card("Diamond", 2, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/D02.png')))
        self.deck.append(Card("Diamond", 3, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/D03.png')))
        self.deck.append(Card("Diamond", 4, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/D04.png')))
        self.deck.append(Card("Diamond", 5, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/D05.png')))
        self.deck.append(Card("Diamond", 6, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/D06.png')))
        self.deck.append(Card("Diamond", 7, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/D07.png')))
        self.deck.append(Card("Diamond", 8, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/D08.png')))
        self.deck.append(Card("Diamond", 9, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/D09.png')))
        self.deck.append(Card("Diamond", 10, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/D10.png')))
        self.deck.append(Card("Diamond", 11, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/D11.png')))
        self.deck.append(Card("Diamond", 12, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/D12.png')))
        self.deck.append(Card("Diamond", 13, PIL.Image.open('./image/0.png'), PIL.Image.open('./image/D13.png')))

        random.shuffle(self.deck)

""" Define Card """
class Card:
    
    def __init__(self, suit, num, img_B, img_F):

        self.suit = suit
        self.num = num
        self.img_B = img_B
        self.img_F = img_F

""" Initialize Player's Card (Hand) """
class Player():

    def __init__(self, deck):

        self.hand = []

        for i in range(5):
            self.hand.append(deck.pop())

    def changeSelectedCard(self, card_position_number, deck):

        self.hand[card_position_number] = deck.pop()
            
""" Define Rank Value """
def isRank(hand):
    
    if(isStraightFlush(hand) == True):
        return 9 + isStraightFlush(hand) / 100

    elif(is4ofCard(hand) == True):
        return 8 + is4ofCard(hand) / 100

    elif(isFullHouse(hand) == True):
        return 7 + isFullHouse(hand) / 100

    elif(isFlush(hand) == True):
        return 6 + isTop(hand) / 100
    
    elif(isStraight(hand) == True):
        return 5 + isStraight(hand) / 100

    elif(is3ofCard(hand) == True):
        return 4 + is3ofCard(hand) / 100

    elif(is2Pair(hand) == True):
        return 3 + is2Pair(hand) / 100

    elif(is1Pair(hand) == True):
        return 2 + is1Pair(hand) / 100

    else:
        return 1 + isTop(hand) / 100

""" Define Rank """
def isStraightFlush(hand):

    if(isFlush(hand) == True and isStraight(hand) == True):
        return isStraight(hand)

    else:
        return False

def is4ofCard(hand):
    
    cardnumlist = []

    for card in hand:
        cardnumlist.append(card.num)

    for i in range(1,14):
        if(cardnumlist.count(i) == 4):
            if(i == 1):
                return 14
            else:
                return i
    
    return False

def isFullHouse(hand):

    if(is3ofCard(hand) == True and is2Pair(hand) == True):
        return is3ofCard(hand)
    
    else:
        return False

def isFlush(hand):

    if(hand[0].suit == hand[1].suit == hand[2].suit == hand[3].suit == hand[4].suit):
        return True

    else:
        return False

def isStraight(hand):

    cardnumlist = []

    for card in hand:
        cardnumlist.append(card.num)

    cardnumlist.sort()

    if(cardnumlist[0] + 1 == cardnumlist[1] and\
       cardnumlist[1] + 1 == cardnumlist[2] and\
       cardnumlist[2] + 1 == cardnumlist[3] and\
       cardnumlist[3] + 1 == cardnumlist[4]):
        return cardnumlist[4]

    elif(cardnumlist[0] == 1 and\
         cardnumlist[1] == 10 and\
         cardnumlist[2] == 11 and\
         cardnumlist[3] == 12 and\
         cardnumlist[4] == 13):
        return 14

    else:
        return False

def is3ofCard(hand):

    cardnumlist = []

    for card in hand:
        cardnumlist.append(card.num)

    for i in range(1,14):
        if(cardnumlist.count(i) == 3):
            if(i == 1):
                return 14
            else:
                return i
    
    return False    

def is2Pair(hand):
    
    cardnumlist = []
    pairs_num = 0

    for card in hand:

        cardnumlist.append(card.num)

    for i in range(1,14):

        if(cardnumlist.count(i) == 2):
            pairs_num = pairs_num + 1

        if(pairs_num == 2):
            if(is1Pair(hand) == 14):
                return 14
            else:
                return i

    return False

def is1Pair(hand):

    cardnumlist = []

    for card in hand:
        cardnumlist.append(card.num)

    for i in range(1,14):
        if(cardnumlist.count(i) == 2):
            if(i == 1):
                return 14
            else:
                return i
    
    return False

def isTop(hand):

    cardnumlist = []

    for card in hand:
        cardnumlist.append(card.num)  
    
    cardnumlist.sort()

    if(cardnumlist[0] == 1):
        return 14
    else:
        return cardnumlist[4]

""" Initialize Card Position """
card_p1_x_origin = 30
card_p1_y_origin = 30

card_p2_x_origin = card_p1_x_origin
card_p2_y_origin = card_p1_y_origin + 350

card_p1_x = []
card_p1_y = []
card_p2_x = []
card_p2_y = []

for i in range(5):
    card_p1_x.append(card_p1_x_origin + (200 * i))
    card_p1_y.append(card_p1_y_origin)
    card_p2_x.append(card_p2_x_origin + (200 * i))
    card_p2_y.append(card_p2_y_origin)

""" define 1st Turn """
turn1 = 3
def nextTurn1():
    card_p1_photoImage[turn1] = PIL.ImageTk.PhotoImage(p1.hand[turn1].img_F)
    card_p1_photoImage_label[turn1].config(image = card_p1_photoImage[turn1])
    card_p2_photoImage[turn1] = PIL.ImageTk.PhotoImage(p2.hand[turn1].img_F)
    card_p2_photoImage_label[turn1].config(image = card_p2_photoImage[turn1])
    btnCheck.config(command = nextTurn2)
    window.update()

""" define 2nd Turn """
turn2 = 4
def nextTurn2():
    card_p1_photoImage[turn2] = PIL.ImageTk.PhotoImage(p1.hand[turn2].img_F)
    card_p1_photoImage_label[turn2].config(image = card_p1_photoImage[turn2])
    card_p2_photoImage[turn2] = PIL.ImageTk.PhotoImage(p2.hand[turn2].img_F)
    card_p2_photoImage_label[turn2].config(image = card_p2_photoImage[turn2])
    btnCheck.config(state = 'disabled')
    window.update()

""" Main """
while(True):
    p = PokerGame()
    p1 = Player(p.deck)
    p2 = Player(p.deck)

    print("\n Player1")

    for card in p1.hand:
        print("%07s %d" %(card.suit, card.num))

    print("Rank : " + str(isRank(p1.hand)))

    print("\n Player2")

    for card in p2.hand:
        print("%07s %d" %(card.suit, card.num))

    print("Rank : " + str(isRank(p2.hand)))

    """ Initialize Window (tkinter) """
    window = tkinter.Tk()
    window.title("GAME")
    window.geometry("1040x700")
    window.resizable(False, False)


    """ Initialize Card Image """
    card_p1_photoImage = []
    card_p2_photoImage = []
    card_p1_photoImage_label = []
    card_p2_photoImage_label = []

    for i in range(0,3):
        card_p1_photoImage.append(PIL.ImageTk.PhotoImage(p1.hand[i].img_F))
        card_p1_photoImage_label.append(tkinter.Label(window, image = card_p1_photoImage[i]))
        card_p1_photoImage_label[i].place(x=card_p1_x[i], y=card_p1_y[i])
        card_p2_photoImage.append(PIL.ImageTk.PhotoImage(p2.hand[i].img_F))
        card_p2_photoImage_label.append(tkinter.Label(window, image = card_p2_photoImage[i]))
        card_p2_photoImage_label[i].place(x=card_p2_x[i], y=card_p2_y[i])

    for i in range(3,5):
        card_p1_photoImage.append(PIL.ImageTk.PhotoImage(p1.hand[i].img_B))
        card_p1_photoImage_label.append(tkinter.Label(window, image = card_p1_photoImage[i]))
        card_p1_photoImage_label[i].place(x=card_p1_x[i], y=card_p1_y[i])
        card_p2_photoImage.append(PIL.ImageTk.PhotoImage(p2.hand[i].img_B))
        card_p2_photoImage_label.append(tkinter.Label(window, image = card_p2_photoImage[i]))
        card_p2_photoImage_label[i].place(x=card_p2_x[i], y=card_p2_y[i])

    btnCheck = tkinter.Button(window, width = 10, height = 3, text="CHECK", command = nextTurn1)
    btnCheck.place(x = 100, y = 300)


    window.mainloop()

