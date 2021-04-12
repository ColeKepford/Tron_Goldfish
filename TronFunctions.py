import random

tronlands = ["mine", "pp", "tower"]

def naturaltron(hand):
  if("tower" in hand and "mine" in hand and "pp" in hand):
    return True
  return False

def twotronlands(hand):
  if("tower" in hand and "mine" in hand or "tower" in hand and "pp" in hand or
  "mine" in hand and "pp" in hand):
    return True
  return False

def onetronland(hand):
  if("tower" in hand or "mine" in hand or "pp" in hand):
    return True
  return False

def doublelandwithtutor(hand):

  if(twotronlands(hand) and "map" in hand or twotronlands(hand) and "scrying" in hand and "star" in hand):
    return True

  return False

def havetron(hand, board):
  foundlands = []
  for card in tronlands:
    if card in hand or card in board:
      foundlands.append(card)
  foundlands.sort()
  if foundlands == tronlands:
    return True
  return False

def twotronpieces(hand, board):
  found_pieces = 0
  for card in tronlands:
    if(card in hand or card in board):
      found_pieces += 1

    if(found_pieces == 2):
      return True
    return False

 

def keeponfive(hand):
  return(

      (naturaltron(hand))
    or
      (doublelandwithtutor(hand))
    or
      (twotronlands(hand) and "star" in hand)
  )
  

def keeponfour(hand):
  return(
      (naturaltron(hand))
    or
      (doublelandwithtutor(hand))
    or
      (twotronlands(hand))
    or
      (onetronland(hand) and "star" in hand or onetronland(hand) and "map" in hand)
  )

def keeponthree(hand):
  return(

      (naturaltron(hand))
    or
      (doublelandwithtutor(hand))
    or
      (twotronlands(hand))
    or
      (onetronland(hand) and "star" in hand or onetronland(hand) and "map" in hand)
  )

def keepontwo(hand):
  if(onetronland(hand)):
    return True
  return False

def keeponone(hand):
  if(onetronland(hand)):
    return True
  return False

def bottomcards(hand, handsize, deck):
  hand.sort()
  
  removedcards = 0
  finished = False
  while removedcards < 7 - handsize and not finished:
    tronlands = []
    tutors = []
    i = 0
    
    temphand = hand
    newhand = []
    while temphand:

      card = temphand.pop()
      if(card != "trash"):
        newhand.append(card)
      elif(card == "trash" and removedcards < 7 - handsize):
        deck.append(card)
        removedcards += 1
      else:
        newhand.append(card)

    hand = newhand
    
    i = 0
    while removedcards < 7 - handsize and i < len(hand):
      if(hand[i] == "tower" and "tower" not in tronlands or hand[i] == "mine" and "mine" not in tronlands or hand[i] == "pp" and "pp" not in tronlands):
        tronlands.append(hand[i])
      
      elif(hand[i] in tronlands):
        deck.append(hand.pop(i))
        removedcards += 1
        
      i += 1
    i = 0
    while removedcards < 7 - handsize and i < len(hand):
      if(hand[i] == "map" and "map" not in tutors or hand[i] == "scrying" and "scrying" not in tutors):
        tutors.append(hand[i])
      
      elif(hand[i] in tutors):
        deck.append(hand.pop(i))
        removedcards += 1
       
      i += 1
    i = 0
    
    while removedcards < 7 - handsize and i < len(hand):
      
      if(hand[i] == "wurmcoil"):
        deck.append(hand.pop(i))
        removedcards += 1
      
      elif(hand[i] == "karnG"):
        deck.append(hand.pop(i))
        removedcards += 1
      
      elif(hand[i] == "karnL"):
        deck.append(hand.pop(i))
        removedcards += 1
      
      i += 1
    i = 0

    while removedcards < 7 - handsize and i < len(hand):
      
      if(hand[i] == "stirrings" and "star" not in hand):
          deck.append(hand.pop(i))
          removedcards += 1
      
      elif(hand[i] == "stirrings" and doublelandwithtutor(hand)):
          deck.append(hand.pop(i))
          removedcards += 1

      elif(hand[i] == "scrying" and "star" not in hand or hand[i] == "scrying"
      and not onetronland(hand)):
        deck.append(hand.pop(i))
        removedcards += 1

      elif(hand[i] == "scrying" and "map" in hand and not onetronland(hand)):
        deck.append(hand.pop(i))
        removedcards += 1

      
      elif(hand[i] == "map" and not twotronlands(hand)):
          deck.append(hand.pop(i))
          removedcards += 1 
      
      i += 1

    i = 0
        
        
    while removedcards < 7 - handsize and i < len(hand):
      if(hand[i] == "star"):
        deck.append(hand.pop(i))
        removedcards += 1
      
      i += 1
    i = 0

    while removedcards < 7 - handsize and i < len(hand):
      if(hand[i] == "tower" or hand[i] == "mine" or hand[i] == "pp"):
        deck.append(hand.pop(i))
        removedcards += 1 
        
      i += 1
               
  return hand

def crackmap(hand, board, deck,):
  board.remove("map")
  for card in ["tower", "mine", "pp"]:
    if card not in hand and card not in board:
      hand.append(card)
      deck.remove(card)
      random.shuffle(deck)

def scrying(hand, board, deck,):
  hand.remove("scrying")
  for card in ["tower", "mine", "pp"]:
    if card not in hand and card not in board:
      hand.append(card)
      deck.remove(card)
      random.shuffle(deck)

def stirrings(hand, board, deck):
  hand.remove("stirrings")
  cards = []
  chosen = ""
  for x in range(5):
    cards.append(deck.pop(x))

  if(havetron(hand, board)):
    
    if("star" in cards):
      chosen = "star"

    elif("karnL" in cards):
      chosen = "karnL"
    
    elif("karnG" in cards):
      chosen = "karnG"
  
  for card in cards:
    if card in {"tower", "mine", "pp"}:
      if card not in board and card not in hand and chosen =="":
        chosen = card
  
  if "karnL" in cards and chosen =="":
    chosen = "karnL"

  if "karnG" in cards and chosen == "":
    chosen = "karnG"

  if "wurmcoil" in cards and chosen == "":
    chosen = "wurmcoil"
  
  if "star" in cards and chosen == "":
    chosen = "star"
  
  for card in cards:
    if card in {"tower", "mine", "pp", "map"} and chosen == "":
      chosen = card

  if chosen != "":
    cards.remove(chosen)
    hand.append(chosen)
    deck.remove(chosen)
  for card in cards:
    deck.append(card)





  