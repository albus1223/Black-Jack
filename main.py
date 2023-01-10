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
    for player in players:
      count = 0
      print(player.hand)
      hit_stay = input("Hit (h) or Stay (s)?")
      if hit_stay == "h":
        player.hand.append(self.deck.pop())
        print(player.hand)
        for i in player.hand:
          count += Card.rank
        if count>21:
          print("game over")
          break
        elif count == 21:
          print("21")
          continue
      if hit_stay == "s":
        pass
