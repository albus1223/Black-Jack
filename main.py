import string
import time
import shelve
import os
import stdiomask


class User:
  def __init__(self, name, password):
    self.name = name
    self.password = password
    self.wins = 0
    self.losses = 0
  def win(self):
    self.wins += 1
  def loss(self):
    self.losses += 1


class Card:
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

class Blackjack:
  def __init__(self, players=[], dealer):
  # Define the suits and ranks of the deck
    suits = ["hearts", "diamonds", "spades", "clubs"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

  # Create a deck of cards
    # Create a deck of cards
    self.deck = []
    for suit in suits:
      for rank in ranks:
        self.deck.append(Card(suit,rank))
    
    # Shuffle the deck
    import random
    random.shuffle(self.deck)
    
    # Add players from list
    newplayer = input("enter new player")
    players.append(newplayer)
    
    # Deal the cards to the player and the dealer
    for player in players:
      player.hand = []
      player.hand.append(self.deck.pop())
      player.hand.append(self.deck.pop())
    
    dealer.hand = []
    dealer.hand.append(self.deck.pop())
    dealer.hand.append(self.deck.pop())
    
    # Begin the game
    while True:
      for player in players:
       count = 0
       print(player.hand)
        hit_stay = input("Hit (h) or Stay (s)?")
        if hit_stay == "h":
          player.hand.append(self.deck.pop())
          print(player.hand)
          for i in player.hand:
            if Card.rank in ["Jack","Queen","King"]:
              count += 10
            elif Card.rank == "Ace":
              
          if count>21:
            print("game over")
            break
          elif count == 21:
            print("21")
            continue
        elif hit_stay == "s":
         pass
      
      
def cipher(pswd):
  shift = 7
  enc_pass = ""
  for ch in pswd:
    val = string.ascii_lowercase.index(ch)
    val = (val + shift) % len(string.ascii_lowercase)
    enc_pass = enc_pass + string.ascii_lowercase[val]
  return enc_pass


def uncipher(pswd):
  #this is used to decipher certain phrases to match them to inputs
  #also used in listall function to undo the cipher so that
  #the user can read them. listall function is password protected
  shift = -7
  enc_pass = ""
  for ch in pswd:
    val = string.ascii_lowercase.index(ch)
    val = (val + shift) % len(string.ascii_lowercase)
    enc_pass = enc_pass + string.ascii_lowercase[val]
  return enc_pass


def signup():

  while True:
    #stdiomask replaces chrs in input with "*"
    
    #auth code ensures teacher is logging in and not student
    auth = stdiomask.getpass('authentication code: ')
    if auth == '123':
      usa = (input("username: "))
      if not usa == "exit":
        password = cipher(stdiomask.getpass("password: "))
        password_2 = cipher(stdiomask.getpass("confirm password: "))
        #checks if the two passwords match so
        #that user doesn't enter it wrong
        if password == password_2:
          with shelve.open('accounts') as usr_pwd:
            if usa not in usr_pwd:
              usr_pwd[usa] = password
              print('account created successfully!')
              time.sleep(1.5)
              os.system('clear')
              break
            else:
              print('Username already in use')
              time.sleep(1)
              print("----------------------------------------")
        else:
          print("passwords do not match")
          break
      else:
        break
    elif auth == "exit":
      break
    else:
      print('error: incorrect auth code')
      break


def login():
  while True:
    usr_name = input("username: ")
    if not usr_name == "exit":
      pwd_password = cipher(stdiomask.getpass("password: "))
      if not pwd_password == cipher("exit"):
        #if the username is a key in the dict and the password is equal to its corresponding key
        with shelve.open('accounts') as usr_pwd:
          if usr_name.casefold() in usr_pwd and pwd_password == usr_pwd[
              usr_name.casefold()]:
            print("login successful!")
            global currentuser
            currentuser = usr_name
            print(" ")
            help()
            print(" ")
            return True
            break
          else:
            print('incorrect username or password')
            continue
      else:
        return False
        continue
    else:
      return False
      continue      

# Main menu
while True:

  while True:
    print(" ")
    print("-------------- Main Menu ----------------")
    print(" ")
    logorsign = input('login (1) or signup (2)? ')
    if logorsign == '1':
      if login() == True:
        break
      else:
        continue
    elif logorsign == '2':
      signup()
    elif logorsign == 'help':
      print(" ")
      help()
    else:
      print('no such command:', logorsign)
      continue

  while True:
    command = input('>>> ')
    if command == '1':
      print(" ")
      # Add players
    elif command == 'logout':
      os.system('clear')
      break
