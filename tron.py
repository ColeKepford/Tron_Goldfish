

from math import trunc
import random
import sys
import TronFunctions




board = []
tronlands = ["tower", "mine", "pp"]


deck = ["tower", "tower", "tower", "tower", "mine", "mine", "mine", "mine","pp", "pp", "pp","pp", "map", "map", "map", "map", "star", "star", "star", "star", "sphere", "sphere","sphere", "sphere", "scrying", "scrying", "scrying", "scrying", "stirrings", "stirrings", "stirrings", "stirrings",  "karnL", "karnL", "karnL", "karnL", "karnG", "karnG", "karnG", "karnG", "wurmcoil", "wurmcoil", "wurmcoil", "wurmcoil", "forest", "forest", "forest", "forest", "forest", "land", "land"]

for x in range(60 - len(deck)):
  deck.append("trash")

def tron(draw):
  

  
  random.shuffle(deck)
  hand = []
  for i in range(7):
    hand.append(deck[i])
  
  havetron = False
  keeping = False
  handsize = 7
  
  
  
  tronlands=["tower", "mine", "pp"]


  while not keeping and handsize > 0:
    if(TronFunctions.naturaltron(hand) and handsize == 7):
      keeping = True
      havetron = True
      
    elif(handsize <= 6 and TronFunctions.naturaltron(hand)):
      hand = TronFunctions.bottomcards(hand, handsize, deck)
      keeping = True
      havetron = True


          
    elif(TronFunctions.doublelandwithtutor(hand)):
      keeping = True
      havetron = True
      
      if(handsize == 6):
        hand = TronFunctions.bottomcards(hand, handsize, deck)
        keeping = True
        havetron = True
        

    if(handsize <= 5):
      
      if(handsize == 5):
        if(TronFunctions.keeponfive(hand)):
          hand = TronFunctions.bottomcards(hand, handsize, deck)
          keeping = True

      elif(handsize == 4):
        if(TronFunctions.keeponfour(hand)):
          hand = TronFunctions.bottomcards(hand, handsize, deck)
          keeping = True
          
      
      elif(handsize == 3):
        if(TronFunctions.keeponthree(hand)):
          hand = TronFunctions.bottomcards(hand, handsize, deck)
          keeping = True
          
      
      elif(handsize == 2):
        if(TronFunctions.keepontwo(hand)):
          hand = TronFunctions.bottomcards(hand, handsize, deck)
          keeping = True
          

      elif(handsize == 1):
        hand = TronFunctions.bottomcards(hand, handsize, deck)
        keeping = True
        
    if not keeping:
      handsize-= 1
      random.shuffle(deck)
      for i in range(7):
        hand[i] = deck[i]
    
  for card in hand:
    deck.remove(card)

  turn = 0
  
  tron = False
  while not tron:
    turn += 1
    mana = 0
    green = 0
    landplayed = False

    if(turn > 1 or draw == True):
      hand.append(deck.pop(0))
    
    for card in board:
      if card in tronlands or card == "land":
        mana += 1
      elif card == "forest":
        mana += 1
        green += 1

    for card in hand:
      if card in tronlands and card not in board and landplayed == False:
        board.append(card)
        hand.remove(card)
        mana += 1
        landplayed = True

    if(TronFunctions.naturaltron(board)):
      tron = True
    
    if("star" in board):
      board.remove("star")
      hand.append(deck.pop(0))
      green += 1
    
    if(TronFunctions.twotronpieces(hand,board)):
      if("map" in board and mana > 1):
        TronFunctions.crackmap(hand, board, deck)
        mana -= 2
      
      if("scrying" in hand and mana > 0 and green > 0):
        TronFunctions.scrying(hand, board, deck)
        mana -= 2
        green -= 1

      if("map" in hand and "map" not in board):
        board.append("map")
        hand.remove("map")
        mana -= 1

      action_taken= True
      while mana > 0 and action_taken:
        
        action_taken = False
        #cast ancient stirrings
        if (green > 0 and mana > 0 and "stirrings" in hand):
          green -= 1
          mana -= 1
          TronFunctions.stirrings(hand, board, deck)
          action_taken = True
        
        if("star" in board and mana > 0):
          board.remove("star")
          hand.append(deck.pop(0))
          green += 1
          action_taken = True
        
        if("star" in hand and mana > 0):
          board.append("star")
          hand.remove("star")
          mana -= 1
          action_taken = True

      if(landplayed == False):
        for card in hand:
          if card in tronlands and card not in board:
            board.append(card)
            hand.remove(card)
            mana += 1
            landplayed = True
            if(TronFunctions.twotronpieces(hand, board)):
              if("map" in board and mana > 1):
                TronFunctions.crackmap(hand, board, deck)
                mana -= 2
              if("scrying" in hand and mana > 1):
                TronFunctions.scrying(hand, board, deck)
                green -= 1
                mana -= 2
              if("map" in hand and mana > 0):
                board.append("map")
                hand.remove("map")
                mana -= 1
        
        if(landplayed == False):
          for card in hand:
            if(card == "forest"):
              board.append("forest")
              hand.remove("forest")
              mana+= 1
              green += 1
              landplayed = True
        if(landplayed == False):
          for card in hand:
            if(card == "land"):
              board.append("land")
              hand.remove("land")
              mana+= 1
              landplayed = True
        if("stirrings" in hand and green > 0 and mana > 0):
          TronFunctions.stirrings(hand, board, deck)
          green -= 1
          mana -= 1

        if("star" in hand and mana > 0):
          board.append("star")
          hand.remove("star")
          mana -= 1



  print("Turn", turn)
  print("Board State:")
  print(board)
  print("Hand:")
  print(hand)
  return(turn, handsize, TronFunctions.havetron(hand, board), "karnL" in hand and TronFunctions.havetron(hand, board), "karnL" in hand and TronFunctions.havetron(hand, board) or "karnG" in hand and TronFunctions.havetron(hand, board) or "wurmcoil" in hand and TronFunctions.havetron(hand, board))

turn3tron = 0
turn3Payoff = 0
turn3KL = 0
total_success_hand_size = 0   
total_fail_hand_size = 0

N = 2
for x in range(N):
  turn, hand_size, have_tron, have_karn, have_payoff = tron(False)

  
  if(turn == 3):
    turn3tron += 1

  if(turn3tron and have_karn):
    turn3KL += 1

  if(turn3tron and have_payoff):
    turn3Payoff += 1
  
  else:
    total_fail_hand_size += hand_size

#avg_success_size = total_success_hand_size / float(turn3tron)
#avg_fail_size = total_fail_hand_size / float(x - turn3tron)

#print("Turn 3 Tron: ", turn3tron / float(N) * 100)
#print("Turn 3 Payoff:", turn3Payoff / float(N) * 100)
#print("Turn 3 Karn Liberated: ", turn3KL / float(N) * 100)

  





