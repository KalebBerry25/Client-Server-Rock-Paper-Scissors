import socket
from _thread import *
import pickle
from game import Game


server = "10.188.148.184"
port = 5555

#creats socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#binds socket to host and port
try:
  s.bind((server, port))
except socket.error as e:
  str(e)
#server socket begins listening for connections
s.listen(2)
print("Server Started")

connected = set()
#game dictionary to keep track of game objects 
games = {}
#count of players connected
idCount = 0

#threaded process that runs simultaneously
def threaded_process(conn, p, gameId):
  global idCount
  conn.send(str.encode(str(p)))
  reply = ""
  while True:
    try:
      data = conn.recv(4096).decode()
      
      if gameId in games:
        game = games[gameId]
        if not data:
          print("Disconected")
          break
        else:
          if data == "reset":
            game.resetMoves()
          elif data != "get":
            game.play(p, data)

          conn.sendall(pickle.dumps(game))
      else:
        break
    except:
      break
  print("Lost Connection")
  try:
    del games[gameId]
  except:
    pass
  idCount -= 1
  conn.close()

while True:
  conn, addr = s.accept()
  print("Connected to:", addr)

  idCount += 1
  p =0
  gameId = (idCount-1)//2
  if idCount % 2==1:
    games[gameId] = Game(gameId)
    print("New Game...")
  else:
    games[gameId].ready = True
    p =1
  

  start_new_thread(threaded_process, (conn,p,gameId))