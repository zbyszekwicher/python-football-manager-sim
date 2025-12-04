import data


data.teamDefalutSort()  #??


print ("\n" * data.freeSpace)
print ("MAIN MENU\n")
print (" *** " + data.clubName + " *** ")
print ("Budget: " + str(data.budget)+' 000')
print ("Year: " + str(data.year))
print ("Game week: " + str(data.gameWeek))
print ("\n1 - fixtures and league")
print ("2 - team")
print ("3 - yor club")
print ('4 - finances')
print ("5 - safe your progress")
print ('Type "exit" to exit')
print
if data.gameWeek == 0:
    print ('\nType "next" to continue to next week (transfer window)')
elif data.gameWeek > len(data.fixtures):
    print ('\nType "next" to continue to next week (end of the season)')
else:
    print ('\nType "next" to continue to next week (mach against '+data.fixtures[data.gameWeek-1][0]+')')

inp = input("\nchose option\n")
correctAnswers = ("1", "2", "3",'4','5', "next",'exit')
while inp not in correctAnswers:
    inp = input("That is not a correct answer! Type number of option you want to chose\n")
    
if inp == "1":
    exec(open("FixturesAndLeague.py").read())
elif inp == "2":
    exec(open("EditTeam.py").read())
elif inp == "3":
    exec(open("EditClub.py").read())
elif inp == '4':
    exec(open("Finances.py").read())
elif inp == "5":
    exec(open("Saving.py").read())
elif inp == 'exit':
    exec(open("exit.py").read())
else:
    exec(open("NextWeek.py").read())
