import socket
from Network import Network

def main():
  run = True
  n = Network()
  player = int(n.getP())
  print("Player: ", player + 1)

  while run:
    try:
      game = n.send("get")
    except:
      run = False
      print("fail 1")
      print("Game not found")
      break
          

    if game.bothMoved():
      try:
        game = n.send("reset")
      except:
        run = False
        print("fail 2")
        print("Game not Found")
        break
      if (game.winner() == 1 and player == 1):
        print("You won!")
        game.updateWins()
        print("PLayer 1 Wins: ", game.p1Wins)
        print("PLayer 2 Wins: ", game.p2Wins)
        print("Ties: ", game.ties)
      elif (game.winner() == 0 and player == 0):
        print("You won!")
        game.updateWins()
        print("PLayer 1 Wins: ", game.p1Wins)
        print("PLayer 2 Wins: ", game.p2Wins)
        print("Ties: ", game.ties)
        
      elif game.winner() == -1:
        print("Tie game!")
        game.updateWins()
        print("PLayer 1 Wins: ", game.p1Wins)
        print("PLayer 2 Wins: ", game.p2Wins)
        print("Ties: ", game.ties)
        
      elif (game.winner() == 1 and player == 0):
        print("You lost!")
        game.updateWins()
        print("PLayer 1 Wins: ", game.p1Wins)
        print("PLayer 2 Wins: ", game.p2Wins)
        print("Ties: ", game.ties)
      elif (game.winner() == 0 and player == 1):
        print("You lost!")
        game.updateWins()  
        print("PLayer 1 Wins: ", game.p1Wins)
        print("PLayer 2 Wins: ", game.p2Wins)
        print("Ties: ", game.ties)

    if game.connected():
      if player == 0:
        if not game.p1Moved:
          move = input("Rock, Paper or Scissors?: Enter r, p or s ")
          n.send(move)
      else:
        if not game.p2Moved:
          move = input("Rock, Paper or Scissors?: Enter r, p or s ")
          n.send(move)

main()
        

    

      
    
        
      
      
      
  

