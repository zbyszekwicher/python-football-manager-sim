import data
import MatchSimulating
from random import randrange
from time import sleep

def Match():
    firstTeam = data.goalkeeper+data.defenders+data.midfielders+data.atackers
    restPlayers = [item for item in data.playerTeam if item not in firstTeam]
    
    defendStr = data.GetTeamPower()[0]
    atackStr = data.GetTeamPower()[1]

    oponent = data.fixtures[data.gameWeek-1]
    oponent[1] = oponent[1]*10
    oponent[1] = oponent[1]+randrange(-1,2)

    n = randrange(-4,5)
    oponentDef = int(oponent[1]-n)
    oponentAtk = int(oponent[1]+n)

    xIn = oponentAtk - defendStr
    xOut = atackStr - oponentDef

    if xIn > 11:
        gListIn = goalsMax
    elif xIn > 8:
        gListIn = goalsPlus5
    elif xIn > 6:
        gListIn = goalsPlus4
    elif xIn > 4:
        gListIn = goalsPlus3
    elif xIn > 3:
        gListIn = goalsPlus2
    elif xIn > 2:
        gListIn = goalsPlus1
    elif xIn < -11:
        gListIn = goalsMin
    elif xIn < -8:
        gListIn = goalsMinus5
    elif xIn < -6:
        gListIn = goalsMinus4
    elif xIn < -4:
        gListIn = goalsMinus3
    elif xIn < -3:
        gListIn = goalsMinus2
    elif xIn < -2:
        gListIn = goalsMinus1
    else:
        gListIn = goalsEqual

    if xOut > 11:
        gListOut = goalsMax
    elif xOut > 8:
        gListOut = goalsPlus5
    elif xOut > 6:
        gListOut = goalsPlus4
    elif xOut > 4:
        gListOut = goalsPlus3
    elif xOut > 3:
        gListOut = goalsPlus2
    elif xOut > 2:
        gListOut = goalsPlus1
    elif xOut < -11:
        gListOut = goalsMin
    elif xOut < -8:
        gListOut = goalsMinus5
    elif xOut < -6:
        gListOut = goalsMinus4
    elif xOut < -4:
        gListOut = goalsMinus3
    elif xOut < -3:
        gListOut = goalsMinus2
    elif xOut < -2:
        gListOut = goalsMinus1
    else:
        gListOut = goalsEqual

    
    print ('strzelone .', gListOut)
    print ()
    print ('stracone  .', gListIn)
    
    print ("\n" * data.freeSpace)
    print('Match: '+data.clubName+' vs '+oponent[0]+'!\n')

    print('         ',data.clubName,'|',oponent[0])
    print('DEFENCE: ',defendStr,' '*(len(data.clubName)-3),'|',oponentDef,' '*(len(oponent[0])-3))
    print('  ATACK: ',atackStr ,' '*(len(data.clubName)-3),'|',oponentAtk,' '*(len(oponent[0])-3))

    inp = input('\n1 - kick off\n2 - simulate\n')
    while not inp in ('1','2'):
        inp = input('Type "1" or "2"\n')

    #gole strzelone i stracone - losowanie
    goalsIn = gListIn[randrange(len(gListIn))]
    goalsOut = gListOut[randrange(len(gListOut))]

    #asysty i gole
    scorers = []
    asists = []
    for i in range(goalsOut):
        rrrr = randrange(13)
        if rrrr < 6:
            sc = data.atackers[randrange(len(data.atackers))]
            scorers.append(sc)
        elif rrrr < 11:
            sc = data.midfielders[randrange(len(data.midfielders))]
            scorers.append(sc)
        else:
            sc = data.defenders[randrange(len(data.defenders))]
            scorers.append(sc)

        rrrr = randrange(20)
        if rrrr < 5:
            a = data.atackers[randrange(len(data.atackers))]
            asists.append(a)
        elif rrrr < 15:
            a = data.midfielders[randrange(len(data.midfielders))]
            asists.append(a)
        else:
            a = data.defenders[randrange(len(data.defenders))]
            asists.append(a)


    ballPosession = int( 100*( atackStr / (atackStr+oponentAtk) ) )
    
    #simulating
    if inp == '2':
        print ("\n" * data.freeSpace)
        print ('simulating...')
        
        sleep(0.5)
        
        print ("\n" * data.freeSpace)
        print (data.clubName+' vs '+oponent[0])
        print ('Result:',goalsOut,'-',goalsIn)
        input ()
        data.matchResult = ''
        if goalsOut > goalsIn:
            print('You win!')
            data.win += 1
            data.points += 3
            data.matchResult = 'win'

        elif goalsOut < goalsIn:
            print('You lose...')
            data.lose += 1
            data.matchResult = 'lose'

        else:
            print('There is a draw.')
            data.draw += 1
            data.points += 1
            data.matchResult = 'draw'


        if scorers:
            print('\nscorers:')
            for s in scorers:
                print(data.GetName(s))
                data.playerTeam[data.playerTeam.index(s)][9] = int(data.playerTeam[data.playerTeam.index(s)][9]) + 1

        if asists:
            print('\nassists:')
            for a in asists:
                print(data.GetName(a))
                data.playerTeam[data.playerTeam.index(a)][10] = int(data.playerTeam[data.playerTeam.index(a)][10]) + 1
    

        data.fixtures[data.gameWeek-1].append(str(goalsOut)+' - '+str(goalsIn))
        input('\ncontinue\n')

    elif inp == '1':
        MatchSimulating.MatchSimulating(goalsOut, goalsIn, ballPosession, oponent, scorers, asists)

        


    staminaLose = (0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,4,5,6)
    print ("\n" * data.freeSpace)
    print ('Players stamina:\n')
        
    print ('FIRST TEAM')
    print ('player\t\t\tgoals \t assists')
    for i in firstTeam:

        #stats - +1 match
        data.playerTeam[data.playerTeam.index(i)][8] = int(data.playerTeam[data.playerTeam.index(i)][8]) + 1

        if i in scorers:
            gg = 0
            for s in scorers:
                if s == i:
                    gg += 1
        else:
            gg = ''

        if i in asists:
            aa = 0
            for a in asists:
                if a == i:
                    aa += 1
        else:
            aa = ''

        
        x = staminaLose[randrange(len(staminaLose))]
        if i[3] == 'GKP' and x > 0:
            x -= 1
        i[7] = int(i[7])
        if i[7] - x < 1:
            print (data.GetName(i)+'\tINJURIED','\t',gg,'\t',aa)
            data.playerTeam[data.playerTeam.index(i)][7] = 0
        else:
            rr = randrange(1000)
            #input('\nKONTROLA\nrandomN = '+str(rr)+'kondycja = '+str(i[7]))
            if rr+int(i[7])*4 < 42:#nie wiem jaki dac numerek bo jak bylo 30 (i i[7]*2) to nie bylo kompletnie zadnych kontuzji
                print (data.GetName(i)+'\t- INJURIED','\t',gg,'\t',aa)
                data.playerTeam[data.playerTeam.index(i)][7] = 0
            else:
                data.playerTeam[data.playerTeam.index(i)][7] -= x
                print (data.GetName(i)+'\t- ',data.playerTeam[data.playerTeam.index(i)][7],'\t',gg,'\t',aa)
            
    print ('\nREST OF TEAM')
    for i in restPlayers:
        i[7] = int(i[7])
        if i[7] < 10:
            x = randrange(5,10)
            data.playerTeam[data.playerTeam.index(i)][7] += x
            if data.playerTeam[data.playerTeam.index(i)][7] > 10:
                data.playerTeam[data.playerTeam.index(i)][7] = 10
        print (data.GetName(i)+'\t- ',data.playerTeam[data.playerTeam.index(i)][7])
    for i in data.playerTeam:
        if i[3] == 'GKP':
            if data.playerTeam[data.playerTeam.index(i)][7] < 10:
                if randrange(2) == 0:
                    data.playerTeam[data.playerTeam.index(i)][7] += 1
    input('\ncontinue\n')
    
    data.Injuries()
               #

goalsMax    = [0,0,1,1,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4,5,5,6,7,8,9]

goalsPlus5  = [0,0,0,0,1,1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,5,6,7,8,9]
goalsPlus4  = [0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,5,6,7,8]
goalsPlus3  = [0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,5,6,7]
goalsPlus2  = [0,0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,3,3,3,4,4,5,6,7]
goalsPlus1  = [0,0,0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,3,3,3,4,4,5,6]
goalsEqual  = [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,3,3,3,4,4,5,6]
goalsMinus1 = [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,2,2,2,2,3,3,4,4,4]
goalsMinus2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,2,2,2,2,3,3,4,4]
goalsMinus3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,2,2,2,2,3,3,4]
goalsMinus4 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,2,2,2,2,3,3]
goalsMinus5 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,2,2,2,2,3]

goalsMin    = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,2,2,2]


"""
goalsPlus5  = [3,0,1,1,1,1,2,2,2,3,3,3,4,4,4,5,6,7,8,9]
goalsPlus4  = [3,0,0,1,1,1,1,2,2,2,3,3,3,4,4,4,5,6,7,8]
goalsPlus3  = [2,0,0,0,1,1,1,1,2,2,2,3,3,3,4,4,4,5,6,7]
goalsPlus2  = [2,0,0,0,0,1,1,1,1,2,2,2,3,3,3,4,4,5,6,7]
goalsPlus1  = [1,0,0,0,0,0,1,1,1,1,2,2,2,3,3,3,4,4,5,6]
goalsEqual  = [0,0,0,0,0,0,0,1,1,1,1,2,2,3,3,3,4,4,5,6]
goalsMinus1 = [0,0,0,0,0,0,0,0,1,1,1,1,2,2,3,3,4,4,5,6]
goalsMinus2 = [0,0,0,0,0,0,0,0,0,1,1,1,1,2,2,3,3,4,5,6]
goalsMinus3 = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,2,2,3,3,4,5]
goalsMinus4 = [0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,2,2,3,3,4]
goalsMinus5 = [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,2,2,3,4]

"""









"""  ORYGINALNIE jest ponizej - POWYZEJ ZMIENILEM ZEBY BYLA WIEKSZA ROZNICA POMIEDZY DRUZYNAMI I LEPSZE DRUZYNY WYGRYWALY
    
    if xIn > 14:
        gListIn = goalsPlus5
    elif xIn > 9:
        gListIn = goalsPlus4
    elif xIn > 6:
        gListIn = goalsPlus3
    elif xIn > 4:
        gListIn = goalsPlus2
    elif xIn > 2:
        gListIn = goalsPlus1
    elif xIn < -14:
        gListIn = goalsMinus5
    elif xIn < -9:
        gListIn = goalsMinus4
    elif xIn < -6:
        gListIn = goalsMinus3
    elif xIn < -4:
        gListIn = goalsMinus2
    elif xIn < -2:
        gListIn = goalsMinus1
    else:
        gListIn = goalsEqual

    if xOut > 14:
        gListOut = goalsPlus5
    elif xOut > 9:
        gListOut = goalsPlus4
    elif xOut > 6:
        gListOut = goalsPlus3
    elif xOut > 4:
        gListOut = goalsPlus2
    elif xOut > 2:
        gListOut = goalsPlus1
    elif xOut < -14:
        gListOut = goalsMinus5
    elif xOut < -9:
        gListOut = goalsMinus4
    elif xOut < -6:
        gListOut = goalsMinus3
    elif xOut < -4:
        gListOut = goalsMinus2
    elif xOut < -2:
        gListOut = goalsMinus1
    else:
        gListOut = goalsEqual

"""
