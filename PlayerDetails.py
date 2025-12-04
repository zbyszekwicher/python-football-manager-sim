import data
from random import randrange

firstTeam = data.goalkeeper+data.defenders+data.midfielders+data.atackers

print ("\n" * data.freeSpace)
index = data.playerId - 1
player = data.playerTeam[index]
print (" *** ", data.GetName(player).upper(), " *** \n")

print ('Nationality: \t '+player[6])

if player[3] == "GKP":
	print("Position: \t", "goalkeeper")
elif player[3] == "DEF":
	print("Position: \t", "defender")
elif player[3] == "MID":
	print("Position: \t", "midfielder")
elif player[3] == "ATK":
	print("Position: \t", "forward")

print ("Skill: \t\t",  player[0])
print ("Stamina: \t",  player[7])
print ("Age: \t\t", player[4])
print ("Market Value:\t", int(player[5]),'000')

x = int(player[0])
fee = int( (x*x/2+0.5) * randrange(70,130)/10 )
if fee == 0:
        fee = 1
print ("Season fee: \t "+str(fee)+' 000')

print ()
print ('matches played:\t',player[8])
print ('goals scored:\t',player[9])
print ('assists scored:\t',player[10])

if player in firstTeam:
	print ("\n1 - put player out of the first team")
	inFirstTeam = True
else:
	print ("\n1 - put player into the first team")
	inFirstTeam = False

print('2 - edit player\tFUNCTION DISABLED')
print('3 - dismiss player\tFUNCTION DISABLED')

inp = input("\nchose option or 0 to exit\n")
correctAnswers = ("0",'1')

while inp not in correctAnswers:
    inp = input("That is not a correct answer! Type number of option you want to chose\n")
if inp == "0":
    exec(open("EditTeam.py").read())
elif inp == '1':
        if inFirstTeam:
                if player in data.goalkeeper:
                        data.goalkeeper.remove(player)
                elif player in data.defenders:
                        data.defenders.remove(player)
                elif player in data.midfielders:
                        data.midfielders.remove(player)
                elif player in data.atackers:
                        data.atackers.remove(player)
        else:
                print ("\n" * data.freeSpace)
                print (" *** ", data.GetName(player).upper(), " *** \n")
                print ('On which position you want to put '+data.GetName(player)+'?')

                if player[3] == "GKP":
                        print ("He gives his best while playing as goalkeeper")
                elif player[3] == "DEF":
                        print ("He gives his best while playing as defender")
                elif player[3] == "MID":
                        print ("He gives his best while playing as midfielder")
                elif player[3] == "ATK":
                        print ("He gives his best while playing as forward")
                        
                print ('Type:')
                print ('1 - goalkeeper')
                print ('2 - defender')
                print ('3 - midfielder')
                print ('4 - atacker')
                
                inp2 = input()
                while not inp2 in ('1','2','3','4'):
                        inp2 = input('wrong input\n')
                        

                if inp2 == "1":
                        if len(data.goalkeeper) < 1:
                                data.goalkeeper.append(player)
                        else:
                                print ('\nYou already have a goalkeeper.\nFirstly you have to remove him from the first team\ncontinue')

                                print('1) '+data.GetName(data.goalkeeper[0])+" skill: "+str(data.goalkeeper[0][0])+" stamina: "+str(data.goalkeeper[0][7]))

                                print('Type 1 to replace player, or 0 to cancel')
                                inp3 = input('')
                                while int(inp3) not in (0,1):
                                        inp3 = input('wrong input, type number of player, or 0 to cancel')

                                if int(inp3) == 1:
                                        print('replacing ', data.goalkeeper[0], 'with', player)
                                        data.goalkeeper = []
                                        data.goalkeeper.append(player)
                                else:
                                        exec(open("PlayerDetails.py").read())

                elif inp2 == "2":
                        if len(data.defenders) < data.formation[0]:
                                data.defenders.append(player)
                        else:
                                print('\nYou already have '+ str(data.formation[0])+' defenders.\nFirstly you have to remove someone from the first team')
                                print('You can also try changing formation')
                                ind = 1
                                for p in data.defenders:
                                        print(str(ind)+') '+data.GetName(p)+" skill: "+str(p[0])+" stamina: "+str(p[7]))
                                        ind += 1

                                print('Type number of player you want to replace, or 0 to cancel')
                                inp3 = input('')
                                while int(inp3) not in range(ind):
                                        inp3 = input('wrong input, type number of player, or 0 to cancel')

                                if int(inp3) > 0:
                                        print('replacing ', data.defenders[int(inp3) - 1], 'with', player)
                                        data.defenders[int(inp3) - 1] = player
                                else:
                                        exec(open("PlayerDetails.py").read())

                elif inp2 == "3":
                        if len(data.midfielders) < data.formation[1]:
                                data.midfielders.append(player)
                        else:
                                print('\nYou already have '+ str(data.formation[1])+' midfielders.\nFirstly you have to remove someone from the first team')
                                print('You can also try changing formation')
                                ind = 1
                                for p in data.midfielders:
                                        print(str(ind)+') '+data.GetName(p)+" skill: "+str(p[0])+" stamina: "+str(p[7]))
                                        ind += 1

                                print('Type number of player you want to replace, or 0 to cancel')
                                inp3 = input('')
                                while int(inp3) not in range(ind):
                                        inp3 = input('wrong input, type number of player, or 0 to cancel')

                                if int(inp3) > 0:
                                        print('replacing ', data.midfielders[int(inp3) - 1], 'with', player)
                                        data.midfielders[int(inp3) - 1] = player
                                else:
                                        exec(open("PlayerDetails.py").read())

                elif inp2 == "4":
                        if len(data.atackers) < data.formation[2]:
                                data.atackers.append(player)
                        else:
                                
                                print('\nYou already have '+ str(data.formation[2])+' atackers.\nFirstly you have to remove someone from the first team')
                                print('You can also try changing formation')
                                ind = 1
                                for p in data.atackers:
                                        print(str(ind)+') '+data.GetName(p)+" skill: "+str(p[0])+" stamina: "+str(p[7]))
                                        ind += 1

                                print('Type number of player you want to replace, or 0 to cancel')
                                inp3 = input('')
                                while int(inp3) not in range(ind):
                                        inp3 = input('wrong input, type number of player, or 0 to cancel')

                                if int(inp3) > 0:
                                        print('replacing ', data.atackers[int(inp3) - 1], 'with', player)
                                        data.atackers[int(inp3) - 1] = player
                                else:
                                        exec(open("PlayerDetails.py").read())

                                
        exec(open("EditTeam.py").read())

elif inp == '2':
        exec(open("EditPlayer.py").read())
elif inp == '3':
        print('\nAre you sure you want to dismiss ',data.GetName(player),'?')
        print('He will not be longer avaliable in your team')
        comp = int((int(player[0])*int(player[0])/2+0.5) * 10)
        print('also you have to pay him',comp,'000 compensation\n')
        inp2 = input('type "dismiss" to pay and dismiss\ntype "0" to go back\n')
        while inp2 not in ('dismiss','0'):
                inp2 = input('type only "dismiss" or "0"')
        if inp2 == '0':
                exec(open("PlayerDetails.py").read())
        elif inp2 == 'dismiss':
                print ("\n" * data.freeSpace)
                print ('You dismissed ',data.GetName(player),'and payed him ',comp,'000')
                data.budget -= comp
                print ('Your budget:',data.budget)
                data.playerTeam.remove(player)
                input('\ncontinue\n')
                exec(open("EditTeam.py").read())
