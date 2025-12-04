import data

print ("\n" * data.freeSpace)

Id = data.fNums.index(data.formation)
print ('\nYOUR FORMATION: ',data.fName[Id],'\n')

data.printFormation(data.formation)

print('\n1 - chose new formation')
print('0 - back')

inp = input('\nChose number\n')
while not inp in ('1','0'):
    inp = input('\nType correct number\n')

if inp == '1':
    inp2 = '0'
    while inp2 != '1':
        print ("\n" * data.freeSpace)
        n = 1
        for i in data.fName:
            if n < 10:
                print (n,' - formation ',i)
            else:
                print (n,'- formation ',i)
            n += 1
        print ('\nTIP: If you want to play with more forward players chose offensive formations')
        print ('\nchose formation for preview or 0 to exit\n')
        inp = input()
        while not inp in ('0','1','2','3','4','5','6','7','8','9','10','11','12','13'):
            inp = input('Type correct number\n')
        if inp == '0':
            exec(open("ChangeFormation.py").read())
        else:
            previewedFormation = data.fName[int(inp)-1]
            print ("\n" * data.freeSpace)
            print ('*** ',previewedFormation.upper(),' ***')
            iD = data.fName.index(previewedFormation)
            data.printFormation(data.fNums[iD])

            inp2 = input('\n1 - set formation\n0 - back\n')
            while not inp2 in ('1','0'):
                inp2 = input('\nType correct number')
            if inp2 == '1':
                data.formation = data.fNums[iD]
                data.goalkeeper = []
                data.defenders = []
                data.midfielders = []
                data.atackers = []
                exec(open("EditTeam.py").read())

if inp == '0':
    exec(open("EditTeam.py").read())
