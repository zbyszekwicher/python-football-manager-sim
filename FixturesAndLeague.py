import data

print ("\n" * data.freeSpace)
print ("FIXTURES AND LEAGUE\n")
print ("You are playing in  " + data.playerLeague_name)
print ("Played: "+str(data.played)+". Your league position: "+str(data.leaguePosition))
print ("WIN: "+str(data.win)+", DRAW: "+str(data.draw)+", LOSE: "+str(data.lose)+". Points: "+str(data.points))
print ("\n1 - Show fixtures")
print ("\n0 - Main menu")
inp = input("\nchose option\n")
correctAnswers = ("1", "0")
while inp not in correctAnswers:
    inp = input("That is not a correct answer! Type number of option you want to chose\n")
    
if inp == "1":
    exec(open("ShowFixtures.py").read())
elif inp == "0":
    exec(open("MainMenu.py").read())
