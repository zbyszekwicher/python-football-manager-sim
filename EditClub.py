import data
inp = 0
inp2 = 0

print ("\n" * data.freeSpace)
print ("EDIT CLUB\n")
print ('1 - stadium\t\tcapacity:',data.stadiumCapacity)
print ('2 - training ground\tlevel\t',data.trainingGroundLv)
#print ('3 - medical facilities\tlevel\t',data.medicalFacilitiesLv)
print ('3 - youth academy\tlevel\t',data.youthAcademyLv)
print ('4 - club info')
print ('5 - hall of fame')
print ('6 - players stats')
print ('0 - back')

inp = input("\nchose option\n")
correctAnswers = ("1", "2", "3",'4',"0",'5','6')
while inp not in correctAnswers:
    inp = input("That is not a correct answer! Type number of option you want to chose\n")

if inp == "1":
    while inp == '1':
        print ("\n" * data.freeSpace)
        print (data.stadiumName.upper())
        print ('Capacity:',data.stadiumCapacity)
        print ('TIP: Bigger stadium means more fans and more money')
        
        inp2 = input('\n1 - build new stadium\n2 - change stadium name\n0 - back\n')
        while not inp2 in ('1','2','0'):
            inp2 = input('Type correct number\n')
        if inp2 == '0':
            exec(open("EditClub.py").read())
        elif inp2 == '2':
            from string import ascii_letters,digits
            print ("\n" * data.freeSpace)
            print('Current stadium name: ',data.stadiumName)

            enoughMoney = True
            if data.stadiumSponsored == 1:
                print('\n If you want to change the stadium name you have to pay 1000 000 compensation')
                if data.budget < 1000:
                    enoughMoney = False
            if data.stadiumSponsored == 2:
                print('\n If you want to change the stadium name you have to pay 5000 000 compensation')
                if data.budget < 5000:
                    enoughMoney = False

            if enoughMoney:
                print('\nType new name for your stadium or 0 to exit')
                isCorrect = False
                while isCorrect == False:
                    inp = input()

                    if inp == '0':
                        exec(open("EditClub.py").read())
                    else:
                        avaliableSigns = ascii_letters+" "+digits
                        isCorrect = True
                        for i in inp:
                            if not i in avaliableSigns:
                                isCorrect = False

                        if isCorrect:
                            if len(inp) <= 30:
                                print('your name is correct')
                            else:
                                print('Your name is correct but too long. Type less letters')
                                isCorrect = False

                        else:
                            print("your name is incorrect. Use only english letters and numbers")


                if data.stadiumSponsored == 1:
                    print('\n Cost: 1000 000')
                if data.stadiumSponsored == 2:
                    print('\n Cost: 5000 000')
                
                inp2 = input('Are you sure you want to overwrite name of stadium '+data.stadiumName.upper()+' to '+inp.upper()+'?\nChanges cannot be removed\n(yes/no)\n')

                while not inp2 in ('yes','no'):
                    inp2 = input('type "yes" or "no"\n')

                if inp2 == 'yes':
                    data.stadiumName = inp
                    exec(open("EditClub.py").read())
                else:
                    exec(open("EditClub.py").read())
            else:
                input('\n You do not have enough money \n continue \n')
                exec(open("EditClub.py").read())
                
                
        elif inp2 == '1':
            while inp2 == '1':
                print ("\n" * data.freeSpace)
                print ('Your budget: ',data.budget,'000')
                print ('Your current stadium capacity: ',data.stadiumCapacity,'\t')
                
                print ('If you want to build new stadium type its capacity.\nIt must be bigger than your current capacity and lower than 100 000')
                print ('Or type 0 to exit')
                print ('Type new stadium capacity')
                isInt = False
                isCorrect = False
                while not isCorrect:
                    while not isInt:
                        cap = input()                    
                        try:
                            cap = int(cap)
                            if isinstance(cap,int):
                                isInt = True
                        except:
                            print ('Type only numbers')

                    if cap == 0 or (cap < 100000 and cap > int(data.stadiumCapacity)):
                        isCorrect = True
                    else:
                        print ('Type number from '+str(data.stadiumCapacity+1)+' to 99999')
                        isInt = False

                if cap == 0:
                    inp2 = ''
                else:
                    print ("\n" * data.freeSpace)
                    print ('Your budget: ',data.budget,'000\n')
                    cost = int((cap*data.newStadiumCostModifier)/10)
                    print ('Your new stadium of ',cap,' capacity will cost you ',cost,'000')
                    correctAnswers = ['0']
                    if cost <= data.budget:
                        print('You can afford to buy this stadium. Type "buy" if you decide or 0 to exit')
                        correctAnswers.append('buy')
                    else:
                        print('You cannot afford to buy this stadium. Type 0 to exit')
                    inp3 = input()
                    while not inp3 in correctAnswers:
                        inp3 = input('incorrect input\n')
                    if inp3 == '0':
                        pass
                    else:
                        print ("\n" * data.freeSpace)
                        data.stadiumCapacity = cap
                        data.budget -= cost
                        data.addToFinances(-cost,data.budget,'New stadium '+str(cap)+' capacity')
                        print ('Congratulations! You have just built a new stadium!')
                        print ('Name:\t',data.stadiumName)
                        print ('Capacity:\t',data.stadiumCapacity)
                        input ('Countinue\n')
                        exec(open("EditClub.py").read())
        
elif inp == "2":
    while inp == '2':
        print ("\n" * data.freeSpace)
        print ('Your budget: ',data.budget,'000\n')
        print ('TRAINING GROUND LEVEL:',data.trainingGroundLv)
        print ('TIP: Biggest training ground level means more chances for players to improve')

        if data.trainingGroundLv == 100:
            input('Your training ground is at the max level. You cant upgrade it any further\ncontinue\n')
            exec(open("EditClub.py").read())
        else:
            cost = int(data.trainingGroundLv*2.45)
            print('\nupgrading training ground to level ',data.trainingGroundLv+1,'will cost you ',cost,'000')
            print('new weekly maintenance cost will be', int((data.trainingGroundLv+1)/10*4+1),'000')
            print('\n1 - upgrade training ground\n0 - back\n')
            inp2 = input()
            while not inp2 in ('1','0'):
                inp2 = input('type correct number\n')
            if inp2 == '0':
                exec(open("EditClub.py").read())
            elif inp2 == '1':
                if cost <= data.budget:
                    print ("\n" * data.freeSpace)
                    data.trainingGroundLv += 1
                    data.budget -= cost
                    data.addToFinances(-cost,data.budget,'Training ground upgrade to level '+str(data.trainingGroundLv))
                    print ('Congratulations! You have just upgrade your training ground to level ',data.trainingGroundLv,'!')
                    input ('continue\n')
                else:
                    print ("\n" * data.freeSpace)
                    input ('Unfortunately you do not have enough money\n')
                                        
elif inp == "3":
    while inp == '3':
        print ("\n" * data.freeSpace)
        print ('Your budget: ',data.budget,'000\n')
        if data.youthAcademyLv == 0:
            print ('You do not have a youth accademy yet. Maybe build one?')
        else:
            print ('YOUTH ACADEMY LEVEL:',data.youthAcademyLv)
        print ('TIP: Youth academy will give you young players for your team. Bigger youth academy level means more and better young talents for your team')

        if data.youthAcademyLv == 100:
            input('Your youth academy is on the max level. You cant upgrade it any further\ncontinue\n')
            exec(open("EditClub.py").read())
        elif data.youthAcademyLv == 0:
            cost = 100
            print('\nEstabilishing your youth academy will cost you ',cost,'000')
            print('\n1 - build youth academy\n0 - back\n')
            inp2 = input()
            while not inp2 in ('1','0'):
                inp2 = input('type correct number\n')
            if inp2 == '0':
                exec(open("EditClub.py").read())
            elif inp2 == '1':
                if cost <= data.budget:
                    print ("\n" * data.freeSpace)
                    data.youthAcademyLv += 1
                    data.budget -= cost
                    data.addToFinances(-cost,data.budget,'Estabilishing youth academy')
                    print ('Congratulations! You have just establish your youth academy. Now its on level ',data.youthAcademyLv,'!')
                    input ('continue\n')
                else:
                    print ("\n" * data.freeSpace)
                    input ('Unfortunately you do not have enough money\n')
        else:
            cost = int(data.youthAcademyLv*2.55)
            print('\nupgrading youth academy to level ',data.youthAcademyLv+1,'will cost you ',cost,'000')
            print('new weekly maintenance cost will be', int((data.youthAcademyLv+1)/10*4+1),'000')
            print('\n1 - upgrade youth academy\n0 - back\n')
            inp2 = input()
            while not inp2 in ('1','0'):
                inp2 = input('type correct number\n')
            if inp2 == '0':
                exec(open("EditClub.py").read())
            elif inp2 == '1':
                if cost <= data.budget:
                    print ("\n" * data.freeSpace)
                    data.youthAcademyLv += 1
                    data.budget -= cost
                    data.addToFinances(-cost,data.budget,'Youth academy upgrade to level '+str(data.youthAcademyLv))
                    print ('Congratulations! You have just upgrade your youth academy to level ',data.youthAcademyLv,'!')
                    input ('continue\n')
                else:
                    print ("\n" * data.freeSpace)
                    input ('Unfortunately you do not have enough money\n')
                    
elif inp == "4":
    while inp == '4':
        print ("\n" * data.freeSpace)
        print ('Club name:\t\t',data.clubName)
        print ('Club owner (your name):\t',data.playerName)
        print ('Stadium name:\t\t',data.stadiumName)
        print ('Stadium capacity:\t',data.stadiumCapacity)
        playersValue = 0
        for i in data.playerTeam:
            playersValue += int(i[5])
        print('Total players value:\t',playersValue,' 000')
        if data.sponsorDeal[0] == '':
            print('You do not have a sponsor contract')
        else:
            print('Sponsor:\t\t'+data.sponsorDeal[0])
        print('\nTIP: If you want to open your previously saved progress, you will have to type your name, so do not forget it.')
        print('\n1 - change club name')
        print('2 - change your nickname (club owner name)')
        print('0 - back')
        print('TIP: if you want to change stadium name, go to stadium in edit club')
        inp2 = input()
        if inp2 == '0':
            exec(open("EditClub.py").read())
        elif inp2 == '1':
            print ("\n" * data.freeSpace)
            x = input('Type new club name\n')
            print ('Are you sure you want to change club name "'+data.clubName+'" to "'+x+'"?')
            inp3 = input('yes/no\n')
            while not inp3 in ('yes','no'):
                inp3 - input('Type "yes" or "no"')
            if inp3 == 'yes':
                data.clubName = x
                print ('Your club name was changed to "'+data.clubName+'"')
                input ('continue')
        
        elif inp2 == '2':
            print ("\n" * data.freeSpace)
            x = input('Type your new nickname\n')
            print ('Are you sure you want to change nickname "'+data.playerName+'" to "'+x+'"?')
            print ('Remember, that you need this name if you want to load this club data')
            inp3 = input('yes/no\n')
            while not inp3 in ('yes','no'):
                inp3 - input('Type "yes" or "no"')
            if inp3 == 'yes':
                data.playerName = x
                print ('Your nickname was changed to "'+data.playerName+'"')
                print ('do not forget it if you want to load your progress')
                input ('continue')

elif inp == "5":
    print ("\n" * data.freeSpace)
    if data.hallOfFame == []:
        print("you don't have any trophies yet")

    else:
        for i in data.hallOfFame:
            print (i)
        print ()

    input('continue\n')
    exec(open("EditClub.py").read())
    
elif inp == "6":
    print ("\n" * data.freeSpace)
    print ('PLAYERS OF ALL THE TIME')
    full = []
    for i in data.PlayersOfAllTheTime:
        full.append(i)

    for i in data.playerTeam:
        full.append([data.GetName(i)+"\t- Position: "+i[3]+'\t\tplayed: '+str(i[8])+'\tscored: '+str(i[9])+'\tassists: '+str(i[10]),int(i[8])])

    full.sort(key=lambda x: int(x[1]))
    full.reverse()

    for i in full:
        print(i[0])

    
    #wszyscy gracze, ktorzy ever grali w klubie
    input('continue\n')
    exec(open("EditClub.py").read())
    
else:
    exec(open("MainMenu.py").read())

