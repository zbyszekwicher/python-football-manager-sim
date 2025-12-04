import data
from time import sleep
import os
#import sys

directory = data.path+'\\saves\\'

pName = ''
saved = []
for filename in os.listdir(directory):
#	if filename.endswith(".py"):
    filePath = (os.path.join(directory+filename))
    try:
        file = open(filePath)
        try:
            all_lines = file.readlines()
            pName = all_lines[0].replace("\n", "")
        finally:
            file.close()

    except IOError:
        print("Opening files error")

    #print (filename)
    #print (pName)
    #print (data.playerName)
    if pName == data.playerName:
        saved.append(filename)


print("\n" * data.freeSpace)

if len(saved) > 0:
    print ('account: ', data.playerName)
    print ('\nYOUR SAVED CLUBS NAMES:')
    for i in saved:
        print (i)
    print ('\nYou can type name of your previus club or create new one\n')
else:
    print ('account: ', data.playerName)
    print('\nYou do not have any saved clubs yet\n')

print('0 - back')

""" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - """
data.budget = 1000
data.playerLeague = data.national_league
data.playerLeague_name = 'National League'

data.clubName = ''
#print ("Hi " + data.playerName + "!")
while data.clubName == '':
    data.clubName = input("Type club name \n")

if data.clubName == '0':
    data.playerName = ''
    exec(open("_FFManager_app.py").read())

else:

    data.stadiumName = data.clubName+' Stadium'

    if data.IsFile(data.clubName):
        exec(open("LoggingIn.py").read())
    else:
        print("\n" * data.freeSpace)
        print ('Are you sure you want to create a new team called "'+data.clubName+'"?')
        inp = 'nothing'
        while not inp in ('yes','no'):
            inp = input('type "yes"/"no" \n')
        if inp == 'no':
            print("\n" * data.freeSpace)
            exec(open("GameStarter.py").read())
        else:
            
            print ("Your new club " + data.clubName + " will start in English National League!")

            exec(open("CreateNewTeam.py").read())

            sleep(0.5)
            input("\n continue\n")
            exec(open("NewSeason.py").read())

