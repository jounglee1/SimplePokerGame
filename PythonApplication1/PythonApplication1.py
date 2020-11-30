
"""

창의적 공학설계입문 10분반
Final Project
Editor: Jeonbook National Univ. Computer Science Engneering,
        201614875 이정
Language: Python 3.8
Program: Py-Poker
Description:
Simple Poker Game via Python
Used module : random, tkinter, pillow 
Game Rule
    1. Rank order : Straight Flush > 4 of Card > Full House > Flush > Straight > 3 of Card > Two Pairs > One Pair > Top
    2. Same rank : compare Top Card of hand
    3. Ace has the value of 14
    4. User can change once, each card

Image Source from https://github.com/deltacluse/Tkinter_Poker

"""

import random
import tkinter
import tkinter.font
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
        
        print("\nUser Changed Card")

        for card in p2.hand:
            print("%07s %d" %(card.suit, card.num))

        print("Rank : %d" %isRank(p2.hand))
            
""" Define Rank Value """
def isRank(hand):
    
    if(isStraightFlush(hand) != False):
        return 800 + isStraightFlush(hand)

    elif(is4ofCard(hand) != False):
        return 700 + is4ofCard(hand)

    elif(isFullHouse(hand) != False):
        return 600 + isFullHouse(hand)

    elif(isFlush(hand) != False):
        return 500 + isFlush(hand)
    
    elif(isStraight(hand) != False):
        return 400 + isStraight(hand)

    elif(is3ofCard(hand) != False):
        return 300 + is3ofCard(hand)
        
    elif(is2Pair(hand) != False):
        return 200 + is2Pair(hand)

    elif(is1Pair(hand) != False):
        return 100 + is1Pair(hand)

    else:
        return isTop(hand)

def ranktoString(hand):
    
    rank = isRank(hand)

    if(rank >= 800):
        return "Straight Flush"
    
    elif(rank >= 700):
        return "4 of Card"
    
    elif(rank >= 600):
        return "Full House"
    
    elif(rank >= 500):
        return "Flush"
    
    elif(rank >= 400):
        return "Straight"
    
    elif(rank >= 300):
        return "3 of Card"
    
    elif(rank >= 200):
        return "Two Pairs"
    
    elif(rank >= 100):
        return "One Pair"

    else:
        return "Top"
 
""" Define Rank """
def isStraightFlush(hand):

    if(isFlush(hand) != False and isStraight(hand) != False):
        return isStraight(hand)

    else:
        return False

def is4ofCard(hand):
    
    cardnumlist = []

    for card in hand:
        cardnumlist.append(card.num)

    for i in range(1, 14):
        if(cardnumlist.count(i) == 4):
            if(i == 1):
                return 14
            else:
                return i
    
    return False

def isFullHouse(hand):

    if(is3ofCard(hand) != False and is2Pair(hand) != False):
        return is3ofCard(hand)
    
    else:
        return False

def isFlush(hand):

    if(hand[0].suit == hand[1].suit == hand[2].suit == hand[3].suit == hand[4].suit):
        return isTop(hand)

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

    cardnumlist.sort()

    for i in range(1, 14):
        if(cardnumlist.count(i) >= 3):
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

    cardnumlist.sort()

    for i in range(1, 14):
        if(cardnumlist.count(i) >= 2):
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

    cardnumlist.sort()

    for i in range(1, 14):
        if(cardnumlist.count(i) >= 2):
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

""" Card Change Button Command """
def card0Change():

    btnCardChange[0].config(text = "Changed", state = 'disabled')
    p2.changeSelectedCard(0, p.deck)
    card_p2_photoImage[0] = PIL.ImageTk.PhotoImage(p2.hand[0].img_F)
    card_p2_photoImage_label[0].config(image = card_p2_photoImage[0])
    window.update()

def card1Change():

    btnCardChange[1].config(text = "Changed", state = 'disabled')
    p2.changeSelectedCard(1, p.deck)
    card_p2_photoImage[1] = PIL.ImageTk.PhotoImage(p2.hand[1].img_F)
    card_p2_photoImage_label[1].config(image = card_p2_photoImage[1])
    window.update()

def card2Change():

    btnCardChange[2].config(text = "Changed", state = 'disabled')
    p2.changeSelectedCard(2, p.deck)
    card_p2_photoImage[2] = PIL.ImageTk.PhotoImage(p2.hand[2].img_F)
    card_p2_photoImage_label[2].config(image = card_p2_photoImage[2])
    window.update()

def card3Change():

    btnCardChange[3].config(text = "Changed", state = 'disabled')
    p2.changeSelectedCard(3, p.deck)
    card_p2_photoImage[3] = PIL.ImageTk.PhotoImage(p2.hand[3].img_F)
    card_p2_photoImage_label[3].config(image = card_p2_photoImage[3])
    window.update()

def card4Change():

    btnCardChange[4].config(text = "Changed", state = 'disabled')
    p2.changeSelectedCard(4, p.deck)
    card_p2_photoImage[4] = PIL.ImageTk.PhotoImage(p2.hand[4].img_F)
    card_p2_photoImage_label[4].config(image = card_p2_photoImage[4])
    window.update()

def matchStart():
    
    print("\nCOMPUTER CARD")

    for card in p1.hand:
        print("%07s %d" %(card.suit, card.num))

    print("Rank : %d" %isRank(p1.hand))

    print("\nUser CARD")

    for card in p2.hand:
        print("%07s %d" %(card.suit, card.num))

    print("Rank : %d" %isRank(p2.hand))

    labelPlayer1Score.config(text = ranktoString(p1.hand))
    labelPlayer2Score.config(text = ranktoString(p2.hand))

    if(isRank(p1.hand) == isRank(p2.hand)):
        btnMatchStart.config(text = "DRAW")
        print("\nGAME DRAW!")
        
    elif(isRank(p1.hand) < isRank(p2.hand)):
        btnMatchStart.config(text = "WIN")
        print("\nUSER WIN!")

    elif(isRank(p1.hand) > isRank(p2.hand)):
        btnMatchStart.config(text = "LOSE")
        print("\nCOMPUTER WIN!")

    for i in range(5):
        card_p1_photoImage[i] = PIL.ImageTk.PhotoImage(p1.hand[i].img_F)
        card_p1_photoImage_label[i].config(image = card_p1_photoImage[i])
        btnCardChange[i].config(text = "Game End", state = 'disabled')
        window.update()

""" Initialize Card Laycout """
card_p1_x_origin = 30
card_p1_y_origin = 30

card_p2_x_origin = card_p1_x_origin
card_p2_y_origin = card_p1_y_origin + 300

card_p1_x = []
card_p1_y = []
card_p2_x = []
card_p2_y = []

for i in range(5):
    card_p1_x.append(card_p1_x_origin + (200 * i))
    card_p1_y.append(card_p1_y_origin)
    card_p2_x.append(card_p2_x_origin + (200 * i))
    card_p2_y.append(card_p2_y_origin)


""" Main """
while(True):

    p = PokerGame()
    p1 = Player(p.deck)
    p2 = Player(p.deck)

    print("\nUser CARD")

    for card in p2.hand:
        print("%07s %d" %(card.suit, card.num))

    print("Rank : %d" %isRank(p2.hand))

    """ Initialize Window (tkinter) """
    window = tkinter.Tk()
    window.title("GAME")
    window.geometry("1170x700")
    window.resizable(False,False)
    window.config(background = 'darkseagreen')

    """ Button Layout Design """
    myfont = tkinter.font.Font(family="맑은 고딕", size=11, weight = 'bold')

    btnMatchStart = tkinter.Button(window, width = 10, height = 3, text = "Match!!", command = matchStart, background = 'Crimson', foreground = 'White' , font = myfont)
    btnMatchStart.place(x = 1050, y = 270)

    labelPlayer1Score = tkinter.Label(window, width = 10, height = 3, text = "Score", relief = 'solid', font = myfont)
    labelPlayer1Score.place(x = 1050, y = 140)

    labelPlayer2Score = tkinter.Label(window, width = 10, height = 3, text = "Score", relief = 'solid', font = myfont)
    labelPlayer2Score.place(x = 1050, y = 430)

    btnGameExit = tkinter.Button(window, width = 10, height = 3, text = "EXIT", background = 'lightsteelblue', command = lambda : exit(True), font = myfont)
    btnGameExit.place(x = 1050, y = 590)

    """ Initialize Card Image """
    card_p1_photoImage = []
    card_p2_photoImage = []
    card_p1_photoImage_label = []
    card_p2_photoImage_label = []

    for i in range(5):
        card_p1_photoImage.append(PIL.ImageTk.PhotoImage(p1.hand[i].img_B))
        card_p1_photoImage_label.append(tkinter.Label(window, image = card_p1_photoImage[i], background = 'gainsboro', relief = 'sunken'))
        card_p1_photoImage_label[i].place(x=card_p1_x[i], y=card_p1_y[i])
        card_p2_photoImage.append(PIL.ImageTk.PhotoImage(p2.hand[i].img_F))
        card_p2_photoImage_label.append(tkinter.Label(window, image = card_p2_photoImage[i], background = 'gainsboro', relief = 'sunken'))
        card_p2_photoImage_label[i].place(x=card_p2_x[i], y=card_p2_y[i])

    """ Function: Card Change """
    btnCardChange = []

    for i in range(5):
        btnCardChange.append(tkinter.Button(window, width = 10, height = 3, text = "Change", font = myfont))
        btnCardChange[i].place(x = card_p2_x[i] + 40, y = card_p2_y[i] + 270)

    btnCardChange[0].config(command = card0Change)
    btnCardChange[1].config(command = card1Change)
    btnCardChange[2].config(command = card2Change)
    btnCardChange[3].config(command = card3Change)
    btnCardChange[4].config(command = card4Change)
    
    """ Print Window """
    window.mainloop()

