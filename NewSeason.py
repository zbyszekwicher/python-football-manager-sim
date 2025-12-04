import data
from random import shuffle,randrange
from time import sleep

data.fixtures = []
for i in data.playerLeague:
    data.fixtures.append(i)
shuffle(data.fixtures)
data.gameWeek = 0
data.win = 0
data.draw = 0
data.lose = 0
data.played = 0
data.points = 0
data.leaguePosition = 1


data.teamDefalutSort()

exec(open("MainMenu.py").read())


"""
print('PREPARING NEW SEASON')
prc = 0
for i in range(51):
    xx = '='*i
    yy = ' '*(50-i)
    print('|'+xx+yy+'|\t'+str(round(prc))+'%',end='\r')
    prc += 100/50
    sleep(0.1)
"""

"""
if data.playerLeague_name == 'National League':
    data.sponsorDeal[1] = 1
elif data.playerLeague_name == 'League Two':
    data.sponsorDeal[1] = randrange(1,4)
elif data.playerLeague_name == 'League One':
    data.sponsorDeal[1] =  randrange(2,5)
elif data.playerLeague_name == 'Championship':
    data.sponsorDeal[1] = randrange(5,10)
elif data.playerLeague_name == 'Premier League':
    data.sponsorDeal[1] = randrange(8,16)
print ("\n" * data.freeSpace)
print ('You have new sponsorship contract offer!')
data.sponsorDeal[0] = data.sponsorName[randrange(len(data.sponsorName))]
print ('"'+data.sponsorDeal[0]+'" company will pay you',data.sponsorDeal[1],'000 a week')
print ("Only thing you have to do is to carry their logo on your club's shirts")
inp = input ('\n1 - accept offer\n2 - reject offer\n')
while not inp in ('1','2'):
    inp = input('Type "1" or "2"\n')
if inp == '2':
    print ("\n" * data.freeSpace)
    print ('"'+data.sponsorDeal[0]+'" company will pay you',data.sponsorDeal[1],'000 a week')
    print ("Only thing you have to do is to carry their logo on your club's shirts")
    print ('\nAre you completly sure, you want to reject this offer?')
    inp2 = input('Type "reject" or "accept"\n')
    while not inp2 in ('reject','accept'):
        inp2 = input('Type only "reject" or "accept"')
    if inp2 == "accept":
        inp = '1'
    else:
        data.sponsorDeal = ['',0]
        input('\noffer has been rejected\ncontinue\n')
if inp == '1':
    print ("\n" * data.freeSpace)
    print ('Congratulations! You have just got your sponsorship contract with "'+data.sponsorDeal[0]+'" company!')
    input ('\ncontinue\n')
"""



