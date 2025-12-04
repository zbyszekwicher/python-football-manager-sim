from random import randrange
from CreateNewPlayer import CreateNewPlayer
import data
data.playerTeam = []

position = "GKP"
for i in range(3):
    howGood = data.averageSkill + randrange(-1,2)
    newPlayer = CreateNewPlayer(howGood, position, 'England')
    data.playerTeam.append(newPlayer)
    
position = "DEF"
for i in range(6):
    howGood = data.averageSkill + randrange(-1,2)
    newPlayer = CreateNewPlayer(howGood, position, 'England')
    data.playerTeam.append(newPlayer)

position = "MID"
for i in range(6):
    howGood = data.averageSkill + randrange(-1,2)
    newPlayer = CreateNewPlayer(howGood, position, 'England')
    data.playerTeam.append(newPlayer)

position = "ATK"
for i in range(5):
    howGood = data.averageSkill + randrange(-1,2)
    newPlayer = CreateNewPlayer(howGood, position, 'England')
    data.playerTeam.append(newPlayer)

data.playerTeam.sort()
data.playerTeam.reverse()

lista = []
for i in data.playerTeam:
    if i[0] == 1:
        lista.append(i)

if len(lista) > 9:
    exec(open("CreateNewTeam.py").read())
