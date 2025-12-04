import data
from time import sleep
from random import randrange




def changeAction(atacking, minute, minuteGstrz, minuteGstra, ballPosession, oponent):
    if minute in minuteGstrz:
        atacking = 1
    elif minute in minuteGstra:
        atacking = 0
    else:
        if atacking == 1:
            if randrange(1,101) >= ballPosession+10:
                atacking = 0
                
        else:
            if randrange(1,101) <= ballPosession-10:
                atacking = 1
    if atacking == 1:
        action = data.clubName+' atacking'
    else:
        action = oponent[0]+' atacking'

    return action
    


def MatchSimulating(strzelone, stracone, ballPosession, oponent, scorers, asists):      

    s = 0.2
    score_delay = 1.5
    
    action = data.clubName+' kick off'
    atacking = 1


    dol = [2,2,3,3,3,4,4,4,4,5,5,5,5,5,7,7,8,10]
    doliczone = dol[randrange(len(dol))]

    minuteGstrz = []
    minuteGstra = []
    for i in range(strzelone):
        m = randrange(1,90+doliczone)
        while m in minuteGstrz:
            m = randrange(1,90+doliczone)
        minuteGstrz.append(m)
    for i in range(stracone):
        m = randrange(1,90+doliczone)
        while m in minuteGstra+minuteGstrz:
            m = randrange(1,90+doliczone)
        minuteGstra.append(m)


    for i in range(100):
        if i in minuteGstra:
            if i+1 in minuteGstra:
                minuteGstra.remove(i)
    
    for i in range(100):
        if i in minuteGstrz:
            if i+1 in minuteGstrz:
                minuteGstrz.remove(i)
                scorers.pop()           #usuwanie z listy strzelców
                asists.pop()
    
    Gstrz = 0
    Gstra = 0
    
    minute = 0
    playing = True
    while playing:
        print ("\n" * data.freeSpace)
        print (data.clubName+' vs '+oponent[0])
        print ('Result:',Gstrz,'-',Gstra)
        print (str(minute)+"' -", action)



        #dodac sposob strzelenia gola (dosrodkowanie strzal z dystansu karny, rozny itp)
        if minute in minuteGstrz:
            sleep(s)
            print ()
            print ("GOAL ",data.clubName+' score!')
            print (data.GetName(scorers[Gstrz]),'score!')
            data.playerTeam[data.playerTeam.index(scorers[Gstrz])][9] = int(data.playerTeam[data.playerTeam.index(scorers[Gstrz])][9]) + 1
            if scorers[Gstrz] == asists[Gstrz]:
                #asists.remove(asists.index(Gstrz))     WYSKAKIWAL ERROR CZASEM ("2 is not in list")
                print('from penalty kick')
            else:
                print (data.GetName(asists[Gstrz]),'get assist')
                data.playerTeam[data.playerTeam.index(asists[Gstrz])][10] = int(data.playerTeam[data.playerTeam.index(asists[Gstrz])][10]) + 1        
            
            
            Gstrz += 1
            atacking = 0
            sleep(s)
            print ('Result:',Gstrz,'-',Gstra)
            sleep(score_delay)

        if minute in minuteGstra:
            sleep(s)
            print ()
            print ("GOAL ",oponent[0]+' score!')

            #dodac kto goal i kto asyste (stworzenie nowego pilkarza losowo)
            Gstra += 1
            atacking = 1
            sleep(s)
            print ('Result:',Gstrz,'-',Gstra)
            sleep(score_delay)



        

        if minute < 90 and minute != 45:
            minute += 1
            sleep(s)
            action = changeAction(atacking, minute, minuteGstrz, minuteGstra, ballPosession, oponent)
            
        elif minute == 45:
            sleep(s)
            print ("\n" * data.freeSpace)
            print (data.clubName+' vs '+oponent[0])
            print ('Result:',Gstrz,'-',Gstra)
            print (str(minute)+"' - half break")
            input ('\ncontinue\n')
            action = oponent[0]+' kick off'
            atacking = 2
            minute += 1
            
        else:
            sleep(s)
            d = 1
            while d <= doliczone:                
                minute = '90+'+str(d)
                print ("\n" * data.freeSpace)
                print (data.clubName+' vs '+oponent[0])
                print ('Result:',Gstrz,'-',Gstra)
                print (minute+"' -", action)

                d += 1
                sleep(s)
                action = changeAction(atacking, minute, minuteGstrz, minuteGstra, ballPosession, oponent)

            playing = False
            
            print ('\nMATCH FINISHED')
            input('\ncontinue\n')
            
            
            
            

        

        





#PODSUMOWANIE
    print ("\n" * data.freeSpace)
    print ('MATCH FINISHED\n')
    print (data.clubName+' vs '+oponent[0])
    print ('Result:',Gstrz,'-',Gstra)
    input ()
    if Gstrz > Gstra:
        print('You win!')
        data.win += 1
        data.points += 3
        data.matchResult = 'win'

    elif Gstrz < Gstra:
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

    if asists:
        print('\nassists:')
        for a in asists:
            print(data.GetName(a))
    

    data.fixtures[data.gameWeek-1].append(str(Gstrz)+' - '+str(Gstra))
    input('\ncontinue\n')





"""


okazja = ['shoot','shoot from the distance','cross and header']  #extend
comment = ['long pass','slowly buliding atack','dribbling','offensive pass']


def changeAction(action, atacking, minute, minuteGstrz, minuteGstra, ballPosession, oponent):
    o = False
    if minute in minuteGstrz:
        atacking = 1
        o = True
    elif minute in minuteGstra:
        atacking = 0
        o = True
    else:
        if atacking == 1:
            if randrange(1,101) <= ballPosession:
                if randrange(1,101) <= ballPosession:
                    o = True
            else:
                atacking = 0
                action = oponent[0]+': '+comment[randrange(len(comment))]
                
        else:
            if randrange(1,101) >= ballPosession:
                if randrange(1,101) >= ballPosession:
                    o = True
            else:
                atacking = 1
                action = data.clubName+': '+comment[randrange(len(comment))]

    if atacking == 1 and o:
        action = data.clubName+': '+okazja[randrange(len(okazja))]
            
    elif atacking == 0 and o:
        action = oponent[0]+': '+okazja[randrange(len(okazja))]

    return action

"""
