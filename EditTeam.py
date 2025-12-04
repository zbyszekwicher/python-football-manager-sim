import data

print ("\n" * data.freeSpace)
print ("*** FIRST TEAM ***")
print ('TIP: team strenght depends on players skill, stamina and if they are playing on their positions')

iD = data.fNums.index(data.formation)
print ('FORMATION:',data.fName[iD])
if len(data.goalkeeper+data.defenders+data.midfielders+data.atackers) == 11:
        defendStr = data.GetTeamPower()[0]
        atackStr = data.GetTeamPower()[1]
        print ('TEAM DEFENCE STRENGHT:',defendStr)
        print ('TEAM ATACK  STRENGHT:',atackStr,'\n')

if len(data.atackers+data.midfielders+data.defenders+data.goalkeeper) < 11:
        print(' '*9+'*YOUR FIRST TEAM IS NOT FULL*\n')

data.printFirstTeam()
firstTeam = data.goalkeeper+data.defenders+data.midfielders+data.atackers

print("\n\nALL YOUR PLAYERS")
for i in data.playerTeam:
        if len(str(i[5])) == 4:
            i[5] = ' '+str(i[5])
        elif len(str(i[5])) == 3:
            i[5] = '  '+str(i[5])
        elif len(str(i[5])) == 2:
            i[5] = '   '+str(i[5])
#txt = ''
for i in data.playerTeam:
        index = data.playerTeam.index(i)+1
        if index < 10:
                index = ' '+str(index)
        if i in firstTeam:
                txt = '\t*IN FIRTS TEAM*'
        else:
                txt = ''
        print(str(index)+") "+data.GetName(i)+"\t- Position: "+i[3]+" skill: "+str(i[0])+" stamina: "+str(i[7])+txt)  #+" age: "+str(i[4]))   #+" value: "+str(i[5])+' 000'

if data.injuried:
        print('\nINJURIED PLAYERS')
        for i in data.injuried:
                print(data.GetName(i)+'\tInjuried')
7        

correctAnswers = ["0",'sort','autopick','formation']
for i in range(len(data.playerTeam)):
	correctAnswers.append(str(i + 1))

recomended = ''
if data.goalkeeper == [] and data.defenders == [] and data.midfielders == [] and data.atackers == []:
        recomended = ' *RECOMMENDED*'
inp = input('\nChose player or 0 to go back.\nIf you want to sort players type "sort"\nIf you want to auto pick players to first team type "autopick"'+recomended+'\nIf you want to edit your formation type "formation"\n')
while inp not in correctAnswers:
	inp = input("That is not a correct answer! Type number of option you want to chose\n")

if inp == "0":
    exec(open("MainMenu.py").read())
elif inp == 'sort':
        exec(open("Sort_playerTeam.py").read())
elif inp == 'autopick':
        data.autopick()
        data.teamDefalutSort()  ####
        exec(open("EditTeam.py").read())
elif inp == 'formation':
        exec(open("ChangeFormation.py").read())
else:
    data.playerId = int(inp)
    exec(open("PlayerDetails.py").read())
    
