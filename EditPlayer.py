import data
from string import ascii_letters

print ("\n" * data.freeSpace)

index = data.playerId - 1
player = data.playerTeam[index]

isCorrect = False
while isCorrect == False:
    print('\nType new name for player '+data.GetName(player).upper()+' or 0 to exit')
    inp = input()

    if inp == '0':
        exec(open("PlayerDetails.py").read())
    else:
        avaliableSigns = ascii_letters+' '
        isCorrect = True
        for i in inp:
            if not i in avaliableSigns:
                isCorrect = False

        if isCorrect:
            if len(inp.split()) <= 3:
                if len(inp) <= 20:
                    print('your name is correct')
                else:
                    print('Your name is correct but too long. Type less letters')
                    isCorrect = False
            else:
                print('Your name is correct but too long. Type less words')
                isCorrect = False

        else:
            print('your name is incorrect. Use only english letters')

inp2 = input('Are you sure you want to overwrite name of player '+data.GetName(player).upper()+' to '+inp.upper()+'?\nChanges cannot be removed\n(yes/no)\n')

while not inp2 in ('yes','no'):
    inp2 = input('type "yes" or "no"\n')

if inp2 == 'yes':
    newName = inp.split()[0]
    newSurname = ' '.join(inp.split()[1:])
    data.playerTeam[index][1] = newName
    data.playerTeam[index][2] = newSurname
    exec(open("PlayerDetails.py").read())
else:
    exec(open("PlayerDetails.py").read())


