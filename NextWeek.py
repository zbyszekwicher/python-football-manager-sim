import data
import Match
from random import randrange

if data.gameWeek == 0:
     exec(open("TransferWindow.py").read())
    
elif data.gameWeek > len(data.fixtures):
     data.gameWeek += 1
     exec(open("SeasonEnd.py").read())

else:
     print ("\n" * data.freeSpace)
     firstTeam = data.atackers+data.midfielders+data.defenders+data.goalkeeper
     oponent = data.fixtures[data.gameWeek-1]
     walkover = False
     if len(firstTeam) < 11:
        data.printFirstTeam()
        print ('\nYOUR TEAM IS NOT FULL')
        print ('you cant begin match against '+oponent[0])
        print ('\n0 - come back to your team')
        print ('type "next" if you want to give walk-over')
        inp = input ()
        while not inp in ('0','next'):
            inp = input('type "0" or "next"')

        if inp == '0':
            exec(open("EditTeam.py").read())
        else:
            walkover = True
            
     else:
          lowStamina = False
          for i in firstTeam:
               if int(i[7]) < 5:
                    lowStamina = True
                    print(data.GetName(i)+"\t- stamina: "+str(i[7]))
          if lowStamina:
               print ('\nSOME PLAYERS FROM YOUR FIRST TEAM ARE LOW STAMINA')
               print ('there might be chance for getting injury')
               print ('\n0 - come back to your team')
               print ('1 - kick off anyway')
               inp = input ()
               while not inp in ('0','1'):
                    inp = input('type "0" or "1"')

               if inp == '0':
                    exec(open("EditTeam.py").read())
               
               
            
     if not walkover:
        
        Match.Match()##MATCH!!!!
        
     else:
        print ("\n" * data.freeSpace)
        print ('You gave walk-over.')
        print ('The result of the match '+data.clubName+' against '+oponent[0]+' is 0 - 3')
        data.fixtures[data.gameWeek-1].append('0 - 3')
        data.lose += 1


     data.gameWeek += 1          #    <--- TUTAJ GAMEWEEK!
     data.played +=1

     #Update league position
     res = {}
     n = 240
     x = round(240/len(data.playerLeague))
     x -= 1
     for i in range(len(data.playerLeague)):
        res[i+1] = n
        n -= x
     q = round(((data.points+0.21)*randrange(98,115)/data.played))
     LP = len(data.playerLeague)
     for i in res.items():
        if q >= i[1]:
            LP = i[0]
            break

     #print ('old',data.leaguePosition)            #########
     #print ('new',LP)
     #print (data.matchResult)

     if data.leaguePosition == LP:
          upOrDown = ' -'
     elif data.leaguePosition > LP:
          upOrDown = ' ^'
     elif data.leaguePosition < LP:
          upOrDown = ' v'
     
     if data.matchResult == 'win':
          if not LP > data.leaguePosition:
               data.leaguePosition = LP
          else:
               upOrDown = ' -'
     elif data.matchResult == 'lose':
          if not LP < data.leaguePosition:
               data.leaguePosition = LP
          else:
               upOrDown = ' -'
     elif data.matchResult == 'draw':
          if LP+1 >= data.leaguePosition:
               data.leaguePosition = LP
          else:
               upOrDown = ' -'
               
               
     print ('\nYour new league position is now',data.leaguePosition,upOrDown)
     input ('\ncontinue\n')

     #Update finances
     print ("\n" * data.freeSpace)
     print ('WEEKLY FINANCES')
     if data.sponsorDeal[0] == '':
        print('You do not have a sponsor contract')
     else:
        print('Sponsor: '+data.sponsorDeal[0])
     print (data.stadiumName+' max. capacity:',data.stadiumCapacity)
     print (data.playerLeague_name+' ticket cost:',data.tickets[data.playerLeague_name])
     capacity = round(data.stadiumCapacity*(randrange(40,101))/100)
     if walkover:
        capacity = 0
        print ('Because of walkover there was no match')
     print ("Today's capacity:",capacity)
     print ('\nIncomes:')
     inc1 = round((data.tickets[data.playerLeague_name]*capacity)/1000)
     print ('\tGate money:\t\t\t ',inc1,'000')
     inc2 = data.sponsorDeal[1]
     print ('\tSponsorship contract:\t\t ',inc2,'000')
     sumInc = inc1 + int(inc2)
     data.budget += sumInc
     data.addToFinances(sumInc,data.budget,'weekly income (gate money + sponsor)')
    
     print ('\nSpendings:')
     out1 = -(int(data.stadiumCapacity/10000)*10+2)
     print ('\tstadium maintenance       \t',out1,'000')
     out2 = -(int(data.trainingGroundLv/10*4+1))
     print ('\ttraining ground maintenance\t',out2,'000')
     if data.youthAcademyLv > 0:
        out3 = -(int(data.youthAcademyLv/10*4+1))
        print ('\tyouth academy maintenance\t',out3,'000')
     else:
        out3 = 0
     sumOut = out1+out2+out3
     data.budget += sumOut
     data.addToFinances(sumOut,data.budget,'club facilities maintenance')

     if sumOut+sumInc > 0:
        print ('\nTOTAL:  +'+str(sumInc+sumOut),'000')
     else:
        print ('\nTOTAL:  ',sumInc+sumOut,'000')
     print('\nNow your budget is',data.budget,'000')
     input ('\ncontinue\n')


     #Sponsor contract update
     if data.sponsorDeal[0] == '':
          if randrange(2) == 0:
               if data.playerLeague_name == 'National League':
                    data.sponsorDeal[1] = randrange(1,3)
               elif data.playerLeague_name == 'League Two':
                    data.sponsorDeal[1] = randrange(2,6)
               elif data.playerLeague_name == 'League One':
                    data.sponsorDeal[1] =  randrange(4,8)
               elif data.playerLeague_name == 'Championship':
                    data.sponsorDeal[1] = randrange(7,15)
               elif data.playerLeague_name == 'Premier League':
                    data.sponsorDeal[1] = randrange(11,21)
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
                    print ('\nAre you 100% sure, you want to reject this offer?')
                    inp2 = input('Type "reject" or "accept"\n')
                    while not inp2 in ('reject','accept'):
                         inp2 = input('Type only "reject" or "accept"')
                    if inp2 == "accept":
                         inp = '1'
                    else:
                         data.sponsorDeal = ['',0]
                         input('\noffer has been rejected\ncontinue\n')
               elif inp == '1':
                    print ("\n" * data.freeSpace)
                    print ('Congratulations! You have just got your sponsorship contract with "'+data.sponsorDeal[0]+'" company!')
                    input ('\ncontinue\n')

     #players skill update
     print ("\n" * data.freeSpace)
     chance = round((int(data.trainingGroundLv)+10)*2+7+data.trainingGroundLv)

     young = []
     for f in data.playerTeam:
          if int(f[4]) < 23:# or int(f[0]) > 8:
               young.append(f)
     
     for pl in young:
          rrr = randrange(1500*len(young))        #zwiekszylem z 1000 do 1500 bo turbo czesto sie wzmacniali
          
          #print(pl)
          #print(rrr,' - ',chance,'\n')
          
          if chance >= rrr:
               data.playerTeam[data.playerTeam.index(pl)][0] = int(data.playerTeam[data.playerTeam.index(pl)][0])
               data.playerTeam[data.playerTeam.index(pl)][0] += 1
               print(data.GetName(data.playerTeam[data.playerTeam.index(pl)])+' improved his skill!')
               print('Age:',int(data.playerTeam[data.playerTeam.index(pl)][4]))
               input('Now his skill is '+str(data.playerTeam[data.playerTeam.index(pl)][0]))
     """
     chance = round((int(data.trainingGroundLv)+10)*2+7+data.trainingGroundLv)
     #print('Chance for player upgrade:',chance/10,'%')############
     rrr = randrange(1000)
     #print('result is ',rrr/10,'%')############
     #input()##############
     if chance >= rrr:
          n = randrange(len(data.playerTeam))
          x = 0
          while int(data.playerTeam[n][4]) > 25 or int(data.playerTeam[n][0]) == 9:
               n = randrange(len(data.playerTeam))
               x += 1
               if x == 100:
                    break
                    n = False
                    #print('no player found')############
          if n:
               data.playerTeam[n][0] = int(data.playerTeam[n][0])
               data.playerTeam[n][0] += 1
               print(data.GetName(data.playerTeam[n])+' improved his skill!')
               print('Age:',int(data.playerTeam[n][4]))
               input('Now his skill is '+str(data.playerTeam[n][0]))
               
     #else:
     #     print('result failed. Upgrade your training ground for better results')
     #     input('continue\n')

     """
     #downgrade player's skill
     """
     if 5 >= randrange(100): #zrobione ze naprawde rzadko. Do przemyslenia co dalej
          n = randrange(len(data.playerTeam))
          x = 0
          while int(data.playerTeam[n][4]) < 31 or int(data.playerTeam[n][0]) == 1:
               n = randrange(len(data.playerTeam))
               x += 1
               if x == 100:
                    break
                    n = False
          if n:
               data.playerTeam[n][0] = int(data.playerTeam[n][0]) - 1
               print('Unfortunately, '+data.GetName(data.playerTeam[n])+"'s skill has been decreased.")
               print('Age:',int(data.playerTeam[n][4]))
               input('Now his skill is '+str(data.playerTeam[n][0]))
     """    
     
     print ("\n" * data.freeSpace)
     input ('\nsave progress\n')
     #Save data
     print ("Saving data...")
     data.ExportData()
     sleep(0.5)

     exec(open("MainMenu.py").read())
