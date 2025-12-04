from sys import exit
import data
from time import sleep
print ("\n" * data.freeSpace)
inp = input ('Do you want to save your progress before exit?\n(yes/no)\n')
while not inp in ('yes','no'):
    inp = input('Type "yes" or "no"')
if inp == 'yes':
    print ("\n" * data.freeSpace)
    print ("Saving data...")
    data.ExportData()
    sleep(0.5)

    print ("\n" * data.freeSpace)
    print ('Your progress is saved as "'+data.clubName+'" create by "'+data.playerName+'".')
    print ('REMEMBER! that if you want to use your saved club you have to log in as '+data.playerName)
    input("\nexit\n")

exit()
