"""
ZROBIC ZEBY JEDEN GRACZ MOGL SIE NA RAZ ULEPSZYC TYLKO O JEDEN

1)podsumowanie ligi
2)nagroda za lige
3)podsumowanie finansow
    w tym wynagrodzenia dla pilkarzy!

4)szkolka mlodzierzowa
    w pierwszym sezonie od zalorzenia szkolki nie dostaje sie pilkarzy


aktualizacja zmiennych (gameWeek, playerLeague, playerLeague_name, fixures,
wiek graczy, winlosedraw itp)

5)pilkarze starsi niz 35 lat koncza kariery (36+)

6)młodzi piłkarze mają szanse na ulepszenie skilla
    jesli wystarczajaco dobry training ground to nawet o 2

7)zakonczenie kontraktu sponsorskiego
    jest mozliwosc przedluzenia kontraktu
    jesli awans do wyzszej ligi wskazowka zeby poszukac nowego sponsora

8) update wartosc pilkarzy

9) jesli mały stadion w porownaniu do ligi: przypomnienie o wybudowaniu nowego

10) continue -> after the summer breake following players end their injuries:
            wszyscy pilkarze lecza kontuzje
"""
            
import data
import CreateNewPlayer
from random import shuffle,randrange

def stadiumNameChangeOffer(n, PremierLeague):
    input('continue')
    company = data.sponsorName[randrange(len(data.sponsorName))]
    sth = ['Stadium', 'Arena', 'Ground']
    addsth = sth[randrange(len(sth))]
    newName = company+' '+addsth
    print("\n" * data.freeSpace)
        
    if PremierLeague:
        if n < 2:
            print(company+" company wants to pay you 5000 000 in case to change your stadium's name from "+data.stadiumName+' to '+newName+'.')
            print("\n If you agree, for future stadium's name changes you will have to pay 5000 000 compensation")
            print('your budget: '+str(data.budget)+' 000')
            inp = input('type: "yes" / "no" \n')
            while not inp in ('yes','no'):
                inp = input('wrong input, type "yes" or "no" \n')
            if inp == 'yes':
                print("\n" * data.freeSpace)
                data.stadiumName = newName
                data.budget += 1000
                data.stadiumSponsored = 2
                print('Your new stadium name is "'+data.stadiumName+'"')
                print('now your budget is '+str(data.budget)+' 000')
                input('continue')
            
            
    elif n == 0:
        print(company+" company wants to pay you 1000 000 in case to change your stadium's name from "+data.stadiumName+' to '+newName+'.')
        print("\n If you agree, for future stadium's name changes you will have to pay 1000 000 compensation")
        print('your budget: '+str(data.budget)+' 000')
        inp = input('type: "yes" / "no" \n')
        while not inp in ('yes','no'):
            inp = input('wrong input, type "yes" or "no" \n')
        if inp == 'yes':
            print("\n" * data.freeSpace)
            data.stadiumName = newName
            data.budget += 1000
            data.stadiumSponsored = 1
            print('Your new stadium name is "'+data.stadiumName+'"')
            print('now your budget is '+str(data.budget)+' 000')
            input('continue')



data.goalkeeper = []
data.defenders = []
data.midfielders = []
data.atackers = []


#hallOfFame
if int(data.leaguePosition) in (1,2,3):
    txt = data.playerLeague_name+'-'+str(data.leaguePosition)+'place in'+str(data.year)+'season'
    data.hallOfFame.append(txt)


#SEASON SUMMARY

print("\n" * data.freeSpace)
print('The',data.year,'season finished!')
print('You finished ',data.playerLeague_name,' at ',data.leaguePosition,'position')


if data.playerLeague_name == 'National League':
    prize = 1000
    print('There are two teams promoted from National League to League Two\n')
    if data.leaguePosition < 3:
        print('YOU ARE PROMOTED TO LEAGUE TWO')
        data.playerLeague = data.league_two
        data.playerLeague_name = 'League Two'

        stadiumNameChangeOffer(data.stadiumSponsored, False)

        if int(data.sponsorDeal[1]) < 2:
            print ('\n TIP: Now in higher league you might consider trying to get better sponsorship contract')
        
    else:
        print('You stay in National League for the next season')

elif data.playerLeague_name == 'League Two':
    prize = 3000
    print('There are four teams promoted from League Two to League One')
    print('And two teams are relegated\n')
    if data.leaguePosition < 5:
        print('YOU ARE PROMOTED TO LEAGUE ONE')
        data.playerLeague = data.league_one
        data.playerLeague_name = 'League One'

        stadiumNameChangeOffer(data.stadiumSponsored, False)

        if int(data.sponsorDeal[1]) < 4:
            print ('\n TIP: Now in higher league you might consider trying to get better sponsorship contract')
        
        if int(data.stadiumCapacity) < 2500:
            print ("\n TIP: Your club is achieving succes and it brings more and more fans! But your stadium capaciity is only",data.stadiumCapacity)
            print ("Consider building bigger stadium and your weekly income will increase!")
            print ('You can do it from main menu in "your club" -> "stadium" -> "build new stadium"')
        
    elif data.leaguePosition > 22:
        print('UNFORTUNATELY YOU ARE RELEGATED TO NATIONAL LEAGUE')
        data.playerLeague = data.national_league
        data.playerLeague_name = 'National League'
    else:
        print('You stay in League Two for the next season')

elif data.playerLeague_name == 'League One':
    prize = 5000
    print('There are three teams promoted from League One to Championship')
    print('And four teams are relegated\n')
    if data.leaguePosition < 4:
        print('YOU ARE PROMOTED TO CHAMPIONSHIP')
        data.playerLeague = data.championship
        data.playerLeague_name = 'Championship'

        stadiumNameChangeOffer(data.stadiumSponsored, False)
        
        if int(data.sponsorDeal[1]) < 7:
            print ('\n TIP: Now in higher league you might consider trying to get better sponsorship contract')
        if int(data.stadiumCapacity) < 18999:
            print ("\n TIP: Your club is achieving succes and it brings more and more fans! But your stadium capaciity is only",data.stadiumCapacity)
            print ("Consider building bigger stadium and your weekly income will increase!")
            print ('You can do it from main menu in "your club" -> "stadium" -> "build new stadium"')
        
    elif data.leaguePosition > 20:
        print('UNFORTUNATELY YOU ARE RELEGATED TO LEAGUE TWO')
        data.playerLeague = data.league_two
        data.playerLeague_name = 'League Two'
    else:
        print('You stay in League One for the next season')

elif data.playerLeague_name == 'Championship':
    prize = 10000
    print('There are three teams promoted from Championship to Premier League')
    print('And three teams are relegated\n')
    if data.leaguePosition < 4:
        print('YOU ARE PROMOTED TO PREMIER LEAGUE')
        data.playerLeague = data.premier_league
        data.playerLeague_name = 'Premier League'

        stadiumNameChangeOffer(data.stadiumSponsored, True)

        if int(data.sponsorDeal[1]) < 11:
            print ('\n TIP: Now in higher league you might consider trying to get better sponsorship contract')

        if int(data.stadiumCapacity) < 44567:
            print ("\n TIP: Your club is achieving succes and it brings more and more fans! But your stadium capaciity is only",data.stadiumCapacity)
            print ("Consider building bigger stadium and your weekly income will increase!")
            print ('You can do it from main menu in "your club" -> "stadium" -> "build new stadium"')
        
    elif int(data.leaguePosition) > 21:
        print('UNFORTUNATELY YOU ARE RELEGATED TO LEAGUE ONE')
        data.playerLeague = data.league_one
        data.playerLeague_name = 'League One'
    else:
        print('You stay in Championship for the next season')

elif data.playerLeague_name == 'Premier League':
    prize = 15000
    print('There are three teams relegated from Premier League to Championship\n')
    if int(data.leaguePosition) > 17:
        print('UNFORTUNATELY YOU ARE RELEGATED TO CHAMPIONSHIP')
        data.playerLeague = data.championship
        data.playerLeague_name = 'Championship'
    else:
        print('You stay in Premier League for the next season')

input('continue\n')

#LEAGUE REWARD
print("\n" * data.freeSpace)
print('*** FINANCES SUMMARY ***')

x = (data.leaguePosition-1)*(prize/100)
reward = int(prize-x)
print('Your reward for',data.leaguePosition,'th place is',reward,'000')
print(reward,'000 has been added to your budget')
data.budget += reward
print('your budget:',data.budget,'000')

input('\ncontinue\n')

#PLAYER'S FEES + FINANCES SUMMARY
print()
print("Player's fees:")
total = 0
for i in data.playerTeam+data.injuried:
    x = int(i[0])
    fee = int( (x*x/2+0.5) * randrange(70,130)/10 )
    if fee == 0:
        fee = 1
    print(data.GetName(i),'\tfee:\t',fee,'000')
    total += fee

print('\nTOTAL FEES:',total,'000\n')

print()
print("Club facilities maintenance:")
out1 = ((int(data.stadiumCapacity/10000))*10+2)*4
print ('\tstadium maintenance       \t',out1,'000')
out2 = (int(data.trainingGroundLv/10*4+1))*2
print ('\ttraining ground maintenance\t',out2,'000')
if data.youthAcademyLv > 0:
    out3 = (int(data.youthAcademyLv/10*4+1))*2
    print ('\tyouth academy maintenance\t',out3,'000')
else:
    out3 = 0
total2 = out1+out2+out3

print('\nTOTAL FACILITIES:',total2,'000\n')

                                                    #DODAC PLACENIE ZA SKAUTOW

suma = total + total2    #  +total3 za skautow
print('\nTOTAL:',suma,'000\n')

print(suma,'000 has been removed from your budget')
data.budget -= total
print('Now your budget is',data.budget,'000')

input('\ncontinue\n')

#TRAINING
print("\n" * data.freeSpace)
chance = round((int(data.trainingGroundLv)+10)*2+7+data.trainingGroundLv)

young = []
for f in data.playerTeam:
    if int(f[4]) < 28:  #tutaj 27 lat i mlodsi w NextWeek.py 22 lat i mlodsi
        young.append(f)
            
for i in range(10):
    for pl in young:
        rrr = randrange(1000*len(young))
        #print(pl)
        #print(rrr,' - ',chance,'/',1000*len(young),'\n')

        if chance >= rrr:
            data.playerTeam[data.playerTeam.index(pl)][0] = int(data.playerTeam[data.playerTeam.index(pl)][0])
            data.playerTeam[data.playerTeam.index(pl)][0] += 1
            print(data.GetName(data.playerTeam[data.playerTeam.index(pl)])+' improved his skill!')
            print('Age:',int(data.playerTeam[data.playerTeam.index(pl)][4]))
            input('Now his skill is '+str(data.playerTeam[data.playerTeam.index(pl)][0]))

#AKTUALIZACJA - NEW SEASON
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

#YOUTH ACADEMY
def HowGood(lv):
    if lv+50 > randrange(100):
        if lv+25 > randrange(100):
            if lv+10 > randrange(100):
                if lv+8 > randrange(100):
                    if lv+7 > randrange(100):
                        if lv+6 > randrange(100):
                            if lv+5 > randrange(100):
                                if lv+4 > randrange(100):
                                    return 9
                                else:
                                    return 8
                            else:
                                return 7
                        else:
                            return 6
                    else:
                        return 5
                else:
                    return 4
            else:
                return 3
        else:
            return 2
    else:
        return 1

def PrintAcademy(academy):
    print('*'*50,'\n')
    for y in academy:
        print(data.GetName(y),'\tAge:',y[4],' Position:',y[3],' Skill:',y[0])
    print('\n'+('*'*50))

print("\n" * data.freeSpace)
if data.youthAcademyLv > 0:
    print('YOUR YOUTH ACADEMY ANNUAL SUMMARY')
    print('\nYouth academy level:',data.youthAcademyLv)
    print('\nNow you will see players from your Youth academy')
    print('You will decide to give each of them senior contract or not')
    n = int((data.youthAcademyLv+5)/5)
    if n == 0:
        n = 1
    if n > 5:
        n = 5

    input('\ncontinue\n')

    academy = []
    positions = ['GKP','DEF','DEF','MID','MID','ATK','ATK']
    for q in range(n):
        newP = CreateNewPlayer.CreateNewPlayer(HowGood(data.youthAcademyLv),positions[randrange(len(positions))],'England')
        academy.append(newP)
    
    for i in academy:
        if academy[academy.index(i)][4] > 18:
            academy[academy.index(i)][4] = 16
    
    for z in academy:
        print("\n" * data.freeSpace)
        PrintAcademy(academy)
        print('\nDo you want to sign',data.GetName(z),'?')

        #young player fee
        n = int(z[0])
        youngFee = int( (n*n/2+0.5) * randrange(70,130)/10 )
        if youngFee == 0:
            youngFee = 1
        print('You will have to pay him ',youngFee,'000')
        print('your budget: '+str(data.budget)+' 000')
        
        print('\n Type "yes" or "no". If you do not sign him he will look for some other club and will not be longer avaliable')
        inp = input()
        while not inp in ('yes','no'):
            inp = input('Type only "yes" or "no"\n')

        if inp == 'yes':
            if data.budget >= youngFee:
                data.budget -= youngFee
                print('\nCongratulations on signing ',data.GetName(z),'!')
                print('He is very happy about starting trainings with your first team\n')
                data.playerTeam.append(z)
            else:
                print('your budget: '+str(data.budget)+' 000')
                print('\nYou do not have enough money to sign '+data.GetName(z)+'.')
                print('\nYou do not signed contract with',data.GetName(z))
        else:
            print('\nYou do not signed contract with',data.GetName(z))

        input('continue\n')
        
else:
    print('You do not build your youth academy yet! You do not recive any players.')
    print('Establish your youth academy as soon as possible to recive young talents every season!')
    input('\ncontinue\n')

#INJURIES AND STAMINA
print("\n" * data.freeSpace)
print("It's holidays time! I hope you enjoy your vacations!")
print('Your players also take a rest. Now their stamina is 10')
if data.injuried:
    print('During the summer break following players heal theirs injuries:')
    for p in data.injuried:
        p[7] = 1
        data.playerTeam.append(p)
        print(data.GetName(p))
        
    data.injuried = []
    
else:
    print('You do not have any injuried players so they cant heal')
    
for i in data.playerTeam:
    data.playerTeam[data.playerTeam.index(i)][7] = 10

input('\ncontinue\n')



#players age
for i in data.playerTeam:
    data.playerTeam[data.playerTeam.index(i)][4] = int(i[4])
    data.playerTeam[data.playerTeam.index(i)][4] += 1



# YEAR
data.year += 1




#END OF PLAYER'S CARRIERS
print("\n" * data.freeSpace)
for i in data.playerTeam:
    if int(i[4]) > randrange(34,37):
        print(data.GetName(i),'is ending his football career')
        print('Age:',i[4],'Skill:',i[0],'Position:',i[3],'Nationality:',i[6])
        print()
        if int(i[8]) > 0:
            print('He played',i[8],'matches for your club')
        if int(i[9]) > 0:
            print('Score',i[9],'goals')
        if int(i[10]) > 0:
            print('Assist',i[10],'times')

        data.PlayersOfAllTheTime.append([data.GetName(i)+"\t- Position: "+i[3]+'\t\tplayed: '+str(i[8])+'\tscored: '+str(i[9])+'\tassists: '+str(i[10]),int(i[8])])
        
        data.playerTeam.remove(i)
        input('\ncontinue\n')

#SPONSOR
if not data.sponsorDeal[0] == '':
    print("\n" * data.freeSpace)
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
    print ('Your sponsor',data.sponsorDeal[0]+' wants to continue partnership with your club')
    print ('"'+data.sponsorDeal[0]+'" company will pay you',data.sponsorDeal[1],'000 a week')
    print ("Only thing you have to do is to carry their logo on your club's shirts")
    inp = input ('\n1 - accept offer\n2 - reject offer\n')
    while not inp in ('1','2'):
        inp = input('Type "1" or "2"\n')
    if inp == '2':
        print ("\n" * data.freeSpace)
        print ('"'+data.sponsorDeal[0]+'" company will pay you',data.sponsorDeal[1],'000 a week')
        print ('\nAre you completly sure, you want to reject this offer?')
        print ('And wait for some better offerts')
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
            print ('Congratulations! You have just renew your sponsorship contract with "'+data.sponsorDeal[0]+'" company!')
            input ('\ncontinue\n')



#PLAYERS WORTH
for i in data.playerTeam:
    i[4] = int(i[4])
    if i[4] <= 26:
        ageModifier = i[4]/10
    elif i[4] == 27:
        ageModifier = 2.4
    elif i[4] == 28:
        ageModifier = 2.2
    elif i[4] == 29:
        ageModifier = 2.0
    elif i[4] == 30:
        ageModifier = 1.8
    elif i[4] == 31:
        ageModifier = 1.6
    elif i[4] == 32:
        ageModifier = 1.4
    elif i[4] == 33:
        ageModifier = 1.2
    elif i[4] == 34:
        ageModifier = 1.0
    else:
        ageModifier = 0.8
    
    r = randrange(91, 110)
    marketValue = round(int(i[0]) * int(i[0]) * r * ageModifier)
    
    data.playerTeam.remove(i)
    i[5] = marketValue
    data.playerTeam.append(i)

from time import sleep
print("\n" * data.freeSpace)
print('preparing to the new season...')
sleep(randrange(6,12)/10)
print("\n" * data.freeSpace)

print ("Saving data...")
data.ExportData()
sleep(0.5)

data.ImportData()#jest error po okienku kiedy chce sortowac zawodnikow

exec(open("MainMenu.py").read())
