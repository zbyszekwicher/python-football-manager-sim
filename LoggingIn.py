import data
import os
from time import sleep
print ("\n" * data.freeSpace)

try:
    file = open(data.path + '\\saves\\' + data.clubName)
    try:
        whoCreate = file.readlines()[0].replace("\n", "")
    finally:
        file.close()
except IOError:
    print("Opening files error")

if whoCreate == data.playerName:
    print ("You have already created club called '" + data.clubName + "'.")
    print ("You can use it, overwrite it or remove")
    inp = input('use/overwrite/remove\n')
    while not inp in ('use','overwrite','remove'):
        inp = input("incorrect answer. Type 'use', 'overwrite' or 'remove'")
    if inp == 'overwrite':
        print ('This will delete your progress. Are you sure, you want to overwrite?')
        inp = input('yes/no\n')
        while not inp in ('yes','no'):
            inp = input("incorrect answer. Type 'yes' or 'no'")
        if inp == 'yes':
            print ("\n" * data.freeSpace)
            print ("Your new club " + data.clubName + " will start in English National League!")
            exec(open("CreateNewTeam.py").read())
            sleep(0.5)
            input("\n continue\n")
            exec(open("NewSeason.py").read())
            data.ExportData()
            
        else:
            exec(open("LoggingIn.py").read())

    elif inp == 'remove':
        print ('This will delete all your progress. Are you sure, you want to remove?')
        inp = input('yes/no\n')
        while not inp in ('yes','no'):
            inp = input("incorrect answer. Type 'yes' or 'no'")
        if inp == 'yes':
            print ("\n" * data.freeSpace)
            try:
                os.remove(data.path+'\\saves\\'+data.clubName)
                print ('your '+data.clubName+' was removed')
                data.clubName = ''
            except:
                print ('There was an error. Your club cannot be removed')
            input("\n continue\n")
            exec(open("GameStarter.py").read())
            
        else:
            exec(open("LoggingIn.py").read())
            
    else:
        print('importing data...')
        data.ImportData()
        data.autopick()
        sleep(0.5)
        exec(open("MainMenu.py").read())
        
else:
    print("There is already club called '" + data.clubName + "' created by other user. \nYou cannot use it")
    sleep(0.5)
    inp = input('\ncontinue\n')
    exec(open("GameStarter.py").read())
