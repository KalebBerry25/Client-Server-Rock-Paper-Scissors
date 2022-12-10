class Game:
  def __init__(self, id):
    self.p1Moved = False
    self.p2Moved = False
    self.ready = False
    self.id = id
    self.moves = [None,None]
    self.p1Wins = 0
    self.p2Wins = 0
    self.ties = 0

  def player_move(self, player):
    return self.moves[player]

  def play(self, player, move):
    self.moves[player] = move
    if player == 0:
      self.p1Moved = True
    else:
      self.p2Moved = True

  def connected(self):
    return self.ready

  def bothMoved(self):
    return self.p1Moved and self.p2Moved

  def winner(self):
    p1 = self.moves[0]
    p2 = self.moves[1]
    winner = -1
    if p1 == "r" and p2 == "s":
      winner = 0
    elif p1 == "s" and p2 == "r":
      winner = 1
    elif p1 == "p" and p2 == "r":
      winner = 0
    elif p1 == "r" and p2 == "p":
      winner = 1
    elif p1 == "s" and p2 == "p":
      winner = 0
    elif p1 == "p" and p2 == "s":
      winner = 1
    return winner

  def updateWins(self):
    if self.winner() == 0:
      self.p1Wins += 1
    elif self.winner() ==  1:
      self.p2Wins +=1
    elif self.winner() == -1:
      self.ties += 1
  

  def resetMoves(self):
    self.p1Moved = False
    self.p2Moved = False




      

    


  
