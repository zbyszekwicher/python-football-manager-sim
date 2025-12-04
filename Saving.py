import data
from time import sleep

print ("\n" * data.freeSpace)
print ("Saving data...")
data.ExportData()
#data.ImportData()      ewentualnie zeby wszystkie zmienne sie zrobily dobrze ulozyly nowi pilkarze szczegolnie
sleep(0.5)

print ("\n" * data.freeSpace)
print ('Your progress is saved as "'+data.clubName+'" create by "'+data.playerName+'".')
print ('REMEMBER! that if you want to use your saved club you have to log in as '+data.playerName)
input("\ncontinue\n")

exec(open("MainMenu.py").read())
