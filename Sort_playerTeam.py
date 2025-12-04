import data

print ("\n" * data.freeSpace)
print ('1 - sort by surname')
print ('2 - sort by skill')
print ('3 - sort by position')
print ('4 - sort by age')
print ('5 - sort by market value')
print ('6 - sort by stamina')

correctAnswers = ('1','2','3','4','5','6')
inp = input('Type numer (1-6)\n')

while not inp in correctAnswers:
    inp = input('Type numer (1-6)\n')

if inp == '1':
    data.playerTeam.sort(key=lambda x: x[2])
elif inp == '2':
    data.playerTeam.sort(key=lambda x: int(x[0]))
    data.playerTeam.reverse()
elif inp == '3':
    sorting = data.playerTeam
    data.playerTeam = []
    for i in sorting:
        if i[3] == 'GKP':
            data.playerTeam.append(i)
    for i in sorting:
        if i[3] == 'DEF':
            data.playerTeam.append(i)
    for i in sorting:
        if i[3] == 'MID':
            data.playerTeam.append(i)
    for i in sorting:
        if i[3] == 'ATK':
            data.playerTeam.append(i)
elif inp == '4':
    data.playerTeam.sort(key=lambda x: int(x[4]))
elif inp == '5':
    for i in data.playerTeam:
        if len(str(i[5])) == 4:
            i[5] = ' '+str(i[5])
        elif len(str(i[5])) == 3:
            i[5] = '  '+str(i[5])
        elif len(str(i[5])) == 2:
            i[5] = '   '+str(i[5])
    data.playerTeam.sort(key=lambda x: int(x[5]))
    data.playerTeam.reverse()

elif inp == '6':
    for i in data.playerTeam:
        if int(i[7]) != 10:
            data.playerTeam[data.playerTeam.index(i)][7] = '0'+str(i[7])
        else:
            data.playerTeam[data.playerTeam.index(i)][7] = str(i[7])
    data.playerTeam.sort(key=lambda x: int(x[7]))
    data.playerTeam.reverse()
    for i in data.playerTeam:
        data.playerTeam[data.playerTeam.index(i)][7] = int(i[7])

exec(open("EditTeam.py").read())
