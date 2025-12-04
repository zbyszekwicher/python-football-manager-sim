from time import sleep
import data
from CreateNewPlayer import CreateNewPlayer
from random import randrange

teams = data.premier_league+data.championship+data.league_one+data.league_two+data.world_teams
def Sold(name, cost):
    p = [0,0,0,0,0,0,0,0,0,0,0]#for check
    for i in data.playerTeam:
        if i[2] == name.split(' ')[1]:
            p = i
    print (p) #check
    
    print ("\n" * data.freeSpace,'TRANSFER WINDOW\n')
    data.budget += int(cost)
    for i in data.playerTeam:
        if i[1] == name.split()[0] and i[2] == name.split()[1]:
            data.playerTeam.remove(i)
    print('Congratulations! You already sell '+name+'!\n')

    if int(p[8]) > 0:
        print('He played',p[8],'matches for your club')
    if int(p[9]) > 0:
        print('Score',p[9],'goals')
    if int(p[10]) > 0:
        print('Assist',p[10],'times')
    print()

    #dodaje do listy graczy ever
    data.PlayersOfAllTheTime.append([data.GetName(p)+"\t- Position: "+p[3]+'\t\tplayed: '+str(p[8])+'\tscored: '+str(p[9])+'\tassists: '+str(p[10]),int(p[8])])
    
    print(int(cost),'000 has been added to your budget')
    print ('Now, your budget is',data.budget,'000')
    data.addToFinances(int(cost),data.budget,'selling '+name)

def Sell(name,cost):
    
    if len(data.playerTeam) > 15:
        Sold(name, cost)        
    else:
        print ("\n" * data.freeSpace,'TRANSFER WINDOW\n')
        print ("You have only "+str(len(data.playerTeam))+' players in your team')
        print ("Are you sure, you want to sell "+name+'?')
        print ('You might not have enough players for playing matches')
        print ('Remember, that you need a few players for the bench and doing first team rotations')
        inp_selling = input('\n type "sell" or "keep"\n')
        while inp_selling not in ('keep','sell'):
            inp_selling = input('Wrong input, type "keep" or "sell"')
        if inp_selling == 'keep':
            print ("\n" * data.freeSpace,'TRANSFER WINDOW\n')
            print('You reject this offer')
        else:
            Sold(name, cost)
    

def Decline():
    print ("\n" * data.freeSpace,'TRANSFER WINDOW\n')
    print('You reject this offer')

def Sign(player,cost):
    print ("\n" * data.freeSpace,'TRANSFER WINDOW\n')
    data.budget -= int(cost)
    data.playerTeam.append(player)
    print('Congratulations! You already sign '+data.GetName(player)+'!')
    print('your budget has been decreased by',int(cost),'000')
    print ('Now, your budget is',data.budget,'000')
    data.addToFinances(-int(cost),data.budget,'signing '+data.GetName(player))

def printTeam():
    print ("\n" * data.freeSpace,'TRANSFER WINDOW')
    print("\n\nALL YOUR PLAYERS")
    for i in data.playerTeam:
        if len(str(i[5])) == 4:
            i[5] = ' '+str(i[5])
        elif len(str(i[5])) == 3:
            i[5] = '  '+str(i[5])
        elif len(str(i[5])) == 2:
            i[5] = '   '+str(i[5])
    data.teamDefalutSort()
    for i in data.playerTeam:
        index = str(data.playerTeam.index(i)+1)
        if int(index) < 10:
            index = ' '+index
        print(index+") "+data.GetName(i)+" \t- Position: "+i[3]+" skill: "+str(i[0])+" age: "+str(i[4])+" value: "+str(i[5])+' 000')
    input ('\ncontinue\n')


inp = 0
transferList = []
other = []
x = 1
for i in data.playerTeam:
        if len(str(i[5])) == 4:
            i[5] = ' '+str(i[5])
        elif len(str(i[5])) == 3:
            i[5] = '  '+str(i[5])
        elif len(str(i[5])) == 2:
            i[5] = '   '+str(i[5])

for i in data.playerTeam:
    if x < 10:
        x = ' '+str(x)
    else:
        x = str(x)
    other.append(x+") "+data.GetName(i)+"\t- Position: "+i[3]+" skill: "+str(i[0])+" age: "+str(i[4])+" value: "+str(i[5])+' 000  nationality: '+i[6])
    x = int(x)+1

while inp != 'next':
    print ("\n" * data.freeSpace,'TRANSFER WINDOW\n')
    print('Firstly, add players you want sell to transfer list.')
    print('Team:')
    for i in other:
        print (i)
    print('\nTransfer list:')
    for i in transferList:
        print(i)
    print('\nType number of player you want to replace.')
    print('If you are done type "next"')
    index = ''
    while index == '':
        inp = input()
        if not inp == 'next':
            try:
                index = int(inp)
            except:
                print('Type only number or "next"')
        else:
            index = 'next'
    if not index == 'next':
        for i in transferList+other:
            if int(i.split(')')[0]) == index:
                x = 'finded'
                if i in other:
                    age = int(i.split(' age: ')[1].split(' value: ')[0])
                    if age > 17:
                        other.remove(i)
                        transferList.append(i)
                    else:
                        input('\nPlayer on a transfer list must be at least 18 years old\ncontinue')
                elif i in transferList:
                    transferList.remove(i)
                    other.append(i)

        if x != 'finded':
            index = ''
            input('Your number is incorrect\ncontinue')
        x = 0

if len(transferList) == 0:
    print ("\n" * data.freeSpace,'TRANSFER WINDOW\n')
    print('You dont want to sell your players and its OK\nBut there might be some offers \nlets check!\n')
    input('continue\n')
else: 
    print ("\n" * data.freeSpace,'TRANSFER WINDOW\n')
    print ('Now you will consider offerts about your players')
    print ('TIP: Dont sell all players')
    input ('\ncontinue\n')
    while len(transferList) != 0:
        for i in transferList:
            print ("\n" * data.freeSpace,'TRANSFER WINDOW\n')
            print ('Your budget:',data.budget,'000')
            full = i.split(') ')[1]
            name = full.split('\t- Position: ')[0]
            value = int(i.split(' value: ')[1].split(' 000')[0])
            age = int(i.split(' age: ')[1].split(' value: ')[0])
            transferList.remove(i)
            if randrange(4) == 0:
                print ('Unforunately nobody is intersted in signing '+name)
                input ('\ncontinue\n')
            else:
                buyingTeam = teams[randrange(len(teams))][0]
                valueMod = randrange(75,101)/100
                offer = int(value*valueMod)
                
                offering = True
                while offering:
                    print (buyingTeam+' is interested in signing '+name)#+'!')
                    print (full)
                    print ('Their offer is ',int(offer),'000')
                    print ('What will you do?')
                    print ('to accept offer type "sell"')
                    print ('to reject offer type "next"')
                    print ('to negotiate offer type "negotiate"')
                    print ('to see your team type "team"')
                    inp = input()
                    while not inp in ('sell','next','negotiate','team'):
                        inp = input ('wrong input\n')
                    negotiateTime = 0
                    biggestOffer = offer
                    if inp == 'negotiate':
                        while inp == 'negotiate':
                            negotiateTime += 1
                            print ("\n" * data.freeSpace,'TRANSFER WINDOW\n')
                            print ('Your budget:',data.budget,'000\n')
                            print (full)
                            if offer == int(value*valueMod):
                                print (buyingTeam+' offer is ',int(offer),'000')
                            else:
                                print (buyingTeam+' new offer is ',int(offer),'000')
                            print ('Type your counter-bid. It must be bigger than current offer')
                            print ('Type "sell" to accept their offer')
                            print ('Type "next" to reject their offer')
                            print ('Type "team" to see your team')
                            isInt = False
                            isCorrect = False
                            while not isCorrect:
                                while not isInt:
                                    inp2 = input()
                                    if not inp2 in ('sell','next','team'):
                                        try:
                                            inp2 = int(inp2)
                                            if isinstance(inp2,int):
                                                isInt = True
                                        except:
                                            print ('Type only numbers')
                                    else:
                                        isInt = True
                                if not inp2 in ('sell','next','team'):
                                    if inp2/1000 > offer:
                                        isCorrect = True
                                    else:
                                        print ('Type number bigger than ',offer,'000')
                                        isInt = False                                    
                                else:
                                    isCorrect = True
                            if not inp2 in ('sell','next','team'):
                                
                                offer = int(inp2/1000)
                                print ("\n" * data.freeSpace,'TRANSFER WINDOW\n')
                                print ('Your budget:',data.budget,'000\n')
                                print (full)
                                print ('Your new offer is',offer,'000.\n')
                                sleep (1)
                                if int(offer/(value*valueMod)*100) < randrange(105,150):
                                    print (buyingTeam+' is ready to pay you',offer,'000 in case to sign '+name+'.')
                                    input ('continue\n')
                                    Sell(name,offer)
                                    offering = False
                                    input ('continue\n')
                                    inp = ''
                                elif int(offer/(value*valueMod)*100) < randrange(150-negotiateTime*10,180):
                                    print (offer,'000 is too much for '+buyingTeam+' to sign '+name+'.')
                                    print ('But they are thinking about new offer')
                                    input ('continue\n')
                                    x = value*valueMod+int((offer-value*valueMod)*(randrange(30,61)/100))
                                    while x < biggestOffer+10:
                                        x += 3
                                    while x > offer-5:
                                        x -= 1
                                    offer = x
                                    biggestOffer = offer
                                else:
                                    print (buyingTeam+' told, that',offer,'000 in case to sign '+name+' is an outrageous offer.')
                                    print ('And they are not longer interested in signing '+name+'.')
                                    offering = False
                                    inp = ''
                                    input ('continue\n')
                            elif inp2 == 'sell':
                                offering = False
                                inp = ''
                                Sell(name,offer)
                                input ('continue\n')
                            elif inp2 == 'next':
                                offering = False
                                inp = ''
                                Decline()
                                input ('continue\n')
                            elif inp2 == 'team':
                                printTeam()
                                
                    elif inp == 'sell':
                        Sell(name,offer)
                        input ('continue\n')
                        offering = False
                    elif inp == 'team':
                        printTeam()
                    elif inp == 'next':
                        Decline()
                        input ('continue\n')
                        offering = False

    print ("\n" * data.freeSpace,'TRANSFER WINDOW\n')
    input ('There is nobody else on your transfer list.\nNow its time for some other offers\ncontinue\n')

### Here starts offers from other clubs for players not in transfer list

how_many_offers = int(len(data.playerTeam)/3)

if len(data.playerTeam) > 0:
    for i in range(randrange(2,how_many_offers)):
        i = data.playerTeam[randrange(len(data.playerTeam))]
        full = data.GetName(i)+"\t- Position: "+i[3]+" skill: "+str(i[0])+" age: "+str(i[4])+" value: "+str(i[5])+' 000  nationality: '+i[6]
        name = data.GetName(i)
        value = int(i[5])
        buyingTeam = teams[randrange(len(teams))][0]
        valueMod = randrange(75,101)/100
        offer = int(value*valueMod*1.3)

        offering = True
        while offering:
            print ("\n" * data.freeSpace,'TRANSFER WINDOW\n')
            print ('Your budget:',data.budget,'000')
            print (buyingTeam+' is interested in signing '+name+'!')
            print (full)
            print ('Their offer is ',int(offer),'000')
            print ('What will you do?')
            print ('to accept offer type "sell"')
            print ('to reject offer type "next"')
            print ('to negotiate offer type "negotiate"')
            print ('to see your team type "team"')
            inp = input()
            while not inp in ('sell','next','negotiate','team'):
                inp = input ('wrong input\n')
            negotiateTime = 0
            biggestOffer = offer
            if inp == 'negotiate':
                while inp == 'negotiate':
                        negotiateTime += 1
                        print ("\n" * data.freeSpace,'TRANSFER WINDOW\n')
                        print ('Your budget:',data.budget,'000\n')
                        print (full)
                        if offer == int(value*valueMod):
                                print (buyingTeam+' offer is ',int(offer),'000')
                        else:
                                print (buyingTeam+' new offer is ',int(offer),'000')
                        print ('Type your counter-bid. It must be bigger than current offer')
                        print ('Type "sell" to accept their offer')
                        print ('Type "next" to reject their offer')
                        print ('Type "team" to see your team')
                        isInt = False
                        isCorrect = False
                        while not isCorrect:
                                while not isInt:
                                        inp2 = input()
                                        if not inp2 in ('sell','next','team'):
                                                try:
                                                        inp2 = int(inp2)
                                                        if isinstance(inp2,int):
                                                                isInt = True
                                                except:
                                                        print ('Type only numbers')
                                        else:
                                                isInt = True
                                if not inp2 in ('sell','next','team'):
                                        if inp2/1000 > offer:
                                                isCorrect = True
                                        else:
                                                print ('Type number bigger than ',offer,'000')
                                                isInt = False
                                else:
                                        isCorrect = True
                        if not inp2 in ('sell','next','team'):
                            offer = int(inp2/1000)
                            print ("\n" * data.freeSpace,'TRANSFER WINDOW\n')
                            print ('Your budget:',data.budget,'000\n')
                            print (full)
                            print ('Your new offer is',offer,'000.\n')
                            sleep (1)
                            if int(offer/(value*valueMod)*100) < randrange(105,150):
                                print (buyingTeam+' is ready to pay you',offer,'000 in case to sign '+name+'.')
                                input ('continue\n')
                                Sell(name,offer)
                                offering = False
                                input ('continue\n')
                                inp = ''
                            elif int(offer/(value*valueMod)*100) < randrange(150-negotiateTime*10,180):
                                print (offer,'000 is too much for '+buyingTeam+' to sign '+name+'.')
                                print ('But they are thinking about new offer')
                                input ('continue\n')
                                x = value*valueMod+int((offer-value*valueMod)*(randrange(30,61)/100))
                                while x < biggestOffer+10:
                                    x += 3
                                while x > offer-5:
                                    x -= 1
                                offer = x
                                biggestOffer = offer
                            else:
                                print (buyingTeam+' told, that',offer,'000 in case to sign '+name+' is an outrageous offer.')
                                print ('And they are not longer interested in signing '+name+'.')
                                offering = False
                                inp = ''
                                input('continue')
                        elif inp2 == 'sell':
                            inp = ''
                            Sell(name,offer)
                            input ('\ncontinue\n')
                            offering = False
                        elif inp2 == 'next':
                            inp = ''
                            Decline()
                            input ('\ncontinue\n')
                            offering = False
                        elif inp2 == 'team':
                            printTeam()
                                
            elif inp == 'sell':
                Sell(name,offer)
                input ('continue\n')
                offering = False
            elif inp == 'team':
                printTeam()
            elif inp == 'next':
                Decline()
                input ('continue\n')
                offering = False

    print ("\n" * data.freeSpace,'TRANSFER WINDOW\n')
    print('There are no more offers...')
    input()
else:
    print ("\n" * data.freeSpace,'TRANSFER WINDOW\n')
    print('You do not have any player in your team')
    input()

#Here starts buying players
def PlayerDisplay(player):
    print (" *** ", data.GetName(player).upper(), " *** \n")
    if player[3] == "GKP":
        print("Position: \t", "goalkeeper")
    elif player[3] == "DEF":
        print("Position: \t", "defender")
    elif player[3] == "MID":
        print("Position: \t", "midfielder")
    elif player[3] == "ATK":
        print("Position: \t", "forward")
    print ("Skill: \t\t",  player[0])
    print ("Age: \t\t", player[4])
    print ("Market Value:\t", int(player[5]),' 000')
    print ('Nationality: \t '+player[6])
    
    
playersToBuy = []
positions = ('GKP','GKP','DEF','MID','ATK','DEF','MID','ATK','DEF','MID','ATK','DEF','MID','ATK')
for i in range(randrange(6,16)):
    if len(data.playerTeam) == 0:
        n = randrange(2,9)
    else:
        if randrange(3) == 0:
            x = int(data.playerTeam[randrange(len(data.playerTeam))][0])+1
            n = randrange(1,x)
        else:
            n = int(data.playerTeam[randrange(len(data.playerTeam))][0])+randrange(3)
    r = randrange(6)
    if r == 0:
        nationality = 'England'
    elif r == 1:
        nationality = 'Italian'
    elif r == 2:
        nationality = 'French'
    elif r == 3:
        nationality = 'German'
    else:
        nationality = 'Other'
    p = CreateNewPlayer(n,positions[randrange(len(positions))],nationality)
    isGood = True
    for i in playersToBuy:
        if i[2] == p[2]:
            isGood = False
    if isGood:
        playersToBuy.append(p)
    
data.playerTeam.sort(key=lambda x: x[0])
data.playerTeam.reverse()
for n in range(5):
    for i in playersToBuy:
        if len(str(i[5])) == 4:
            i[5] = ' '+str(i[5])
        elif len(str(i[5])) == 3:
            i[5] = '  '+str(i[5])
        elif len(str(i[5])) == 2:
            i[5] = '   '+str(i[5])
    correctAnswers = ['team','next']
    for i in playersToBuy:
        index = str(playersToBuy.index(i)+1)
        correctAnswers.append(str(index))
        if int(index) < 10:
            index = ' '+str(index)
    day = str(5 - n)
    inp = 0
    while inp != 'next':
        print ("\n" * data.freeSpace,'TRANSFER WINDOW')
        print ('Your budget:',data.budget,'000\n')
        print ('There is '+day+' days till the end of transfer window\n')
        print ('TIP: Upgrade your team in order to atract better players')
        for i in playersToBuy:
            index = str(playersToBuy.index(i)+1)
            if int(index) < 10:
                index = ' '+index
            print(index+") "+data.GetName(i)+"\t- Position: "+i[3]+" skill: "+str(i[0])+" age: "+str(i[4])+" value: "+str(i[5])+' 000 nationality: '+i[6])
        print('\nType number of player you want to buy or type "team" to look on your team.')
        print('If no one from that list sounds nice, you can just wait. Maybe it will refresh a bit')
        print('To skip this transfer window day type "next"')
        inp = input()
        while not inp in correctAnswers:
            inp = input('Type "team", "next", or correct player number.\n')
        if inp == 'next':
            pass
        elif inp == 'team':
            printTeam()
        else:
            print ("\n" * data.freeSpace,'TRANSFER WINDOW\n')
            print ('Your budget:',data.budget,'000\n')
            player = playersToBuy[int(inp)-1]
            PlayerDisplay(player)
            print ('\n1 - start negotiations (you can negotiate one time per day)')
            print ('0 - quit')
            inp2 = input()
            while not inp2 in ('1','0'):
                inp2 = input('Type correct number\n')
            if inp2 == '1':
                playersToBuy.remove(player)
                currentClub = teams[randrange(len(teams))][0]
                offer = ''
                answers = ['next']
                negTime = 0
                while inp2 == '1':
                    print ("\n" * data.freeSpace,'TRANSFER WINDOW\n')
                    print ('Your budget:',data.budget,'000\n')
                    PlayerDisplay(player)
                    print ("Current team:\t "+currentClub)
                    if offer == '':
                        print('\nType your offer for signing '+data.GetName(player)+' from '+currentClub+'.')
                    else:
                        print('\n'+currentClub+' counter-bid is ',offer,' 000.')
                        print('Type your new offer or type "buy" to accept their counter-bid')
                        answers.append('buy')
                    print('Or type "next" to quit negotiations')
                    isCorrect = False
                    isInt = False
                    while not isCorrect:
                            while not isInt:
                                    inp3 = input()
                                    if not inp3 in answers:
                                            try:
                                                    inp3 = int(inp3)
                                                    if isinstance(inp3,int):
                                                            isInt = True
                                            except:
                                                    print ('Type only numbers')
                                    else:
                                            isInt = True
                            if not inp3 in answers:
                                    if inp3/1000 <= data.budget:
                                            isCorrect = True
                                    else:
                                            print ('You do not have so much cash')
                                            isInt = False
                            else:
                                    isCorrect = True
                    inp4 = '1'
                    if inp3 == 'next':
                        inp2 = ''
                        inp = 'next'
                        print ("\n" * data.freeSpace,'TRANSFER WINDOW\n')
                        print ('Your budget:',data.budget,'000\n')
                        print('You end the negotiations with '+currentClub+' abut signing '+data.GetName(player)+'.')
                        input('\ncontinue\n')
                        inp4 = '0'
                    elif 'buy' in answers and inp3 == 'buy':
                        if offer <= data.budget:
                            Sign(player,offer)
                            inp2 = ''
                            inp = 'next'
                            input('\ncontinue\n')
                        else:
                            print ("\n" * data.freeSpace,'TRANSFER WINDOW\n')
                            print ('Your budget:',data.budget,'000\n')
                            input('You do not have enough money...\ncontinue\n')
                        inp4 = '0'
                    else:
                        if int(player[5]) < 20:
                            val = int(player[5])*1.6
                        else:
                            val = int(player[5])

                        inp3 = int(inp3/1000)
                        q = (inp3/val)*100

                    if q > 180:
                        print ("\n" * data.freeSpace,'TRANSFER WINDOW\n')
                        print ('Your budget:',data.budget,'000\n')
                        print (inp3,'000 is a lots of money!! Are you sure you want offer this?')
                        print ('Reminder: '+data.GetName(player)+' is worth ',player[5],'000')
                        print ('\n1 - I know what i am doing.')
                        print ('0 - Changed my mind. I want to change offer.')
                        inp4 = input ()
                        while not inp4 in ('1','0'):
                            inp4 = input('Type correct number\n')
                        
                    if inp4 == '1':
                        if q > randrange(110,140):
                            print ("\n" * data.freeSpace,'TRANSFER WINDOW\n')
                            print ('Your budget:',data.budget,'000\n')
                            print (currentClub+' accept your offer of ',inp3,'000.')
                            input('\ncontinue\n')
                            offer = inp3
                            Sign(player,offer)
                            inp2 = ''
                            inp = 'next'
                            input('\ncontinue\n')
                        elif q > randrange(70+negTime*10,90+negTime*10):
                            x = int(int(player[5])*(randrange(105,146)/100))
                            if offer != '':
                                while x >= offer:                                           #?????
                                    x -= randrange(5,10)
                            while x < inp3:
                                x += 1
                            offer = x

                            if offer == inp3:
                                print ("\n" * data.freeSpace,'TRANSFER WINDOW\n')
                                print ('Your budget:',data.budget,'000\n')
                                print (currentClub+' accept your offer of ',inp3,'000.')
                                input('\ncontinue\n')
                                offer = inp3
                                Sign(player,offer)
                                inp2 = ''
                                inp = 'next'
                                input('\ncontinue\n')
                            else:
                                print ("\n" * data.freeSpace,'TRANSFER WINDOW\n')
                                print ('Your budget:',data.budget,'000\n')
                                print (currentClub+' told that '+data.GetName(player)+' is worth more than',inp3,'000.')
                                print ('But they are thinking about counter-bid')
                                input ('\ncontinue\n')
                            
                        else:
                            if inp3 == 0:
                                input('Your offer is too low. You have to offer at least 1 000. \ncontinue\n')
                                negTime -= 1
                            else:
                                print ("\n" * data.freeSpace,'TRANSFER WINDOW\n')
                                print ('Your budget:',data.budget,'000\n')
                                print (currentClub+' told, that',inp3,'000 in case to sell '+data.GetName(player)+' is an outrageous offer.')
                                print ('And, that '+data.GetName(player)+' is worth MUCH more than',inp3,'000.')
                                print ('And they are not longer interested in selling '+data.GetName(player)+'.')
                                input('\ncontinue\n')
                                
                                inp2 = ''
                                inp = 'next'
                                print ("\n" * data.freeSpace,'TRANSFER WINDOW\n')
                                print ('Your budget:',data.budget,'000\n')
                                print('The negotiations with '+currentClub+' abut signing '+data.GetName(player)+' are closed')
                                input('\ncontinue\n')

                    negTime += 1
            
    print ("\n" * data.freeSpace,'TRANSFER WINDOW\n')
    print ('These players are no longer avaliable:\n')
    item = playersToBuy[randrange(len(playersToBuy))]
    playersToBuy.remove(item)
    print(data.GetName(item)+' was signed by '+teams[randrange(len(teams))][0])
    for i in range(randrange(2,10)):
        if len(playersToBuy) > randrange(5,20):
            item = playersToBuy[randrange(len(playersToBuy))]
            playersToBuy.remove(item)
            print(data.GetName(item)+' was signed by '+teams[randrange(len(teams))][0])
        if len(playersToBuy) < randrange(14,22):
            if len(data.playerTeam) == 0:
                n = randrange(2,9)
            else:
                if randrange(3) == 0:
                    x = int(data.playerTeam[randrange(len(data.playerTeam))][0])+1
                    n = randrange(1,x)
                else:
                    n = int(data.playerTeam[randrange(len(data.playerTeam))][0])+randrange(3)
            r = randrange(6)
            if r == 0:
                nationality = 'England'
            elif r == 1:
                nationality = 'Italian'
            elif r == 2:
                nationality = 'French'
            elif r == 3:
                nationality = 'German'
            else:
                nationality = 'Other'
            p = CreateNewPlayer(n,positions[randrange(len(positions))],nationality)
            isGood = True
            for i in playersToBuy:
                if i[2] == p[2]:
                    isGood = False
            if isGood:
                playersToBuy.append(p)
    input ('\ncontinue\n')

    

print ("\n" * data.freeSpace,'TRANSFER WINDOW IS NOW CLOSED!')
input ('\ncontinue and save progress\n')

data.gameWeek += 1          #    <--- TUTAJ GAMEWEEK!

#Save data
#exec(open("Saving.py").read())
print ("Saving data...")
data.ExportData()
sleep(0.5)

data.ImportData()#jest error po okienku kiedy chce sortowac zawodnikow

exec(open("MainMenu.py").read())
