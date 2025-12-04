from random import randrange
import os
import sys
#path = os.path.dirname(sys.argv[0])
path = os.path.dirname(os.path.abspath(__file__))

def GetTeamPower():
    d = []
    a = []
    for i in goalkeeper:
        if i[3] != 'GKP':
            skill = 0
        else:
            skill = int(i[0])
        d.append(skill*10)#*((int(i[7])+10)/2))
        
    for i in defenders:
        if i[3] != 'DEF':
            if i[3] == 'MID':
                skill = 0.8*int(i[0])
            elif i[3] == 'GKP':
                skill = 0.5
            else:
                skill = 0.5*int(i[0])
        else:
            skill = int(i[0])
        d.append(skill*10)#*((int(i[7])+10)/2))
        
    for i in midfielders:
        if i[3] != 'MID':
            skill = 0.8*int(i[0])
        elif i[3] == 'GKP':
                skill = 0.5
        else:
            skill = int(i[0])
        a.append(skill*10)#*((int(i[7])+10)/2))

    for i in atackers:
        if i[3] != 'ATK':
            if i[3] == 'MID':
                skill = 0.8*int(i[0])
            elif i[3] == 'GKP':
                skill = 0.5
            else:
                skill = 0.5*int(i[0])
        else:
            skill = int(i[0])
        a.append(skill*10)#*((int(i[7])+10)/2))
        
    return [int((sum(d)/5)),int((sum(a)/6))]

def GetName(player):
    x = player[1] + " " + player[2]
    if len(x) < 15:
        if len(x) == 14:
            x = x+' '
        elif len(x) == 13:
            x = x+'  '
        elif len(x) == 12:
            x = x+'   '
        elif len(x) == 11:
            x = x+'    '
        elif len(x) == 10:
            x = x+'     '
        elif len(x) == 9:
            x = x+'      '
        elif len(x) == 8:
            x = x+'       '
        elif len(x) == 7:
            x = x+'        '
    return x


def IsFile(name):
    #dataPath = path + '\\saves\\' + name
    dataPath = os.path.join(path, 'saves', name)

    if os.path.exists(dataPath):
        return True
    else:
        return False

def ExportData():
    #dataPath = path + '\\saves\\' + clubName
    dataPath = os.path.join(path, 'saves', clubName)
    
    file = open(dataPath, 'w')
    
    file.write(playerName)
    file.write('\n')
    file.write(clubName)
    file.write('\n')
    file.write(str(budget))
    file.write('\n')
    for i in playerLeague:
        file.write(str(i) + ';')
    file.write('\n')
    
    file.write(str(gameWeek))
    file.write('\n')
    for i in fixtures:
        file.write(str(i) + ';')
    file.write('\n')
    file.write(str(win))
    file.write('\n')
    file.write(str(draw))
    file.write('\n')
    file.write(str(lose))
    file.write('\n')
    file.write(str(played))
    file.write('\n')
    file.write(str(points))
    file.write('\n')
    file.write(str(leaguePosition))
    file.write('\n')

    for l in playerTeam:
        for i in l:
            file.write(str(i) + ',')
        file.write(';')
    file.write('\n')

    for l in goalkeeper:
        for i in l:
            file.write(str(i) + ',')
        file.write(';')
    file.write('\n')
    for l in defenders:
        for i in l:
            file.write(str(i) + ',')
        file.write(';')
    file.write('\n')
    for l in midfielders:
        for i in l:
            file.write(str(i) + ',')
        file.write(';')
    file.write('\n')
    for l in atackers:
        for i in l:
            file.write(str(i) + ',')
        file.write(';')
    file.write('\n')

    file.write(str(playerLeague_name))
    file.write('\n')

    file.write(str(formation))
    file.write('\n')

    file.write(str(stadiumCapacity))
    file.write('\n')
    file.write(str(trainingGroundLv))
    file.write('\n')
#    file.write(str(medicalFacilitiesLv))
#    file.write('\n')
    file.write(str(youthAcademyLv))
    file.write('\n')

#    for i in finances:
#        file.write(str(i) + ';')
#    file.write('\n')

    for i in sponsorDeal:
        file.write(str(i) + ';')
    file.write('\n')

    for l in injuried:
        for i in l:
            file.write(str(i) + ',')
        file.write(';')
    file.write('\n')

    file.write(str(year))
    file.write('\n')

    for h in hallOfFame:
        file.write(str(h) + ';')
    file.write('\n')

    for l in PlayersOfAllTheTime:
        for i in l:
            file.write(str(i) + ',')
        file.write(';')
    file.write('\n')
    
    
    file.close()

def ImportData():
    global playerName
    global clubName
    global budget
    global playerLeague
    global gameWeek
    global fixtures
    global win
    global draw
    global lose
    global played
    global points
    global leaguePosition
    global playerTeam
    global goalkeeper
    global defenders
    global midfielders
    global atackers
    global playerLeague_name
    global formation
    global stadiumCapacity
    global trainingGroundLv
#    global medicalFacilitiesLv
    global youthAcademyLv
#    global finances
    global sponsorDeal
    global injuried
    
    global year
    global hallOfFame
    global PlayersOfAllTheTime

    #dataPath = path + '\\saves\\' + clubName
    dataPath = os.path.join(path, 'saves', clubName)
    data = []
    try:
        file = open(dataPath)
        try:
            for line in file:
                data.append(line.replace("\n", ""))            
        finally:
            file.close()

    except IOError:
        print("Opening files error")
    
    playerName = data[0]
    clubName = data[1]
    budget = int(data[2])
    playerLeague = []
    l = data[3].replace("[", "").replace(']', '').split(';')
    l.remove('')
    for i in l:
        item = i.replace("'","")
        item = item.split(',')
        item[1] = float(item[1])
        playerLeague.append(item)

    fixtures = []
    l = data[5].replace("[", "").replace(']', '').split(';')
    l.remove('')
    for i in l:
        item = i.replace("'","")
        item = item.split(',')
        item[1] = float(item[1])
        fixtures.append(item)        
    gameWeek = int(data[4])
    win = int(data[6])
    draw = int(data[7])
    lose = int(data[8])
    played = int(data[9])
    points = int(data[10])
    leaguePosition = int(data[11])

    playerTeam = []
    list1 = data[12].split(';')
    list1.remove('')
    for i in list1:
        item = i.split(',')
        item.remove('')
        item[4] = int(item[4])
        playerTeam.append(item)

    goalkeeper = []
    list1 = data[12].split(';')
    list1.remove('')
    for i in list1:
        item = i.split(',')
        item.remove('')
        goalkeeper.append(item)

    defenders = []
    list1 = data[13].split(';')
    list1.remove('')
    for i in list1:
        item = i.split(',')
        item.remove('')
        defenders.append(item)

    midfielders = []
    list1 = data[14].split(';')
    list1.remove('')
    for i in list1:
        item = i.split(',')
        item.remove('')
        midfielders.append(item)
    
    atackers = []
    list1 = data[15].split(';')
    list1.remove('')
    for i in list1:
        item = i.split(',')
        item.remove('')
        atackers.append(item)


    playerLeague_name = data[17]

    formation = []
    formation.append(int(data[18][1]))
    formation.append(int(data[18][4]))
    formation.append(int(data[18][7]))

    stadiumCapacity = int(data[19])
    trainingGroundLv =int(data[20])
#    medicalFacilitiesLv = int(data[21])
    youthAcademyLv = int(data[21])

#    finances = data[22].split(';')
    sponsorDeal = data[22].split(';')

    if data[23] != []:
        injuried = []
        list1 = data[23].split(';')
        list1.remove('')
        for i in list1:
            item = i.split(',')
            item.remove('')
            injuried.append(item)

    year = int(data[24])

    if data[25] != []:
        hallOfFame = []
        listx = data[25].split(';')
        listx.remove('')
        for i in listx:
            hallOfFame.append(i)

#    if data[26] != []:
#        PlayersOfAllTheTime = []
#        listx = data[26].split(';')
#        listx.remove('')
#        for i in listx:
#            PlayersOfAllTheTime.append(i)

    PlayersOfAllTheTime = []
    list1 = data[26].split(';')
    list1.remove('')
    for i in list1:
        item = i.split(',')
        item.remove('')
        PlayersOfAllTheTime.append(item)


def teamDefalutSort():
    global playerTeam

    #sort players by skill
    playerTeam.sort(key=lambda x: int(x[0]))
    playerTeam.reverse()
    #and now sort players by position
    sorting = playerTeam
    playerTeam = []
    for i in sorting:
        if i[3] == 'GKP':
            playerTeam.append(i)
    for i in sorting:
        if i[3] == 'DEF':
            playerTeam.append(i)
    for i in sorting:
        if i[3] == 'MID':
            playerTeam.append(i)
    for i in sorting:
        if i[3] == 'ATK':
            playerTeam.append(i)



def autopick():


    #autopick
    players = []
    for i in playerTeam:
        players.append(i)
        
    for i in players:
        players[players.index(i)].insert(100,int(i[0])*10)
    
    players.sort(key=lambda x: x[-1])
    players.reverse()

    for i in players:
        i.reverse()
        i.remove(i[0])
        i.reverse()            
    
    global goalkeeper
    global defenders
    global midfielders
    global atackers
    
    goalkeeper = []
    for i in players:
        if i[3] == 'GKP' and len(goalkeeper) < 1 and int(i[7]) > 4:
            goalkeeper.append(i)

    defenders = []
    for i in players:
        if i[3] == 'DEF' and len(defenders) < formation[0] and int(i[7]) > 4:
            defenders.append(i)

    midfielders = []
    for i in players:
        if i[3] == 'MID' and len(midfielders) < formation[1] and int(i[7]) > 4:
            midfielders.append(i)

    atackers = []
    for i in players:
        if i[3] == 'ATK' and len(atackers) < formation[2] and int(i[7]) > 4:
            atackers.append(i)
            
    
    for i in players:   #give goalkeepers at the end of the list
        if i[3] == 'GKP':
            players.remove(i)
            players.append(i)
    for i in players:   #give midfielders at the begining of the list
        if i[3] == 'MID':
            players.remove(i)
            players.insert(0,i)
    for i in players:
        if int(i[7]) < 3:#nie dodawaj takich
            #print(i)
            players.remove(i)
        if int(i[7]) == 3:#daj takich na koniec listy
            players.remove(i)
            players.append(i)
    
    firstTeam = goalkeeper+defenders+midfielders+atackers
    
    if len(atackers) < formation[2]:
        for i in players:
            if i not in firstTeam:
                atackers.append(i)
                if len(atackers) == formation[2]:
                    break

    if len(defenders) < formation[0]:
        for i in players:
            if i not in firstTeam:
                defenders.append(i)
                if len(defenders) == formation[0]:
                    break

    if len(midfielders) < formation[1]:
        for i in players:
            if i not in firstTeam:
                midfielders.append(i)
                if len(midfielders) == formation[1]:
                    break
    
    if len(goalkeeper) < 1:
        for i in players:
            if i not in firstTeam:
                goalkeeper.append(i)
                if len(goalkeeper) == 1:
                    break

def addToFinances(income,total,desc):#WYLACZONE
    #global finances
    
    #txt = str(income)+' 000   \t'+str(total)+' 000   \t '+desc
    #finances.append(txt)
    print()

def Injuries():
    if injuried:
        if randrange(5) == 0:
            p = injuried[0]
            injuried.remove(p)
            p[7] = 1
            playerTeam.append(p)
            print(GetName(p),'Heal his injury!')
            print('Now his stamina is 1.')
            input('\ncontinue\n')
    
    for i in playerTeam:
        if int(i[7]) < 1:
            playerTeam.remove(i)
            injuried.append(i)
    for i in goalkeeper:
        if i in injuried:
            goalkeeper.remove(i)
    for i in defenders:
        if i in injuried:
            defenders.remove(i)
    for i in midfielders:
        if i in injuried:
            midfielders.remove(i)
    for i in atackers:
        if i in injuried:
            atackers.remove(i)

#   ＮＯＴＥＳ
#   w dodawaniu pilkarzy do pierwszego skladu dodac zeby mozna bylo wybrac pilkarza
#   ktorego chce sie zamienic
#   usunac zmienna played. zamiast niej uzywac gameWeek
#   dodac gole strzelone stracone

#   lista.index("element listy") - zwraca index elementu
#   \t - dodaje tab
playerId = 1#used for PlayerDetails
newStadiumCostModifier = 2.63
# ＤＡＴＡＢＡＳＥ  

freeSpace = 49 #40 works fine BUT I'LL GIVE MORE
averageSkill = 2 #starting player team strenght
#2 musi byc

#variables
hallOfFame = []
PlayersOfAllTheTime = []

#GameStarter
year = 2022
playerName = ''
clubName = ''
stadiumName = ''
budget = 0
finances = []
addToFinances(+1000,1000,'Beggining budget')
playerLeague = []
playerLeague_name = ''
tickets = {'National League':3,'League Two':3.5,'League One':4,'Championship':4.5,'Premier League':5}

#NewSeason
sponsorDeal = ['',0]
gameWeek = 0
fixtures = []
win = 0
draw = 0
lose = 0
played = 0
points = 0
leaguePosition = 0

#CreateNewTeam
playerTeam = []
injuried = []

#EditTeam
goalkeeper = []
defenders = []
midfielders = []
atackers = []

#EditClub
stadiumCapacity = 2000
trainingGroundLv = 1
#medicalFacilitiesLv = 1
youthAcademyLv = 0

#Match
matchResult = ''

#max dlugosc imion i nazwisk to 7 liter.
#min dlugosc nazwiska i imienia - 4 litery, jesli 3 literowe imie dodaj spacje
playerNameENG = ['Aaron', 'Abraham', 'Absalom', 'Adam', 'Addison', 'Adel', 'Adolf', 'Adrian', 'Albert', 'Alec', 'Alex', 'Alfred', 'Alvin', 'Andrew', 'Andy', 'Anthony', 'Antony', 'Archie', 'Arlo', 'Arnaut', 'Arnold', 'Arthur', 'Ashley', 'Austen', 'Austin', 'Baron', 'Basil', 'Bayard', 'Bernard', 'Bertram', 'Blake', 'Bobby', 'Booth', 'Brad', 'Brian', 'Brock', 'Brooks', 'Bryan', 'Bubba', 'Bubby', 'Buck', 'Byron', 'Caleb', 'Callum', 'Calvin', 'Cardew', 'Carl', 'Carlie', 'Carlton', 'Carroll', 'Cary', 'Chad', 'Chance', 'Chandos', 'Charl', 'Charlee', 'Charley', 'Charli', 'Charlie', 'Charly', 'Chas', 'Chaz', 'Chazz', 'Chet', 'Chip', 'Chris', 'Chucky', 'Claire', 'Clare', 'Claude', 'Clay', 'Cleve', 'Cliff', 'Clint', 'Colby', 'Cole', 'Colin', 'Collin', 'Colman', 'Coloman', 'Colton', 'Conway', 'Corbin', 'Corey', 'Curtis', 'Curtley', 'Dallas', 'Damien', 'Damon', 'Dana', 'Daniel', 'Danny', 'Darby', 'Darren', 'David', 'Davy', 'Delbert', 'Derek', 'Derrick', 'Dexter', 'Dickon', 'Dirk', 'Dobie', 'Donald', 'Doug', 'Dougie', 'Douglas', 'Drew', 'Duncan', 'Dwight', 'Dylan', 'Eadwulf', 'Earl', 'Eddie', 'Edgar', 'Edmund', 'Edward', 'Edwin', 'Elbert', 'Elias', 'Elliot', 'Ellwood', 'Elmer', 'Elton', 'Emil', 'Erastus', 'Eric', 'Ernest', 'Ethan', 'Evelyn', 'Ezekiel', 'Fabian', 'Felix', 'Floyd', 'Francis', 'Frank', 'Gabriel', 'Gale', 'Galton', 'Gareth', 'Garth', 'Gary', 'Gavin', 'George', 'Gerald', 'Gerard', 'Gilbert', 'Glen', 'Gorden', 'Gordon', 'Graham', 'Grant', 'Grayson', 'Gregory', 'Griffin', 'Hank', 'Harold', 'Harry', 'Henry', 'Herbert', 'Herman', 'Hervey', 'Hilary', 'Hope', 'Horace', 'Howard', 'Hubert', 'Hudson', 'Hugh', 'Hugo', 'Hunter', 'Isaac', 'Jack', 'Jackie', 'Jackson', 'Jacob', 'Jaime', 'Jake', 'James', 'Jamie', 'Jared', 'Jason', 'Jasper', 'Jeb', 'Jeff', 'Jeffery', 'Jeffrey', 'Jeremy', 'Jerome', 'Jerry', 'Jess', 'Jesse', 'Jimmy', 'Jodie', 'Joel', 'Joey', 'John', 'Johnny', 'Johnson', 'Jolyon', 'Jonah', 'Jonas', 'Jordan', 'Jordie', 'Jordy', 'Joseph', 'Josh', 'Joshua', 'Julian', 'Justin', 'Keith', 'Kelsey', 'Kenneth', 'Kenny', 'Kevin', 'Kian', 'Kimble', 'Kurt', 'Kyle', 'Lanny', 'Larry', 'Laurie', 'Lawton', 'Leonard', 'Leopold', 'Leslie', 'Lester', 'Lewis', 'Lindsay', 'Linus', 'Louis', 'Lucas', 'Luther', 'Lyle', 'Lyndsay', 'Malachi', 'Malcolm', 'Mandy', 'Manuel', 'Marcus', 'Mark', 'Martin', 'Marvin', 'Mason', 'Matt', 'Matthew', 'Maurice', 'Melvin', 'Melvyn', 'Merle', 'Merlin', 'Michael', 'Miles', 'Milo', 'Morgan', 'Murray', 'Myron', 'Nate', 'Nathan', 'Neil', 'Newt', 'Newton', 'Nicolas', 'Nolan', 'Norman', 'Nowell', 'Oliver', 'Orlando', 'Osbert', 'Oscar', 'Osric', 'Oswald', 'Otis', 'Otto', 'Owen', 'Palmer', 'Patrick', 'Patsy', 'Paul', 'Peleg', 'Pete', 'Peter', 'Philip', 'Quentin', 'Raife', 'Ralph', 'Ramsey', 'Randall', 'Raymond', 'Rendell', 'Reuben', 'Rich', 'Richie', 'Ricky', 'Robbie', 'Robert', 'Robin', 'Rodger', 'Rodney', 'Roger', 'Rogers', 'Ronald', 'Ronnie', 'Roscoe', 'Ross', 'Rowland', 'Rufus', 'Rupert', 'Russell', 'Samuel', 'Sanford', 'Sean', 'Seth', 'Shahaf', 'Shane', 'Shannon', 'Shaun', 'Shawn', 'Shayne', 'Sigmund', 'Simon', 'Skyler', 'Spencer', 'Stanley', 'Stefan', 'Stephen', 'Steve', 'Stevie', 'Swaine', 'Taran', 'Tate', 'Terence', 'Terry', 'Thomas', 'Timmy', 'Timothy', 'Tobias', 'Toby', 'Tommie', 'Tony', 'Tracy', 'Travis', 'Trevor', 'Tristan', 'Troy', 'Tyler', 'Tyrone', 'Ultan', 'Ulysses', 'Vicary', 'Victor', 'Vince', 'Vincent', 'Walden', 'Waldo', 'Walter', 'Wayne', 'Whitney', 'Wilfred', 'William', 'Wilmon', 'Winnie', 'Winston', 'Wyndham', 'Zadoc']
playerSurnameENG = ['Aaron', 'Aarons', 'Abbey', 'Abbot', 'Abbott', 'Acheson', 'Ackroyd', 'Adcock', 'Adin', 'Adkin', 'Adkins', 'Adlam', 'Adlard', 'Adley', 'Adshead', 'Afford', 'Aiken', 'Aikin', 'Aimson', 'Ainslie', 'Aitch', 'Aizer', 'Akam', 'Akroyd', 'Alan', 'Alcorn', 'Alden', 'Allard', 'Allison', 'Allitt', 'Allred', 'Allum', 'Almond', 'Altman', 'Amberg', 'Ambler', 'Amory', 'Annon', 'Anstead', 'Anstey', 'Anthony', 'Arbour', 'Arch', 'Archer', 'Ardley', 'Ardron', 'Arliss', 'Arnold', 'Artell', 'Arthur', 'Artley', 'Ascroft', 'Ashbee', 'Ashby', 'Ashdown', 'Asplin', 'Astle', 'Astley', 'Atkin', 'Atkins', 'Atlee', 'Auger', 'Austen', 'Auster', 'Austin', 'Avey', 'Aveyard', 'Awford', 'Axford', 'Axon', 'Axtell', 'Axton', 'Aykroyd', 'Aymes', 'Ayres', 'Ayris', 'Ayrton', 'Babbage', 'Babbs', 'Bacuzzi', 'Badley', 'Bagshaw', 'Bailie', 'Baily', 'Bain', 'Baines', 'Baker', 'Ball', 'Bambra', 'Bamford', 'Barber', 'Barker', 'Barkley', 'Barley', 'Barnet', 'Barnett', 'Barry', 'Barton', 'Bartrop', 'Basford', 'Bassham', 'Bastock', 'Bates', 'Bateup', 'Batey', 'Batley', 'Batton', 'Batts', 'Bawden', 'Baxter', 'Bayer', 'Bayles', 'Baynton', 'Bayntun', 'Beacham', 'Beadon', 'Beal', 'Beale', 'Beamont', 'Beard', 'Beasant', 'Beaton', 'Beavers', 'Beck', 'Beckley', 'Beddow', 'Bedford', 'Bedser', 'Beeby', 'Beeks', 'Beer', 'Beere', 'Beevers', 'Begley', 'Bell', 'Bellett', 'Bellows', 'Bence', 'Benett', 'Bennett', 'Benson', 'Bentley', 'Benton', 'Berker', 'Berry', 'Best', 'Bestall', 'Bethell', 'Bethune', 'Betmead', 'Bettney', 'Bickle', 'Bidder', 'Bidmead', 'Bigden', 'Biggins', 'Biggs', 'Bignot', 'Bigwood', 'Billman', 'Bimpson', 'Bimson', 'Bingley', 'Bird', 'Birrell', 'Bishop', 'Biswell', 'Black', 'Blair', 'Blake', 'Blalock', 'Blant', 'Blight', 'Bloomer', 'Blyth', 'Blythe', 'Bomer', 'Bomford', 'Bonsor', 'Boot', 'Booth', 'Boothby', 'Boothe', 'Booze', 'Bostick', 'Bostock', 'Bott', 'Bow', 'Bowers', 'Bowes', 'Bowie', 'Bowles', 'Bowyer', 'Brabin', 'Bracey', 'Brack', 'Bradley', 'Bragg', 'Bramble', 'Bramley', 'Brandis', 'Braxton', 'Brayton', 'Brazier', 'Brewer', 'Brewill', 'Brimson', 'Broady', 'Bronson', 'Brookes', 'Brooks', 'Broom', 'Brower', 'Brown', 'Bruce', 'Bubb', 'Buckler', 'Buckley', 'Bugden', 'Bull', 'Burdon', 'Burgess', 'Burk', 'Burke', 'Burks', 'Burney', 'Burnham', 'Burns', 'Bush', 'Butcher', 'Butter', 'Butters', 'Byers', 'Byrd', 'Bysshe', 'Bywater', 'Cadman', 'Caferro', 'Calle', 'Calnan', 'Camden', 'Campion', 'Caple', 'Capron', 'Carder', 'Carell', 'Carnell', 'Carrell', 'Case', 'Caton', 'Cauley', 'Cawley', 'Chapman', 'Chaucer', 'Chesney', 'Chew', 'Chin', 'Chinn', 'Chow', 'Chriss', 'Clapham', 'Clapton', 'Clark', 'Cleland', 'Clerk', 'Cliburn', 'Clopton', 'Cloud', 'Clower', 'Clowers', 'Clowney', 'Coates', 'Coats', 'Cobham', 'Coburn', 'Coffin', 'Colborn', 'Colburn', 'Collins', 'Colvin', 'Combe', 'Conlee', 'Conly', 'Connell', 'Conway', 'Cook', 'Cooke', 'Cooksey', 'Cooling', 'Coombes', 'Coon', 'Cooper', 'Coppock', 'Corbett', 'Corbin', 'Corin', 'Corrie', 'Cotman', 'Cotton', 'Coull', 'Cowell', 'Cowman', 'Cramton', 'Crerar', 'Crier', 'Crofts', 'Crosbie', 'Crosby', 'Crossan', 'Crowley', 'Cruddas', 'Cruise', 'Cruse', 'Crute', 'Cryer', 'Culver', 'Curren', 'Currie', 'Cusden', 'Cushing', 'Cust', 'Dalman', 'Dane', 'Daneman', 'Danson', 'Darwin', 'Daw', 'Dawber', 'Dawkins', 'Dawson', 'Dean', 'Debney', 'Deeks', 'Deller', 'Dering', 'Derwin', 'Devall', 'Devoe', 'Dewell', 'Dewing', 'Diamond', 'Dickons', 'Dicks', 'Dilley', 'Dines', 'Dingley', 'Dinning', 'Diprose', 'Dixon', 'Dobb', 'Dobbs', 'Dobson', 'Docwra', 'Dodwell', 'Donelan', 'Donovan', 'Douch', 'Dowd', 'Dowdall', 'Dowden', 'Dowding', 'Down', 'Downer', 'Downing', 'Downs', 'Dowson', 'Drake', 'Driver', 'Dudding', 'Duerk', 'Duke', 'Dungey', 'Dunham', 'Dunn', 'Dyal', 'Dyson', 'Eady', 'Eagle', 'Eakin', 'Eakins', 'Eatman', 'Eaton', 'Ebanks', 'Eddy', 'Edwards', 'Edwin', 'Egerton', 'Eidson', 'Elwes', 'Emerson', 'Emery', 'England', 'English', 'Evelyn', 'Every', 'Exton', 'Farlow', 'Farmer', 'Farrar', 'Farrow', 'Farwell', 'Faucit', 'Fearon', 'Feasey', 'Feek', 'Feetham', 'Ferrier', 'Finch', 'Finn', 'Finnis', 'Fish', 'Fisher', 'Flake', 'Flatley', 'Fleck', 'Fleming', 'Flower', 'Flowers', 'Foat', 'Folwell', 'Ford', 'Forrest', 'Forster', 'Fowler', 'Foxen', 'Franks', 'French', 'Frith', 'Froud', 'Frye', 'Fuller', 'Gannis', 'Garrad', 'Gaskin', 'Gates', 'Gawley', 'Gayfer', 'Gayford', 'Geddes', 'Genge', 'Getson', 'Gibbon', 'Gibbs', 'Gibson', 'Giffen', 'Gilbert', 'Giles', 'Gillick', 'Ginger', 'Glanton', 'Glasby', 'Glavin', 'Glover', 'Godfrey', 'Goff', 'Gofton', 'Goggin', 'Gold', 'Gooding', 'Goodman', 'Goodson', 'Goodway', 'Goodwin', 'Goodwyn', 'Goring', 'Gotts', 'Gould', 'Gowler', 'Graeme', 'Graham', 'Granger', 'Graves', 'Greaves', 'Green', 'Greene', 'Gregg', 'Greig', 'Grist', 'Groover', 'Groves', 'Gundy', 'Gunn', 'Gunton', 'Guthrie', 'Gwatkin', 'Hackett', 'Hackman', 'Hadley', 'Haigh', 'Haines', 'Haley', 'Hall', 'Halley', 'Hallman', 'Halsey', 'Hamer', 'Hamill', 'Hammond', 'Hampson', 'Hamshaw', 'Hancock', 'Hanson', 'Hardy', 'Harenc', 'Harker', 'Harman', 'Harmon', 'Harold', 'Harp', 'Harper', 'Harrold', 'Hart', 'Harvard', 'Harvie', 'Haslem', 'Hassell', 'Hatton', 'Hawke', 'Hawker', 'Hawkes', 'Hawking', 'Hawkins', 'Hawks', 'Hawley', 'Hayden', 'Hayes', 'Haylen', 'Hayward', 'Haywood', 'Hazell', 'Headley', 'Heaney', 'Hebb', 'Hector', 'Hembree', 'Henman', 'Henson', 'Hepburn', 'Heron', 'Herring', 'Herson', 'Hervey', 'Heston', 'Hewitt', 'Hewlett', 'Hewson', 'Heywood', 'Hicks', 'Hiett', 'Higgins', 'Higham', 'Hill', 'Hixon', 'Hixson', 'Hodgson', 'Hogan', 'Holborn', 'Holcomb', 'Holder', 'Holiday', 'Holland', 'Holt', 'Hom', 'Hood', 'Hooker', 'Hoole', 'Hooley', 'Hooper', 'Hopkins', 'Horler', 'Hornby', 'Horner', 'Hornsby', 'Houchen', 'Howard', 'Howell', 'Hubbard', 'Hudnall', 'Hudson', 'Hunt', 'Hunter', 'Huxley', 'Hyland', 'Inglis', 'Ingram', 'Inskip', 'Irwin', 'Isler', 'Isley', 'Ivens', 'Jacklin', 'Jackson', 'Jacobs', 'Jeal', 'Jemison', 'Jent', 'Jephson', 'Jepson', 'Jessop', 'Jetton', 'Jewell', 'Johns', 'Johnson', 'Jolley', 'Jonas', 'Jones', 'Joplin', 'Joseph', 'Jowett', 'Jupp', 'Kane', 'Keach', 'Keers', 'Keith', 'Kells', 'Kelly', 'Kent', 'Kenyon', 'Kersey', 'Kershaw', 'Kettle', 'Keysor', 'Kinchen', 'King', 'Kingaby', 'Kington', 'Kitchen', 'Kitt', 'Kitts', 'Klahn', 'Knaggs', 'Knight', 'Knott', 'Kovac', 'Kovacec', 'Kovacev', 'Kovach', 'Kovacic', 'Kovacik', 'Kraabel', 'Kyle', 'Laidley', 'Lainson', 'Lake', 'Lamble', 'Lamp', 'Lampkin', 'Lane', 'Lang', 'Langton', 'Lard', 'Laslett', 'Laster', 'Laws', 'Lawson', 'Lawton', 'Lawyer', 'Layton', 'Leach', 'Leavitt', 'Ledger', 'Lemer', 'Lennon', 'Levett', 'Levick', 'Lewis', 'Leyton', 'Light', 'Lillard', 'Lind', 'Lineker', 'Linnell', 'Linney', 'Linwood', 'Lister', 'Liston', 'Little', 'Lively', 'Loar', 'Loates', 'Lock', 'Locke', 'Loder', 'Lolley', 'Love', 'Lovejoy', 'Lovell', 'Lovely', 'Lovett', 'Loving', 'Lowe', 'Lowitt', 'Lucey', 'Lucy', 'Lukis', 'Lulham', 'Luntley', 'Lusher', 'Lyle', 'Mackall', 'Maddux', 'Malgham', 'Malghum', 'Malyon', 'Manly', 'Manning', 'Marris', 'Marsden', 'Marsh', 'Martin', 'Mason', 'Massey', 'Maxwell', 'Mayhall', 'Mayor', 'McAuley', 'McCloud', 'McCouch', 'McCann', 'McGann', 'McKeand', 'McKenna', 'McKeown', 'Mebane', 'Medwin', 'Melton', 'Merritt', 'Michele', 'Miller', 'Milley', 'Mills', 'Milner', 'Milnes', 'Moat', 'Monk', 'Monroe', 'Moore', 'Morris', 'Morton', 'Mosley', 'Mossey', 'Mote', 'Mousley', 'Muchnic', 'Mullen', 'Muller', 'Mursell', 'Myers', 'Nance', 'Nash', 'Nathan', 'Natt', 'Nealey', 'Nelmes', 'Nelson', 'Netter', 'Nettles', 'Newbold', 'Newey', 'Niccol', 'Nicholl', 'Nickson', 'Nicol', 'Nihill', 'Nixon', 'Noakes', 'Nolan', 'Norris', 'Noyce', 'Noyes', 'Nuttall', 'Nutter', "O'Dell", 'Oatway', 'Odell', "O'Hagan", 'Orlebar', 'Orpen', 'Orton', 'Osborne', 'Ottley', 'Ousey', 'Oxley', 'Padden', 'Page', 'Paget', 'Paige', 'Painter', 'Palfrey', 'Palmer', 'Pancake', 'Pankey', 'Pappin', 'Parham', 'Parker', 'Parkes', 'Parnell', 'Parrot', 'Parrott', 'Pastor', 'Pateman', 'Patrick', 'Paul', 'Paulson', 'Paynter', 'Payton', 'Peabody', 'Penfold', 'Perch', 'Pertwee', 'Peters', 'Pettit', 'Pettitt', 'Petty', 'Phelps', 'Philips', 'Phipps', 'Phipson', 'Phoenix', 'Pickard', 'Pickett', 'Pidgeon', 'Pierce', 'Pike', 'Piper', 'Pippen', 'Piston', 'Platt', 'Plumb', 'Podmore', 'Pointon', 'Poland', 'Pollock', 'Polmans', 'Ponting', 'Pool', 'Porter', 'Potter', 'Powers', 'Poynter', 'Prime', 'Pun', 'Purdon', 'Purves', 'Pynchon', 'Pyne', 'Qualls', 'Quarrie', 'Quealy', 'Quelch', 'Querrey', 'Quill', 'Quimby', 'Quintal', 'Ramsey', 'Randall', 'Randel', 'Ranford', 'Ratliff', 'Rawling', 'Ray', 'Rayment', 'Rayner', 'Raynor', 'Reader', 'Reading', 'Reckord', 'Record', 'Rector', 'Redding', 'Redish', 'Redner', 'Reeder', 'Reilley', 'Reiner', 'Rendell', 'Renshaw', 'Reston', 'Richard', 'Ridge', 'Ridings', 'Robson', 'Rodham', 'Rolt', 'Romney', 'Rood', 'Rose', 'Rosena', 'Ross', 'Roth', 'Round', 'Rouse', 'Rowan', 'Rowell', 'Rudner', 'Runcie', 'Rundle', 'Russell', 'Ryan', 'Ryeland', 'Rykener', 'Sage', 'Salem', 'Sales', 'Salmon', 'Salmons', 'Saltman', 'Sammon', 'Sammons', 'Sanders', 'Sands', 'Sarchet', 'Sawyer', 'Saxon', 'Scotten', 'Scriver', 'Scrubb', 'Scruton', 'Seaborn', 'Seacole', 'Seals', 'Seymour', 'Shairp', 'Sharp', 'Sharpe', 'Shave', 'Sherman', 'Shersby', 'Shipton', 'Shipway', 'Short', 'Shown', 'Shum', 'Sibley', 'Sickler', 'Sidney', 'Simm', 'Simon', 'Simons', 'Simpson', 'Simson', 'Siviter', 'Skaife', 'Skeete', 'Skelly', 'Skey', 'Skippon', 'Slocumb', 'Slowey', 'Smith', 'Snowden', 'Somers', 'Sorey', 'Sorley', 'Souttar', 'Spain', 'Sparks', 'Sparrow', 'Speakes', 'Spencer', 'Spicer', 'Spittle', 'Spooner', 'Spratt', 'Squire', 'Squires', 'Stanley', 'Stanton', 'Stark', 'Starkey', 'Starks', 'Stepney', 'Stern', 'Stetson', 'Stevens', 'Stilley', 'Stobart', 'Stone', 'Stookey', 'Stough', 'Stuart', 'Stuckey', 'Sugrue', 'Sumner', 'Swaine', 'Swan', 'Swanton', 'Sweeney', 'Swinton', 'Sydney', 'Tanner', 'Tate', 'Teasley', 'Tebbutt', 'Thaxter', 'Thaxton', 'Thomas', 'Thomson', 'Thorn', 'Thorpe', 'Thring', 'Thwaite', 'Tidwell', 'Tidy', 'Tiffany', 'Tiffen', 'Tillard', 'Tinsley', 'Tittle', 'Toner', 'Tonra', 'Toogood', 'Topp', 'Torbett', 'Torney', 'Towry', 'Tozer', 'Travers', 'Traviss', 'Traynor', 'Treweek', 'Trotman', 'Trout', 'Trull', 'Trump', 'Truss', 'Tubbs', 'Tucker', 'Tuckman', 'Tuson', 'Tuttle', 'Tutton', 'Twyman', 'Tyndale', 'Tyndall', 'Ultan', 'Umpleby', 'Updike', 'Upshaw', 'Upton', 'Vachell', 'Vale', 'Vann', 'Veal', 'Verey', 'Vickers', 'Vince', 'Vincent', 'Virgo', 'Voaden', 'Voyle', 'Voyles', 'Wadding', 'Walden', 'Wale', 'Walker', 'Wall', 'Wallage', 'Walle', 'Wallis', 'Wallman', 'Ward', 'Warren', 'Warwick', 'Wasson', 'Waters', 'Wathey', 'Watkin', 'Watkins', 'Watling', 'Watrous', 'Watson', 'Watt', 'Watters', 'Wattis', 'Watts', 'Waugh', 'Weaver', 'Webber', 'Webster', 'Weeks', 'Weller', 'Wells', 'Welsh', 'Wenham', 'Weston', 'Wharton', 'Wheeler', 'Whibley', 'Whidden', 'White', 'Whitney', 'Whybrow', 'Whyte', 'Wick', 'Wicks', 'Wickwar', 'Wilde', 'Wilk', 'Wilkie', 'Willett', 'Wilmut', 'Wilson', 'Wind', 'Winder', 'Windley', 'Winmill', 'Winrow', 'Winslow', 'Winter', 'Wise', 'Witting', 'Wixom', 'Wolfe', 'Wood', 'Woodard', 'Woodger', 'Woodrow', 'Woodson', 'Woolf', 'Workman', 'Worland', 'Wornum', 'Worrall', 'Worrell', 'Wright', 'Wyness', 'Yabsley', 'Yarde', 'Yawson', 'Yeager', 'Yonge', 'Youlden', 'Young', 'Yount', 'Yung', 'Zeal']
#365 names,1137 surnames

playerNameITA = ['Achile', 'Adamo', 'Adolfo', 'Adriano', 'Alberto', 'Albino', 'Alessio', 'Alfonso', 'Alfredo', 'Amedeo', 'Amerigo', 'Andrea', 'Anselmo', 'Antonio', 'Armando', 'Arrigo', 'Arturo', 'Augusto', 'Basilio', 'Biagio', 'Boris', 'Camillo', 'Candido', 'Carlo', 'Cesare', 'Claudio', 'Corrado', 'Damaso', 'Damiano', 'Daniele', 'Dario', 'Davide', 'Dionigi', 'Donato', 'Edgardo', 'Edmondo', 'Edoardo', 'Eligio', 'Emilio', 'Enrico', 'Enzo', 'Ercole', 'Ermanno', 'Ettore', 'Eugenio', 'Eusebio', 'Ezio', 'Fabiano', 'Fabio', 'Filippo', 'Flavio', 'Gaetano', 'Gaspare', 'Gennaro', 'Gerardo', 'Giacomo', 'Gianni', 'Gino', 'Giorgio', 'Giulio', 'Guido', 'Gustavo', 'Ignazio', 'Igor', 'Ilario', 'Ireneo', 'Isacco', 'Isidoro', ' Ivo', 'Leone', 'Livio', 'Lorenzo', 'Luca', 'Luciano', 'Luigi', 'Marco', 'Mariano', 'Mario', 'Martino', 'Massimo', 'Matteo', 'Mattia', 'Michele', 'Nicola', 'Orazio', 'Oscar', 'Ottavio', 'Paolo', 'Pietro', ' Pio', 'Remigio', 'Remo', 'Roberto', 'Rocco', 'Rodolfo', 'Romano', 'Romolo', 'Sawerio', 'Sergio', 'Simone', 'Siro', 'Sisto', 'Stefano', 'Taddeo', 'Teodoro', 'Teofilo', 'Tito', 'Tiziano', 'Tommaso', ' Ugo', 'Umberto', 'Valerio', 'Vitale', 'Vito']
playerSurnameITA = ['Abate', 'Abati', 'Abba', 'Abbadia', 'Abbate', 'Abbati', 'Abbiati', 'Abruzzo', 'Accardi', 'Accardo', 'Acerbi', 'Achilli', 'Adamo', 'Adduono', 'Adolfi', 'Adorni', 'Adorno', 'Agazzi', 'Aglio', 'Agnelli', 'Agnello', 'Agnesi', 'Agnoli', 'Agnolin', 'Agosti', 'Agresti', 'Agusta', 'Aiello', 'Airoldi', 'Albani', 'Albano', 'Alberti', 'Albini', 'Albizzi', 'Alboni', 'Aldini', 'Aleotti', 'Alessi', 'Alessio', 'Alfieri', 'Alghisi', 'Alinovi', 'Aliotti', 'Allasio', 'Allegri', 'Allio', 'Almici', 'Altieri', 'Álvarez', 'Alverà', 'Amadei', 'Amati', 'Amato', 'Ambu', 'Amico', 'Amodei', 'Amurri', 'Ancona', 'Angeli', 'Angioni', 'Ansaldi', 'Ansaldo', 'Anselmi', 'Aquila', 'Arata', 'Arborio', 'Arcari', 'Arditi', 'Argenti', 'Argento', 'Arienti', 'Arnone', 'Ascani', 'Ascari', 'Astori', 'Atzeni', 'Atzori', 'Audisio', 'Azzini', 'Baccari', 'Bacchi', 'Bacci', 'Baccini', 'Baffi', 'Bagnis', 'Balbi', 'Balboni', 'Baldi', 'Baldini', 'Baldoni', 'Baliani', 'Balleri', 'Ballini', 'Balzano', 'Bamonte', 'Banegas', 'Banti', 'Barale', 'Barassi', 'Barati', 'Baratta', 'Barbaro', 'Barbato', 'Barberi', 'Barbero', 'Barbini', 'Barbuti', 'Barella', 'Barilla', 'Barone', 'Baroni', 'Baronio', 'Barreca', 'Barresi', 'Bartoli', 'Bartolo', 'Baselli', 'Bassani', 'Bassano', 'Bassini', 'Basso', 'Bassoli', 'Bastoni', 'Bazzani', 'Bazzoni', 'Becatti', 'Beccari', 'Belardi', 'Bellemo', 'Belleri', 'Belli', 'Bellini', 'Bello', 'Bellodi', 'Belloni', 'Bellugi', 'Belotti', 'Benassi', 'Benatti', 'Benetti', 'Benigni', 'Benini', 'Bennati', 'Benussi', 'Benzoni', 'Berdini', 'Bergamo', 'Berizzo', 'Bernero', 'Berni', 'Bernini', 'Berruti', 'Bertani', 'Berti', 'Bertino', 'Bertoli', 'Bertolo', 'Bertone', 'Bertoni', 'Berzano', 'Besozzi', 'Bettega', 'Betti', 'Bettini', 'Bettoni', 'Biaggi', 'Biagini', 'Bianchi', 'Bianco', 'Biasini', 'Biava', 'Bigagli', 'Bigazzi', 'Biggio', 'Bindi', 'Bini', 'Biondo', 'Biraghi', 'Bisagno', 'Bisiach', 'Bisoli', 'Bizzi', 'Blasi', 'Boari', 'Bodini', 'Boffi', 'Boggia', 'Boiardo', 'Bolchi', 'Boldi', 'Bolelli', 'Bollini', 'Bolocco', 'Bolzan', 'Bolzoni', 'Bonanni', 'Bonanno', 'Bonatti', 'Bonci', 'Bonelli', 'Bonera', 'Bongino', 'Bonini', 'Bonolis', 'Bonomi', 'Bonucci', 'Bordoni', 'Borelli', 'Borgato', 'Borgese', 'Borghi', 'Borri', 'Borsi', 'Borsoi', 'Bosatta', 'Boscolo', 'Boselli', 'Bosisio', 'Bossi', 'Bottini', 'Bovio', 'Bovone', 'Bozzano', 'Bracchi', 'Bracci', 'Braga', 'Braglia', 'Bramati', 'Brascia', 'Brescia', 'Brevi', 'Briano', 'Brienza', 'Brighi', 'Briglia', 'Brivio', 'Brizzi', 'Brocchi', 'Broggi', 'Brogi', 'Brucato', 'Bruni', 'Bruno', 'Brunori', 'Brusca', 'Bruschi', 'Bucchi', 'Bucci', 'Buglio', 'Bugno', 'Buono', 'Buratti', 'Burelli', 'Buzzi', 'Cabello', 'Cabrini', 'Caccia', 'Caccini', 'Caetani', 'Cafagna', 'Caffi', 'Cagni', 'Caimo', 'Caiola', 'Cairo', 'Calabro', 'Calamai', 'Calì', 'Calleri', 'Calloni', 'Calò', 'Calvano', 'Calvi', 'Calvo', 'Camilli', 'Campisi', 'Campori', 'Canale', 'Canali', 'Canfari', 'Canfora', 'Canini', 'Cannata', 'Cannone', 'Cantoni', 'Cantù', 'Canuti', 'Capaldi', 'Capano', 'Capasso', 'Capece', 'Capello', 'Capone', 'Caponi', 'Capozzi', 'Capponi', 'Capra', 'Caprari', 'Capria', 'Caprio', 'Capua', 'Capuana', 'Capuano', 'Capucci', 'Caputi', 'Caputo', 'Capuzzi', 'Capuzzo', 'Caratti', 'Carbo', 'Carbone', 'Carboni', 'Cardi', 'Cardini', 'Cardone', 'Cardoni', 'Carelli', 'Carlini', 'Carlino', 'Carloni', 'Caroli', 'Carosi', 'Carotti', 'Carpani', 'Carpi', 'Carpino', 'Carrera', 'Caruso', 'Carzino', 'Casadei', 'Casale', 'Casali', 'Casarin', 'Casati', 'Cascio', 'Cascone', 'Caselli', 'Casini', 'Casolla', 'Cassani', 'Cassano', 'Cassola', 'Cataldi', 'Catani', 'Catania', 'Cattani', 'Cavagna', 'Cavalli', 'Caymmi', 'Cazzola', 'Cecchi', 'Cecconi', 'Ceci', 'Cecon', 'Cellini', 'Cennamo', 'Cerbone', 'Cercato', 'Cerci', 'Cerilli', 'Cerioni', 'Cernuto', 'Ceroli', 'Cerreti', 'Cerri', 'Cerruti', 'Ceruti', 'Cerutti', 'Cervi', 'Cesari', 'Cesca', 'Cesi', 'Cesina', 'Checchi', 'Cheli', 'Chesi', 'Chia', 'Chiappa', 'Chiesa', 'Chiocci', 'Chiodi', 'Chirico', 'Ciacci', 'Ciampa', 'Ciampi', 'Cianci', 'Ciancio', 'Ciardi', 'Ciccone', 'Cicogna', 'Cifra', 'Cimini', 'Cimino', 'Ciocci', 'Cioni', 'Ciotti', 'Cirelli', 'Cirillo', 'Cirulli', 'Ciucci', 'Civita', 'Claro', 'Claudio', 'Clerici', 'Climati', 'Cobelli', 'Coccia', 'Cocuzza', 'Coduri', 'Coletti', 'Colli', 'Collini', 'Colombo', 'Colosi', 'Columbu', 'Comella', 'Cometti', 'Concas', 'Concina', 'Conte', 'Conti', 'Contini', 'Contino', 'Contri', 'Coppi', 'Coppo', 'Coppola', 'Corapi', 'Corazza', 'Cordero', 'Cordone', 'Corioni', 'Corradi', 'Corsaro', 'Corsi', 'Corsini', 'Cortese', 'Corti', 'Coscia', 'Cossu', 'Costa', 'Cotroni', 'Cotti', 'Cottone', 'Cotugno', 'Covino', 'Covre', 'Cozza', 'Cozzi', 'Cozzoli', 'Cravero', 'Craxi', 'Crecco', 'Crespi', 'Crimi', 'Crippa', 'Crocco', 'Croce', 'Crosta', 'Crotti', 'Crotto', 'Cuccia', 'Cuffaro', 'Cunego', 'Cuoco', 'Cuomo', 'Curci', 'Curiel', 'Cusano', 'Cutolo', "D'Agata", "D'Amato", "D'Amico", "D'Eramo", "D'Inzeo", 'Dametto', 'Damiani', 'Dandini', 'Dandolo', 'Daniele', 'Danzi', 'De-Bono', 'De-Lima', 'De-Niro', 'De-Pra', 'De-Sio', 'Decarli', 'DeCarlo', 'DeCicco', 'Degano', 'Deguara', 'Deledda', 'DeLuca', 'Demuro', 'Denegri', 'DeRocco', 'Dettori', 'DeVito', 'Di-Leo', 'DiCarlo', 'DiCosmo', 'DiMarco', 'Dinelli', 'Dini', 'Dionigi', 'Dionisi', 'DiPaolo', 'Dolfini', 'Donati', 'Donato', 'Donnini', 'Dorigo', 'Dotti', 'Dragna', 'Dudan', 'Dugoni', 'Durante', 'Enrici', 'Ercoli', 'Errigo', 'Escuti', 'Ettori', 'Eusepi', 'Fabini', 'Fabrizi', 'Facchin', 'Facci', 'Faccini', 'Facco', 'Facetti', 'Faggin', 'Fagioli', 'Fagnano', 'Falchi', 'Falco', 'Fanelli', 'Fanini', 'Fantini', 'Fanucci', 'Farci', 'Farelli', 'Farina', 'Fasano', 'Fasoli', 'Fattori', 'Fauci', 'Favalli', 'Favaro', 'Favero', 'Fazzi', 'Fedele', 'Felici', 'Ferlito', 'Ferrara', 'Ferrari', 'Ferraro', 'Ferrato', 'Ferrero', 'Ferri', 'Ferro', 'Ferroni', 'Ficano', 'Fietta', 'Figoli', 'Filippi', 'Finazzi', 'Finelli', 'Finizio', 'Fiore', 'Fiori', 'Fiorini', 'Fioroni', 'Fissore', 'Fiumara', 'Flacco', 'Fogli', 'Foglio', 'Fognini', 'Fonda', 'Fontana', 'Forlani', 'Forleo', 'Fornoni', 'Forte', 'Forti', 'Foschi', 'Foscolo', 'Franchi', 'Franco', 'Frasi', 'Fratta', 'Freda', 'Freddi', 'Fregoso', 'Frezza', 'Frieri', 'Frione', 'Frisoni', 'Frizzi', 'Fulci', 'Fusari', 'Fuschi', 'Fusco', 'Fusi', 'Gaeta', 'Gaioni', 'Galassi', 'Galasso', 'Galeone', 'Galizia', 'Gallini', 'Gallo', 'Gamba', 'Gambaro', 'Gambini', 'Gambino', 'Gambone', 'Ganci', 'Gandini', 'Ganna', 'Gardini', 'Gargano', 'Garioni', 'Garlini', 'Garrone', 'Garzena', 'Gatti', 'Gattuso', 'Gaudio', 'Gavazzi', 'Gazzari', 'Gazzoli', 'Gazzolo', 'Gelmini', 'Genna', 'Gennari', 'Gentili', 'Geraci', 'Gerini', 'Germani', 'Ghedin', 'Ghelli', 'Ghezzi', 'Ghidini', 'Giacone', 'Giambi', 'Gianni', 'Gilardi', 'Giletti', 'Gimelli', 'Ginesi', 'Gioli', 'Giomo', 'Giorgi', 'Girardi', 'Girelli', 'Girotti', 'Giudici', 'Giugno', 'Giunta', 'Giusti', 'Gliozzi', 'Gobbi', 'Gobbo', 'Gobetti', 'Goffi', 'Gollini', 'Gotti', 'Gozzi', 'Grabbi', 'Grande', 'Grandi', 'Grassi', 'Greco', 'Greggio', 'Grella', 'Greppi', 'Grieco', 'Grillo', 'Gritti', 'Gronchi', 'Grosso', 'Guaita', 'Gualdi', 'Guarino', 'Guarna', 'Guerci', 'Guerini', 'Guerra', 'Guida', 'Guidi', 'Guido', 'Guidone', 'Guidoni', 'Gulotta', 'Guzzo', 'Herin', 'Iaconi', 'Iamonte', 'Illiano', 'Improta', 'Inaudi', 'Incerti', 'Inglese', 'Inzaghi', 'Iommi', 'Iommi', 'Iorio', 'Iovino', 'Issel', 'Iuliano', 'Ivaldi', 'Jorio', 'Juliano', 'Laezza', 'Lamanna', 'Lancini', 'Landini', 'Lanini', 'Lanza', 'Lanzano', 'Lanzi', 'Lanzini', 'Lanzoni', 'Larini', 'Latini', 'Lavaggi', 'Lavazza', 'Leali', 'Leggio', 'Lelli', 'Lenzi', 'Leone', 'Leoni', 'Leonori', 'Leotta', 'Lepore', 'Lepori', 'Lertora', 'Leto', 'Letteri', 'Leuzzi', 'Levati', 'Liberto', 'Ligabue', 'Linari', 'Lione', 'Liotta', 'Lippi', 'Liviero', 'Lizaola', 'Lolli', 'Longo', 'Longoni', 'Lorenzi', 'Lovato', 'Lozzi', 'Luca', 'Lucci', 'Luci', 'Luciani', 'Lucini', 'Lucio', 'Lucioni', 'Luisi', 'Lunadei', 'Lunardi', 'Lunati', 'Luongo', 'Lupino', 'Lupo', 'Lusardi', 'Lusin', 'Lusoli', 'Luti', 'Luzi', 'Luzzani', 'Luzzi', 'Maccari', 'Macri', 'Madonia', 'Maestri', 'Maggini', 'Magli', 'Magnago', 'Magnani', 'Magnano', 'Magnini', 'Magoni', 'Magri', 'Magrini', 'Maimone', 'Maioli', 'Maione', 'Malori', 'Maltese', 'Manardi', 'Mancini', 'Manelli', 'Manenti', 'Manetti', 'Mangano', 'Maniero', 'Mannari', 'Mannini', 'Manucci', 'Marani', 'Marano', 'Marasco', 'Marcato', 'Marchei', 'Marchi', 'Marchio', 'Marconi', 'Marcora', 'Marello', 'Marenco', 'Mariani', 'Mariano', 'Marini', 'Marino', 'Marotta', 'Marotti', 'Marri', 'Marrone', 'Marsili', 'Martini', 'Martino', 'Marullo', 'Marzano', 'Marzo', 'Mascia', 'Masetti', 'Masiero', 'Masino', 'Mason', 'Massaro', 'Massimo', 'Massone', 'Massoni', 'Mauro', 'Mazza', 'Mazzeo', 'Mazzia', 'Mazzini', 'Mazzola', 'Mazzoli', 'Mazzone', 'Mazzoni', 'Mealli', 'Medda', 'Melato', 'Melis', 'Mellini', 'Meloni', 'Melucci', 'Menconi', 'Menegon', 'Menga', 'Mengoni', 'Meola', 'Meoni', 'Merini', 'Merli', 'Merola', 'Messina', 'Messori', 'Miano', 'Micara', 'Micheli', 'Mignani', 'Milano', 'Milesi', 'Minardi', 'Mineo', 'Minetti', 'Minieri', 'Minoia', 'Minotti', 'Minucci', 'Missoni', 'Moccia', 'Mochi', 'Modesti', 'Modesto', 'Modiano', 'Modugno', 'Mollica', 'Molteni', 'Monaldi', 'Mondini', 'Montani', 'Montesi', 'Monti', 'Morace', 'Morandi', 'Morante', 'Morelli', 'Moresi', 'Moretti', 'Mori', 'Morici', 'Morigi', 'Morin', 'Morina', 'Morini', 'Morino', 'Morleo', 'Morlino', 'Moro', 'Moroni', 'Morresi', 'Mortara', 'Mosca', 'Moscati', 'Motta', 'Mottola', 'Munari', 'Muraro', 'Murolo', 'Musante', 'Musetti', 'Musiani', 'Mussi', 'Mussini', 'Muzzi', 'Nadal', 'Nadi', 'Naldi', 'Nanni', 'Napoli', 'Narciso', 'Nardini', 'Nardone', 'Nasini', 'Natali', 'Navarro', 'Nazari', 'Negri', 'Negrini', 'Negro', 'Negroni', 'Nencini', 'Neri', 'Nespoli', 'Nesti', 'Niggli', 'Nizzi', 'Nobili', 'Nodari', 'Nordio', 'Notaro', 'Novelli', 'Nudi', 'Nunnari', 'Nuzzi', 'Nuzzo', 'Oddi', 'Oliva', 'Oliveri', 'Olivi', 'Olmo', 'Ongaro', 'Onofrio', 'Orazi', 'Orfei', 'Oriani', 'Orlandi', 'Orlando', 'Orsi', 'Ottone', 'Pacelli', 'Pacetti', 'Paci', 'Pacini', 'Pacione', 'Pacitto', 'Paganin', 'Paglia', 'Pagni', 'Pagnini', 'Pagotto', 'Palanti', 'Palazzi', 'Palermo', 'Paletta', 'Panatta', 'Panetta', 'Panetti', 'Pangaro', 'Panizza', 'Panizzi', 'Pansino', 'Pantano', 'Panzeri', 'Paolini', 'Paolo', 'Paoloni', 'Papalia', 'Papini', 'Parenti', 'Pareto', 'Parisi', 'Parlato', 'Paro', 'Paruta', 'Pascal', 'Pascale', 'Pascoe', 'Pasetti', 'Pasini', 'Pasotti', 'Pasqual', 'Passeri', 'Passoni', 'Pastor', 'Paterno', 'Paterra', 'Pavesi', 'Pecchia', 'Pedroni', 'Pellino', 'Pelosi', 'Penna', 'Penzo', 'Pepe', 'Pera', 'Peretti', 'Peri', 'Perilli', 'Perosi', 'Perotti', 'Perri', 'Perrino', 'Perroni', 'Persico', 'Pertile', 'Pesce', 'Pesci', 'Pesenti', 'Pessina', 'Pestrin', 'Petacci', 'Petito', 'Petri', 'Petrini', 'Petris', 'Petroni', 'Pezzati', 'Pezzi', 'Piana', 'Piatti', 'Piazza', 'Picardi', 'Picchi', 'Picchio', 'Piccio', 'Piccoli', 'Piccolo', 'Piccone', 'Pieri', 'Pieroni', 'Pietri', 'Pigni', 'Pileggi', 'Pilotti', 'Pinardi', 'Pinato', 'Pinotti', 'Pinto', 'Pioli', 'Piotti', 'Piovani', 'Piperno', 'Pirro', 'Pisani', 'Pisanu', 'Piscopo', 'Pistone', 'Pivetti', 'Pizzo', 'Pizzuti', 'Poletti', 'Poli', 'Polizzi', 'Poloni', 'Pompeo', 'Pompili', 'Ponzo', 'Porelli', 'Porri', 'Porrini', 'Pozzato', 'Pozzo', 'Pozzoni', 'Presti', 'Prestia', 'Prete', 'Preti', 'Prodi', 'Profeta', 'Protti', 'Provera', 'Puccia', 'Puccio', 'Pucillo', 'Puglia', 'Puglisi', 'Pulcini', 'Puleo', 'Punto', 'Puppi', 'Quaglia', 'Quario', 'Quilici', 'Radici', 'Rafaeli', 'Ragni', 'Raiola', 'Ramella', 'Rampi', 'Rampino', 'Ranalli', 'Ranelli', 'Ranieri', 'Ranucci', 'Ratti', 'Ravasi', 'Ravelli', 'Razzi', 'Reali', 'Reato', 'Rebiba', 'Rebosio', 'Rebuzzi', 'Recchi', 'Redolfi', 'Renda', 'Renica', 'Renosto', 'Renzi', 'Renzo', 'Rettino', 'Ribisi', 'Ricci', 'Ridolfi', 'Rigali', 'Rigano', 'Righi', 'Righini', 'Rigoni', 'Rigotti', 'Rigotto', 'Rimoldi', 'Rinaldi', 'Riolo', 'Rissone', 'Riva', 'Rivalta', 'Rivelli', 'Rivolta', 'Rizza', 'Rizzo', 'Rizzuto', 'Roatta', 'Robotti', 'Rocca', 'Roccati', 'Rocchi', 'Rocci', 'Rocco', 'Rognoni', 'Rolla', 'Romeo', 'Ronconi', 'Rosa', 'Rosai', 'Rosati', 'Rosato', 'Roselli', 'Rosetti', 'Rossi', 'Rossini', 'Rosso', 'Rota', 'Rotolo', 'Rotondi', 'Rotondo', 'Rotundo', 'Roversi', 'Rozzi', 'Rubino', 'Ruffini', 'Ruffo', 'Ruggeri', 'Rullo', 'Rumore', 'Ruotolo', 'Russo', 'Rustici', 'Sabato', 'Sacchi', 'Sacco', 'Sacconi', 'Saitta', 'Salemme', 'Salerno', 'Salvini', 'Sandri', 'Sanesi', 'Sannino', 'Santini', 'Santori', 'Santoro', 'Sardi', 'Sarti', 'Sarto', 'Sartori', 'Sassi', 'Sasso', 'Sassoli', 'Sassone', 'Savelli', 'Savi', 'Savini', 'Savoldi', 'Scaccia', 'Scaduto', 'Scalia', 'Scappi', 'Scarpa', 'Schiavi', 'Sciarra', 'Scilla', 'Scirea', 'Scopoli', 'Secchi', 'Secco', 'Seddio', 'Segato', 'Sella', 'Selleri', 'Selva', 'Semini', 'Sepe', 'Sereni', 'Serra', 'Serrano', 'Sestini', 'Setti', 'Severi', 'Sevieri', 'Sgarbi', 'Sgro', 'Siani', 'Sichi', 'Sidoli', 'Sidoti', 'Sigona', 'Silva', 'Simari', 'Simeoni', 'Simoni', 'Sirola', 'Sivori', 'Solari', 'Soldati', 'Soleri', 'Solinas', 'Sonego', 'Soprani', 'Sormani', 'Spadaro', 'Sparano', 'Speroni', 'Sposito', 'Statuto', 'Stefani', 'Stefano', 'Stella', 'Stocchi', 'Strada', 'Stroppa', 'Strozzi', 'Stuani', 'Succi', 'Sunseri', 'Suriano', 'Taccone', 'Tacconi', 'Taddei', 'Tagnin', 'Taliani', 'Tamburi', 'Tanzini', 'Tarozzi', 'Taruffi', 'Tassi', 'Tassoni', 'Tato', 'Tattini', 'Tavano', 'Tecchio', 'Tedesco', 'Tegano', 'Terzi', 'Tessari', 'Tessaro', 'Testa', 'Testoni', 'Tiezzi', 'Tisci', 'Titone', 'Tocci', 'Tofano', 'Toffoli', 'Togni', 'Tognini', 'Tognoli', 'Tognon', 'Tombesi', 'Tommasi', 'Tonani', 'Tonelli', 'Tonello', 'Tonetti', 'Tonetto', 'Tonini', 'Toniolo', 'Tonoli', 'Tonti', 'Tontini', 'Tonucci', 'Torre', 'Torrisi', 'Toselli', 'Toso', 'Totino', 'Tozzo', 'Trafeli', 'Travia', 'Trebbi', 'Trentin', 'Trezzi', 'Troisi', 'Tropea', 'Trotta', 'Turchi', 'Turci', 'Turrini', 'Tutino', 'Uberti', 'Uccello', 'Ungaro', 'Ursi', 'Ursino', 'Vacca', 'Vairo', 'Valla', 'Vanetti', 'Vanoli', 'Vasari', 'Vecchi', 'Veggio', 'Velotti', 'Vento', 'Venturi', 'Vernati', 'Verona', 'Verri', 'Vescovo', 'Vespoli', 'Vettori', 'Viani', 'Vieri', 'Viganò', 'Vigna', 'Vignali', 'Vignoli', 'Villa', 'Villani', 'Violi', 'Viotti', 'Virzì', 'Vittori', 'Vivaldi', 'Viviani', 'Vizzini', 'Vollaro', 'Volpe', 'Volpi', 'Votto', 'Zacchia', 'Zacconi', 'Zago', 'Zamboni', 'Zampano', 'Zanelli', 'Zanetti', 'Zanin', 'Zanini', 'Zannoni', 'Zanotti', 'Zanzi', 'Zappa', 'Zappa', 'Zarcone', 'Zardini', 'Zauli', 'Zedda', 'Zenoni', 'Ziani', 'Zilioli', 'Zito', 'Zoboli', 'Zocchi', 'Zollo', 'Zoppi', 'Zorzi', 'Zucchi', 'Zuffi', 'Zuliani', 'Zulli', 'Zumbo', 'Zunino', 'Zurlo']
#114 names, 1426 surnames

playerNameFRA = ['Abel', 'Abraham', 'Achille', 'Adam', 'Adel', 'Ademar', 'Adhemar', 'Adolf', 'Adrien', 'Agénor', 'Aimé', 'Alain', 'Albert', 'Alfred', 'Allain', 'Alvin', 'Amable', 'Anatole', 'André', 'Ange', 'Anicet', 'Anne', 'Antoine', 'Anton', 'Antonin', 'Armand', 'Arnaud', 'Arnaut', 'Arsène', 'Arthur', 'Aubin', 'Auguste', 'Aymard', 'Bastien', 'Benoît', 'Bernard', 'Blaise', 'Bruno', 'Calixte', 'Calvin', 'Camille', 'Candide', 'Carolus', 'Cédric', 'Charle', 'Charles', 'Charlot', 'Claude', 'Clement', 'Cyrille', 'Daniel', 'Danton', 'David', 'Delbert', 'Denis', 'Désiré', 'Didier', 'Donald', 'Edgar', 'Edmé', 'Edmond', 'Édouard', 'Élie', 'Émilien', 'Éric', 'Ernest', 'Eran', 'Étienne', 'Fabien', 'Fabrice', 'Fernand', 'Fleury', 'Florian', 'Francis', 'Franck', 'Frank', 'Fulbert', 'Gabriel', 'Gaël', 'Gaspard', 'Gaston', 'Georges', 'Gérald', 'Gérard', 'Gerbaud', 'Germain', 'Gilbert', 'Gilles', ' Guy', 'Harold', 'Henri', 'Herbert', 'Hervé', 'Hilaire', 'Honoré', 'Horace', 'Hubert', 'Hugo', 'Hugues', ' Ivo', 'Jacues', 'Jacuet', 'James', 'Jasper', 'Jean', 'Jérémie', 'Jérémy', 'Jerome', 'Joël', 'Joseph', 'Jules', 'Julien', 'Justin', 'Lauren', 'Laurent', 'Léon', 'Léonce', 'Loïc', 'Louis', 'Loup', ' Luc', 'Lucien', 'Ludo', 'Ludovic', 'Manuel', 'Marc', 'Marcel', 'Marco', 'Martin', 'Mathieu', 'Maurice', 'Maxence', 'Maxime', 'Medard', 'Melvin', 'Michel', 'Moise', 'Nicolas', 'Norbert', 'Octave', 'Odilon', 'Olivier', 'Pacôme', 'Pascal', 'Patrice', 'Patrick', 'Paul', 'Pierre', 'Rainier', 'Raoul', 'Raphael', 'Raymond', 'Rémy', 'René', 'Robert', 'Roger', 'Roland', 'Romain', 'Roman', 'Roméo', 'Romuald', 'Ronald', 'Samuel', 'Serge', 'Servais', 'Severin', 'Simon', 'Sylvain', 'Thibaut', 'Thierry', 'Thomas', 'Titouan', 'Ulysse', 'Victor', 'Vincent', 'Xavier', 'Yacine', 'Yann', 'Yannick', 'Yvan', 'Yves', 'Yvon']
playerSurnameFRA = ['Abadie', 'Abba', 'Abbadie', 'About', 'Absil', 'Adnet', 'Affré', 'Alard', 'Alarie', 'Alibert', 'Aliker', 'Allain', 'Allaire', 'Allais', 'Allard', 'Alméras', 'Ange', 'Antier', 'Appell', 'Arbour', 'Ardouin', 'Assayas', 'Asselin', 'Astier', 'Aubert', 'Auclair', 'Augé', 'Auger', 'Auguste', 'Autié', 'Auvray', 'Aveline', 'Aymard', 'Azaïs', 'Azéma', 'Bacque', 'Badeaux', 'Baffier', 'Bain', 'Balland', 'Balzac', 'Barbeau', 'Barbet', 'Barbier', 'Bardet', 'Bardin', 'Barnaud', 'Barnier', 'Barreau', 'Barrere', 'Barthet', 'Baschet', 'Basset', 'Bassot', 'Bastide', 'Bastien', 'Bastin', 'Batteux', 'Battier', 'Batton', 'Baudet', 'Baugé', 'Bauhin', 'Baumé', 'Baume', 'Bazin', 'Beaulne', 'Beauvau', 'Beaux', 'Bebout', 'Bechard', 'Bedeau', 'Bellet', 'Belshaw', 'Belyea', 'Benoît', 'Béraud', 'Berger', 'Bergier', 'Berjeau', 'Bernard', 'Bernier', 'Berthod', 'Bescond', 'Besnard', 'Besson', 'Bethune', 'Bidard', 'Bigot', 'Blanc', 'Bochart', 'Bocuse', 'Boisson', 'Bonheur', 'Bonnel', 'Bonnet', 'Bonnot', 'Borguet', 'Bossuet', 'Botrel', 'Boucher', 'Boudet', 'Boudier', 'Boudon', 'Bougie', 'Bouhier', 'Boulet', 'Boulle', 'Bourdon', 'Bourgue', 'Bourque', 'Bousset', 'Boutet', 'Boutin', 'Boutry', 'Breguet', 'Bréhal', 'Brian', 'Brouzet', 'Brugère', 'Bruguès', 'Bruneau', 'Brunet', 'Brunot', 'Bruyère', 'Buchard', 'Bullion', 'Bureau', 'Cabal', 'Cadieu', 'Caffier', 'Cahun', 'Caillat', 'Calvet', 'Capron', 'Cardona', 'Cardot', 'Carell', 'Carré', 'Carrel', 'Carrell', 'Cartier', 'Castex', 'Castile', 'Cavé', 'Cazal', 'Celice', 'Cellier', 'Cerf', 'Chabert', 'Chagnon', 'Chambon', 'Chanal', 'Chaney', 'Chapuis', 'Chardin', 'Charlet', 'Chaucer', 'Chauve', 'Chéreau', 'Chéron', 'Chollet', 'Chopin', 'Choplin', 'Choquet', 'Chuquet', 'Clair', 'Clerc', 'Clérico', 'Cochet', 'Cochin', 'Coderre', 'Colbert', 'Collin', 'Colmez', 'Compere', 'Corbin', 'Cordier', 'Corne', 'Cortot', 'Côté', 'Coudert', 'Coudray', 'Coulomb', 'Courbet', 'Courbis', 'Courtet', 'Coutard', 'Coutrot', 'Couttet', 'Couture', 'Crépin', 'Crevier', 'Crouzet', 'Crozier', 'Cuch', "D'Arras", "D'Orves", 'Dallier', 'Danzas', 'Darche', 'Decaen', 'Decamps', 'Decaux', 'Defays', 'Delisle', 'Delon', 'Delpech', 'Demachy', 'Demaret', 'Deniau', 'Deniaud', 'DeRose', 'Deslys', 'Deval', 'Devall', 'Didier', 'Dimont', 'Dion', 'Donnet', 'Dormoy', 'Doucet', 'Doucett', 'Doumbe', 'Drapeau', 'Draper', 'Du Toit', 'Dubois', 'Dubos', 'Dubost', 'Duby', 'Duchamp', 'Duclos', 'Dufau', 'Duhamel', 'Duméril', 'Dumont', 'Dupaty', 'Dupont', 'Dupont', 'Dupuis', 'Dupuy', 'Durand', 'Durant', 'Durbin', 'Durel', 'Duret', 'Dutoit', 'Duval', 'Duvall', 'Édouard', 'Emond', 'Esnault', 'Fabien', 'Faivre', 'Fauveau', 'Favre', 'Febvre', 'Fecteau', 'Ferdon', 'Féret', 'Fétique', 'Figuier', 'Filleul', 'Fillon', 'Firmin', 'Flagel', 'Flandin', 'Floquet', 'Fonder', 'Fortin', 'Fouché', 'Foullon', 'Foulon', 'Fouquet', 'Fraisse', 'Frère', 'Fresnel', 'Friesen', 'Froment', 'Gachet', 'Gagne', 'Gagneux', 'Gagnon', 'Gaillot', 'Gallois', 'Galopin', 'Ganio', 'Gardet', 'Garnier', 'Garon', 'Garreau', 'Gaubert', 'Gaucher', 'Gaudé', 'Gaudin', 'Gaulin', 'Gaume', 'Gaumont', 'Gavreau', 'Geffroy', 'Geiger', 'Genest', 'Genet', 'Génin', 'Gensoul', 'Gérald', 'Gérard', 'Gérin', 'Gicquel', 'Gide', 'Gigot', 'Girard', 'Giraud', 'Girault', 'Giresse', 'Giteau', 'Gobet', 'Godeau', 'Goff', 'Gontard', 'Gouin', 'Goulart', 'Goyette', 'Grandis', 'Granet', 'Grange', 'Grinda', 'Gueguen', 'Guerin', 'Guyon', 'Haillet', 'Halphen', 'Hauet', 'Hébras', 'Hector', 'Hémery', 'Henin', 'Hernu', 'Héroux', 'Hodin', 'Houard', 'Houde', 'Houdin', 'Hugot', 'Husson', 'Jaccoud', 'Jacquet', 'Jacquot', 'Jalbert', 'Jaubert', 'Jeandet', 'Jeannet', 'Jeannin', 'Jeantet', 'Joffrin', 'Joubert', 'Jouret', 'Jousset', 'Jouve', 'Jullien', 'Kaplan', 'La Cour', 'Labatut', 'Lacan', 'Lacau', 'Lachaud', 'Lacroix', 'Lagarde', 'Lahaye', 'Lajoie', 'Lalande', 'Landry', 'Laprise', 'LaRue', 'Laurens', 'Laval', 'Lavaud', 'Lavigne', 'Lavoie', 'Lavorel', 'Lazard', 'Leavitt', 'Lebas', 'LeBeau', 'Lecerf', 'Leclair', 'Leclerc', 'Leclère', 'Lecocq', 'Lefèvre', 'Léger', 'Legrain', 'Legros', 'Lejeune', 'Leleu', 'Leloup', 'Lemaire', 'Lémery', 'Lemoine', 'Lenoir', 'Léotard', 'Leroux', 'Levett', 'Loiseau', 'Lorieux', 'Lortie', 'Loupe', 'Louvel', 'Lozé', 'Lucroy', 'Lucy', 'Lussier', 'Mabille', 'Mace', 'Macé', 'Madiot', 'Magnan', 'Magnier', 'Mahut', 'Maignan', 'Maingon', 'Maitre', 'Maitron', 'Malan', 'Malet', 'Mallet', 'Malzieu', 'Manoury', 'Marais', 'Maraoui', 'Marchal', 'Marett', 'Marquet', 'Masse', 'Massis', 'Masson', 'Maxence', 'Mayeur', 'Mayeux', 'Mayor', 'Mazet', 'Ménard', 'Mercier', 'Mesny', 'Messier', 'Mézard', 'Michaud', 'Michaut', 'Michaux', 'Miellet', 'Mignard', 'Millet', 'Miot', 'Moineau', 'Moise', 'Mongin', 'Monier', 'Monteil', 'Moreau', 'Morel', 'Morin', 'Mossé', 'Motte', 'Moulin', 'Mourlon', 'Moutet', 'Nadaud', 'Nadon', 'Naud', 'Naudé', 'Naviaux', 'Neri', 'Niakaté', 'Niel', 'Noir', 'Noirot', 'Nouel', 'Ollier', 'Ouvrard', 'Ozanne', 'Paquet', 'Paquin', 'Pascal', 'Pechet', 'Peltier', 'Périer', 'Pernet', 'Perreau', 'Perrier', 'Pertuit', 'Petit', 'Phaneuf', 'Piaget', 'Picart', 'Pichard', 'Pierlot', 'Pierrat', 'Pillard', 'Pinchon', 'Pitoëff', 'Planus', 'Plessis', 'Plouffe', 'Poirot', 'Poisson', 'Pomeroy', 'Ponce', 'Popelin', 'Porion', 'Portier', 'Potain', 'Pougnet', 'Poulin', 'Pouliot', 'Poussin', 'Prejean', 'Pretre', 'Prévot', 'Puech', 'Puel', 'Quittet', 'Rambin', 'Ranque', 'Raoult', 'Rapace', 'Ravier', 'Reason', 'Regnard', 'Renard', 'Reneau', 'Renoir', 'Renou', 'Ricard', 'Richard', 'Richet', 'Rigal', 'Ripert', 'Riqueti', 'Rivière', 'Robail', 'Robert', 'Robida', 'Robidas', 'Roche', 'Rodier', 'Rodin', 'Rohmer', 'Rose', 'Rouanet', 'Roueché', 'Roulet', 'Roussel', 'Rousset', 'Rouzet', 'Sadoul', 'Sales', 'Salmon', 'Sartre', 'Saunier', 'Savary', 'Sébire', 'Séjour', 'Serre', 'Sharpe', 'Silvain', 'Simon', 'Simond', 'Simonot', 'Solé', 'Sorre', 'Soubry', 'Souchon', 'Soulier', 'Soyer', 'Suard', 'Suchet', 'Tardy', 'Taskin', 'Tellier', 'Teulet', 'Thauvin', 'Thibaud', 'Thibaut', 'Thibert', 'Thiers', 'Thomas', 'Tillett', 'Tirel', 'Tisseur', 'Tomas', 'Topping', 'Toutain', 'Trémaux', 'Trouvé', 'Trudeau', 'Turgot', 'Turpin', 'Vaganay', 'Vallée', 'Valluy', 'Vandame', 'Vannier', 'Varte', 'Vasseur', 'Veil', 'Vérany', 'Verdier', 'Vernier', 'Vidal', 'Vigier', 'Vincent', 'Vizard', 'Zagre', 'Zazou']
#182 names, 615 surnames

playerNameGER = ['Abraham', 'Achim', 'Adam', 'Adel', 'Adolf', 'Adrian', 'Albert', 'Alfred', 'Alois', 'Alvin', 'Alwin', 'Andreas', 'Ansgar', 'Anthon', 'Anton', 'Antony', 'Armin', 'Arndt', 'Arno', 'Arnold', 'Arnulf', 'Artur', 'August', 'Aurick', 'Axel', 'Baldur', 'Bastian', 'Beat', 'Bernd', 'Bertram', 'Bjorn', 'Bodo', 'Bruno', 'Calvin', 'Carl', 'Carolus', 'Charl', 'Clemens', 'Conrad', 'Daniel', 'David', 'Delbert', 'Derek', 'Detlef', 'Diepold', 'Dieter', 'Dirk', 'Donald', 'Edmund', 'Egbert', 'Egon', 'Ehren', 'Eike', 'Eilhard', 'Elias', 'Elimar', 'Elmar', 'Emil', 'Erhard', 'Eric', 'Ernst', 'Ewald', 'Felix', 'Florian', 'Frank', 'Franz', 'Fredrik', 'Fridolf', 'Fritz', 'Gabriel', 'Gebhard', 'Georg', 'Gerald', 'Gerard', 'Gerd', 'Gerhard', 'Germar', 'Gernot', 'Gert', 'Gerwin', 'Gilbert', 'Götz', 'Guido', 'Gunther', 'Günther', 'Gustav', 'Gustl', 'Hanno', 'Hans', 'Harald', 'Harold', 'Hasso', 'Hauke', 'Heiko', 'Heiner', 'Heini', 'Heino', 'Heinz', 'Helge', 'Helmut', 'Helmuth', 'Henning', 'Herbert', 'Herman', 'Hermann', 'Herwig', 'Holger', 'Horst', 'Hubert', 'Hugo', 'Ignatz', 'Ignaz', 'Ingo', 'Jacob', 'Jakob', ' Jan', 'Jannik', 'Jasper', 'Jerome', 'Joachim', 'Johann', 'Jonas', 'Jörg', 'Joseph', 'Jost', 'Jupp', 'Jürgen', 'Kalli', 'Karl', 'Karsten', 'Kaspar', 'Kepler', 'Klaus', 'Knut', 'Konrad', 'Kuno', 'Kurd', 'Kurt', 'Lars', 'Leopold', 'Levin', 'Linus', 'Lorentz', 'Lotar', 'Lothar', 'Ludger', 'Ludolf', 'Ludwig', 'Lukas', 'Luther', 'Lütold', 'Lutz', 'Magnus', 'Malte', 'Manuel', 'Marcus', 'Marius', 'Martin', 'Medard', 'Meinrad', 'Melvin', 'Michael', 'Michel', 'Milo', 'Mirco', 'Mirko', 'Moritz', 'Nico', 'Nicolas', 'Nivaldo', 'Norbert', 'Norman', 'Olaf', 'Oliver', 'Orlando', 'Oscar', 'Oswald', 'Othmar', 'Otto', 'Ottomar', 'Pascal', 'Patrick', 'Paul', 'Peter', 'Philip', 'Philipp', 'Rainer', 'Ralph', 'Randall', 'Robert', 'Robin', 'Roger', 'Roland', 'Rolf', 'Roman', 'Ronald', 'Rubert', 'Rudolph', 'Samuel', 'Sander', 'Sascha', 'Sepp', 'Severin', 'Sigmund', 'Simon', 'Stefan', 'Stephen', 'Sven', 'Theodor', 'Thomas', 'Timo', 'Tobias', ' Tom', ' Udo', 'Ulrich', 'Urban', ' Uwe', 'Utto', 'Valter', 'Vincenz', 'Vinzenz', 'Waldo', 'Walter', 'Walther', 'Wenzel', 'Werner', 'Wernher', 'Wilhelm', 'William', 'Wolf', 'Wolfram', 'Xavier']
playerSurnameGER = ['Behm', 'Behr', 'Behrend', 'Beier', 'Beitz', 'Bendel', 'Benter', 'Bentz', 'Berger', 'Bergler', 'Berlin', 'Bethke', 'Beutler', 'Bieber', 'Biemann', 'Billman', 'Binder', 'Bingen', 'Binzer', 'Birken', 'Bischof', 'Blacher', 'Blanke', 'Bleuler', 'Blücher', 'Bluhm', 'Blumer', 'Boden', 'Böckler', 'Bödeker', 'Böhmer','Böhning', 'Bohrer', 'Bönsch', 'Borck', 'Bormann', 'Börner', 'Börngen', 'Bosch', 'Boßler', 'Böttger', 'Brandt', 'Brase', 'Bratz', 'Brauen', 'Brecht', 'Brenman', 'Brenner', 'Breuer', 'Breyer', 'Brümmer', 'Brunn', 'Brunner', 'Büchel', 'Büchler', 'Buchman', 'Büchner', 'Buder', 'Bühl', 'Bürger', 'Burkel', 'Burkle', 'Buscher', 'Bussler', 'Buxbaum', 'Calle', 'Cauer', 'Clasen', 'Cocceji', 'Cranach', 'Cranz', 'Dach', 'Dahlke', 'Dahmen', 'Dahmer', 'Dahn', 'Dalman', 'Daluege', 'Danz', 'Danzig', 'Dassler', 'Dehnert', 'Denzel', 'Deppe', 'Destinn', 'Detmold', 'Deutsch', 'Dickert', 'Dieker', 'Diemer', 'Dienst', 'Diesch', 'Dießl', 'Diestel', 'Dimke', 'Dinger', 'Dittmar', 'Ditzel', 'Döhl', 'Doerr', 'Dohna', 'Doležal', 'Dönitz', 'Dörfel', 'Dorfman', 'Dräger', 'Draxler', 'Drewes', 'Drexler', 'Dümmler', 'Eberl', 'Ebert', 'Eder', 'Edinger', 'Effertz', 'Eggert', 'Egner', 'Ehlert', 'Ehmann', 'Ehrlich', 'Ehrmann', 'Eibner', 'Eicke', 'Einhorn', 'Eisele', 'Eismann', 'Ellert', 'Elsner', 'Emmrich', 'Engel', 'Epstein', 'Erdmann', 'Erhard', 'Erlbaum', 'Ernst', 'Essen', 'Esser', 'Essig', 'Eßig', 'Etzdorf', 'Eugster', 'Faas', 'Faerber', 'Fahr', 'Fansler', 'Fauser', 'Fechner', 'Fechter', 'Feldman', 'Fenchel', 'Fendler', 'Ferber', 'Fersen', 'Feulner', 'Fichte', 'Fick', 'Fieber', 'Fiedler', 'Fietz', 'Fischl', 'Fittkau', 'Flecker', 'Fleiss', 'Flesch', 'Flügel', 'Förster', 'Franck', 'Francke', 'Franke', 'Franz', 'Franzl', 'Frenken', 'Freytag', 'Fried', 'Friesen', 'Fritsch', 'Froese', 'Fromm', 'Frosch', 'Fuchs', 'Funke', 'Fünten', 'Fürst', 'Ganser', 'Ganz', 'Gebauer', 'Gehler', 'Gehr', 'Gehrig', 'Gehring', 'Geier', 'Geiger', 'Geis', 'Geller', 'Gellner', 'Gentner', 'Gerber', 'Gering', 'Germann', 'Germar', 'Gernert', 'Gerson', 'Geschke', 'Gessler', 'Gessner', 'Ginter', 'Glasser', 'Glaßer', 'Glöde', 'Glück', 'Göbel', 'Göcke', 'Goedde', 'Goehr', 'Göpfert', 'Goethe', 'Goetze', 'Goll', 'Görges', 'Göring', 'Göth', 'Götz', 'Gotzman', 'Gradl', 'Gräbner', 'Graff', 'Granach', 'Grassl', 'Gratz', 'Grebel', 'Greiser', 'Griebel', 'Grohl', 'Grohs', 'Gröning', 'Gropius', 'Groß', 'Groth', 'Gruber', 'Grün', 'Gunkel', 'Günther', 'Gurtler', 'Gutheil', 'Haass', 'Haber', 'Häberli', 'Habicht', 'Haering', 'Hagmann', 'Hahnel', 'Haller', 'Halm', 'Hamburg', 'Hammerl', 'Hampel', 'Handke', 'Hänel', 'Hanisch', 'Hansch', 'Hanusch', 'Haring', 'Häring', 'Harrer', 'Hartig', 'Hauke', 'Hauser', 'Hautzig', 'Hechler', 'Hector', 'Heidler', 'Heigl', 'Heilig', 'Heiner', 'Heinig', 'Heinz', 'Heisig', 'Helbig', 'Heldt', 'Helwig', 'Hencke', 'Henlein', 'Henning', 'Henzler', 'Herbig', 'Hering', 'Hermann', 'Hersch', 'Hertner', 'Hertwig', 'Hertzog', 'Herwig', 'Hetling', 'Hettich', 'Heumann', 'Heuser', 'Heymann', 'Heyme', 'Hiemer', 'Hilbert', 'Hilgers', 'Hilpert', 'Himmler', 'Hirschl', 'Höcker', 'Hoehman', 'Hoeneß', 'Hönig', 'Hörmann', 'Höfer', 'Hoffman', 'Höffner', 'Höfle', 'Höger', 'Höhmann', 'Höing', 'Hölder', 'Holtz', 'Holweck', 'Hölzle', 'Homburg', 'Hopf', 'Hopfner', 'Hoppe', 'Hörl', 'Horn', 'Horning', 'Hörning', 'Höss', 'Hößler', 'Höttges', 'Howald', 'Hüber', 'Hübsch', 'Huffman', 'Huhn', 'Hülsen', 'Huwyler', 'Ilgner', 'Ilsung', 'Imhoff', 'Ivens', 'Jäger', 'Jodl', 'Johnen', 'Jonas', 'Josten', 'Juhnke', 'Jung', 'Jürgens', 'Jürß', 'Kändler', 'Kahl', 'Kahler', 'Kahn', 'Kaiser', 'Kammler', 'Kampf', 'Kant', 'Kapp', 'Kapsner', 'Karl', 'Kasner', 'Kasper', 'Kassner', 'Kästner', 'Katz', 'Kaulitz', 'Kauss', 'Käutner', 'Kehler', 'Kehrer', 'Keiner', 'Keller', 'Kempf', 'Kempter', 'Kendig', 'Keppler', 'Kern', 'Kessler', 'Kestler', 'Kieber', 'Kieffer', 'Kiesel', 'Kimmel', 'Kinchen', 'Kindler', 'Kinzel', 'Kirsch', 'Kistler', 'Klages', 'Klauber', 'Kleiber', 'Klemm', 'Klemme', 'Klepper', 'Klinger', 'Klippel', 'Klopfer', 'Klopp', 'Klose', 'Kloss', 'Klotz', 'Knacke', 'Knievel', 'Knigge', 'Knipp', 'Knirsch', 'Knoerr', 'Knop', 'Knubel', 'Kober', 'Kocher', 'Koehler', 'Koepcke', 'Kogler', 'Kohl','Köhler', 'Kohring', 'Köler', 'Kollar', 'König', 'Kopff', 'Köppen', 'Körber', 'Korholz', 'Körte', 'Köstner', 'Kott', 'Kraft', 'Krahl', 'Krämer', 'Krantz', 'Kranz', 'Krause', 'Krauss', 'Krehl', 'Kreipe', 'Kreisel', 'Kremer', 'Krenkel', 'Kresge', 'Krieger', 'Kromer', 'Kroos', 'Kropp', 'Kruger', 'Kruspe', 'Kubeck', 'Kuchler', 'Küchler', 'Kühne', 'Kühnert', 'Kuentz', 'Kugler', 'Kühn', 'Kuhnert', 'Kuhnt', 'Kumpf', 'Kunisch', 'Künneth', 'Kuntz', 'Kunze', 'Kurtzer', 'Kusch', 'Küstner', 'Küttner', 'Lachner', 'Lafrenz', 'Lahmann', 'Lammert', 'Lang', 'Lange', 'Langner', 'Lantz', 'Lasker', 'Latz', 'Lederer', 'Lehman', 'Lehnert', 'Leiber', 'Leidig', 'Leiner', 'Leist', 'Leitgeb', 'Leitner', 'Leitsch', 'Lemke', 'Lerch', 'Lerche', 'Lerner', 'Lessing', 'Letzel', 'Lewald', 'Lexer', 'Licht', 'Lichter', 'Liebeck', 'Lieber', 'Liepert', 'Lietzau', 'Lindner', 'Lingg', 'Linse', 'Linzer', 'Lischke', 'Loar', 'Lobe', 'Loewe', 'Löffler', 'Löhr', 'Lorber', 'Lowe', 'Lück', 'Ludorf', 'Ludwick', 'Ludwig', 'Lürssen', 'Lusch', 'Lutgen', 'Lutz', 'Maibaum', 'Mälzer', 'Mandl', 'Mantz', 'Martin', 'Marx', 'Masing', 'Meckler', 'Meindl', 'Melzer', 'Mencken', 'Mengler', 'Menzel', 'Metzger', 'Mittag', 'Möhring', 'Morwitz', 'Möser', 'Mozart', 'Much', 'Mueller', 'Mühle', 'Müller', 'Mulzer', 'Münch', 'Musäus','Nadler', 'Nagel', 'Naumann', 'Nébald', 'Neisser', 'Nelken', 'Nemetz', 'Nessel', 'Neubert', 'Neuer', 'Neufeld', 'Neumann', 'Niebuhr', 'Nitzsch', 'Noffke', 'Noske', 'Nowarra', 'Ochs', 'Ochsner', 'Oeming', 'Oesau', 'Ofner', 'Ohly', 'Olbrich', 'Opitz', 'Oppelt','Oswalt',  'Outman', 'Pachner', 'Panzer', 'Pastor', 'Pechman', 'Peltzer', 'Peucker', 'Pflüger', 'Pfohl', 'Piltz', 'Platz', 'Plesner', 'Poehler', 'Pöge', 'Pohl', 'Pölzl', 'Pommer', 'Pooth', 'Pöpel', 'Porsche', 'Posse', 'Pracht', 'Prantl', 'Preiss', 'Preuss', 'Prinz', 'Pückler', 'Quast', 'Rädler', 'Radtke', 'Raedler', 'Rahmer', 'Rahner', 'Ramberg', 'Rasch', 'Rausch', 'Redler', 'Redlich', 'Rehberg', 'Reiber', 'Reichen', 'Reimann', 'Reimer', 'Reimold', 'Reis', 'Reitter', 'Reitz', 'Reschke', 'Reus', 'Reuter', 'Ribbeck', 'Richter', 'Riecke', 'Riegel', 'Riehl', 'Riehm', 'Riemann', 'Riesch', 'Riess', 'Riessen', 'Rieth', 'Rinder', 'Rippel', 'Röber', 'Rockoff', 'Rödiger', 'Röhr', 'Röhrich', 'Romberg', 'Rommel', 'Rösch', 'Rose', 'Roser', 'Rösler', 'Ross', 'Rossel', 'Roßkopf', 'Röthke', 'Rothman', 'Rott', 'Rowohlt', 'Rudel', 'Rudloff', 'Rühle', 'Sacher', 'Saffer', 'Saft', 'Sagel', 'Salcher', 'Salzer', 'Samter', 'Sasse', 'Sattler', 'Sauer', 'Schaber', 'Schantz', 'Schaper', 'Scharf','Schatzl', 'Schauer', 'Schaus', 'Scherer', 'Scheu', 'Scheuer', 'Schild', 'Schimpf', 'Schiner', 'Schlag', 'Schlitz', 'Schmidt', 'Schneck', 'Schnee', 'Schnell', 'Schober', 'Schock', 'Schöll', 'Schoff', 'Schöler', 'Scholz', 'Scholze', 'Schön', 'Schönau', 'Schöne', 'Schöner', 'Schrade', 'Schramm', 'Schranz', 'Schürer', 'Schult', 'Schultz', 'Schulz', 'Schulze', 'Schutte', 'Schütz', 'Schwab', 'Schwarz', 'Schwede', 'Seckel', 'Seetzen', 'Sehlman', 'Seidel', 'Seiden', 'Seidler', 'Seifert', 'Seiler', 'Seitz', 'Selz', 'Semmler', 'Sendler', 'Senff', 'Senger', 'Seppelt', 'Setzer','Seyler', 'Shroyer', 'Sieber', 'Siebert', 'Siegel', 'Siemens', 'Siemer', 'Siering', 'Sigwart', 'Simmel', 'Simon', 'Simson', 'Singer', 'Smucker', 'Snyder', 'Söllner', 'Sommer', 'Spahr', 'Speck', 'Spener', 'Sperber', 'Spiegel', 'Spitz', 'Staab', 'Stadler', 'Stäbler', 'Stahmer', 'Stahnke', 'Stalder', 'Stamm', 'Stangl', 'Staudte', 'Stecher', 'Stehli', 'Stein', 'Steinle', 'Steitz', 'Stengel', 'Stern', 'Steuer', 'Steyer', 'Stieler', 'Stirner', 'Stöcker', 'Stoffel', 'Stoiber', 'Storch', 'Štorch', 'Storl', 'Stosch', 'Stoss', 'Stotler', 'Strack', 'Strantz', 'Straube', 'Strauch', 'Strauss', 'Streng', 'Strigel', 'Strobel', 'Strobl', 'Ströher', 'Strub', 'Struff', 'Stüber', 'Stuhr', 'Suchman', 'Suckow', 'Suhren', 'Sulser', 'Sulzer', 'Surmann', 'Szmidt', 'Tanne', 'Tanzer', 'Taube', 'Taubman', 'Teicher', 'Teller', 'Tendler', 'Thaler', 'Theil', 'Theiner', 'Thiel', 'Thimig', 'Thomas', 'Thomke', 'Thorn', 'Tilgner', 'Tillich', 'Tischer', 'Topp', 'Traeger', 'Traube', 'Trausch', 'Trauth', 'Treichl', 'Triendl', 'Trump', 'Turnau', 'Tuss', 'Uhlmann', 'Ulbrich', 'Ullmann', 'Ullmer', 'Ullrich', 'Ulmer', 'Umland', 'Umlauf', 'Ungar', 'Ungerer', 'Ungers', 'Unruh', 'Unser', 'Urban', 'Usinger', 'Uthman', 'Vetter', 'Vieweg', 'Vischer', 'Vögel', 'Voigt', 'Volke', 'Volkmer', 'Vonhof', 'Wachs', 'Wachtel', 'Wagener', 'Wagner', 'Wahle', 'Wahler', 'Waibel', 'Walbaum', 'Wald', 'Waldner', 'Walger', 'Walker', 'Walle', 'Wallner', 'Walter', 'Walz', 'Wankel', 'Wasser', 'Watzke', 'Waxman', 'Weber', 'Wegener', 'Wegmann', 'Wegner', 'Wehle', 'Wehner', 'Weidner', 'Weigl', 'Weimann', 'Weiss', 'Weitz', 'Weixler', 'Welter', 'Welz', 'Wendl', 'Wendt', 'Wenkel', 'Wentz', 'Wentzel', 'Wepper', 'Werich', 'Werkner', 'Wernz', 'Wetzel', 'Wexler', 'Wexner', 'Wickler', 'Widmann', 'Wieber', 'Wiegele', 'Wieler', 'Wiesner', 'Wieters', 'Wiggers', 'Wildner', 'Wilhelm', 'Wilke', 'Wilpert', 'Windler', 'Windt', 'Winkler', 'Winter', 'Wintsch', 'Winzer', 'Wirth', 'Wissler', 'Witting',  'Wöhler', 'Woehr', 'Wölk', 'Woerfel', 'Wörndle', 'Wolf', 'Wolff', 'Wolter', 'Wörfel', 'Wormser', 'Woyrsch', 'Wringe', 'Wunsch', 'Wünsche', 'Wurman', 'Wurtz', 'Wuttke', 'Zach', 'Zacher', 'Zaugg', 'Zedler', 'Zedner', 'Zeidler', 'Zeitz', 'Zeller', 'Zelter', 'Zenger', 'Zerfaß', 'Ziegler', 'Ziehrer', 'Zielke', 'Ziemann', 'Zierer', 'Zilzer', 'Zimmer', 'Zinke', 'Zippe', 'Zirk', 'Zöllner', 'Zolman', 'Zopf', 'Zorn', 'Zornes', 'Zuber', 'Zuckert', 'Zude', 'Zühlke', 'Zumthor', 'Zundel', 'Zürcher', 'Zürn', 'Zutter', 'Zwehl', 'Zweifel', 'Zweig', 'Zwerger', 'Zwicker', 'Zwiener', 'Zwinger']
#232 names, 978 surnames (porzadnie przejrzanych i zredukowanych)

playerNameREST = { 'Roland;Baku': 'Albania', 'Ermir;Hoxha': 'Albania', 'Glen;Osmani': 'Albania', 'Erion;Dushuku': 'Albania', 'Alesandro;Kodra': 'Albania', 'Fahadan;Al-Fawzan': 'Saudi Arabia', ' Ali;Shabbir': 'Saudi Arabia', 'Abdul;Al-Rubaish': 'Saudi Arabia', 'Sami;Al-Zamil': 'Saudi Arabia', 'Aamir;Al-Rugaiba': 'Saudi Arabia', 'Tawfiq;Al-Sagheer': 'Saudi Arabia', 'Lucas;Villabla': 'Argentina', 'Augustin;Romero': 'Argentina', 'Andres;Moyano': 'Argentina', 'Joaquin;Ruiz': 'Argentina', 'Juan;Pablo': 'Argentina', 'Nicolas;Rojas': 'Argentina', 'Gustavo;Blanco': 'Argentina', 'Lucas;Gonzales': 'Argentina', 'Tomas;Ortiz': 'Argentina', 'Martin;Torres': 'Argentina', 'Lucas;Ramos': 'Argentina', 'Thiago;Medina': 'Argentina', 'Hernan;Rojas': 'Argentina', 'Marcelo;Molina': 'Argentina', 'Lautaro;Gimenez': 'Argentina', 'Hayk;Poghosyan': 'Armenia', 'Aram;Manukyan': 'Armenia', 'Harrison;Smith': 'Australia', 'Levi;Williams': 'Australia', 'Jacob;Thompson': 'Australia', 'Liam;Wilson': 'Australia', 'Olivier;Walker': 'Australia', 'Max;Robinson': 'Australia', 'Benjamin;Kelly': 'Australia', 'Jack;Nguyen': 'Australia', 'Punhan;Turanli': 'Azerbaijan', 'Ziya;Ismayilzade': 'Azerbaijan', 'Jonas;Smet': 'Belgium', 'Victor;Bosmans': 'Belgium', 'Niels;Wuyts': 'Belgium', 'Theo;Timermans': 'Belgium', 'Justin;Simons': 'Belgium', 'Hugo;Verstraet': 'Belgium', 'Milan;Laurent': 'Belgium', 'Niels;Mertens': 'Belgium', 'Quinten;Peeters': 'Belgium', 'Hugo;Devos': 'Belgium', 'Lars;Michel': 'Belgium', 'Ivo;Kolasinac': 'Bosnia and Herzegovina', 'Slaven;Cosic': 'Bosnia and Herzegovina', 'Adam;Mutapic': 'Bosnia and Herzegovina', 'Danko;Muratovic': 'Bosnia and Herzegovina', 'Neven;Mesic': 'Bosnia and Herzegovina', 'Nermain;Zurkic': 'Bosnia and Herzegovina', 'Adin;Basic': 'Bosnia and Herzegovina', 'Franjo;Susic': 'Bosnia and Herzegovina', 'Mirko;Koroman': 'Bosnia and Herzegovina', 'Zlatan;Nikic': 'Bosnia and Herzegovina', 'Breno;Morais': 'Brasil', 'Paulo;Fernandez': 'Brasil', 'Renan;Diaz': 'Brasil', 'Erick;Santos': 'Brasil', 'Diego;Gomes': 'Brasil', 'Caio;Cavalcanti': 'Brasil', 'Henrique;Correia': 'Brasil', 'Murilo;RibeiroPaulo': 'Brasil', 'Igor;Montes': 'Brasil', 'Renan;Ribero': 'Brasil', 'Guilherme;Sousa': 'Brasil', 'Victor;Azevedo': 'Brasil', 'Vladimir;Krasteva': 'Bulgaria', 'Zdravko;Yordanov': 'Bulgaria', 'Anton;Petrova': 'Bulgaria', ' On ;Qing': 'Chiny', 'Zhou;Hang': 'Chiny', 'Quin;Hui ': 'Chiny', 'Yang;Hou ': 'Chiny', ' Gu ;Xin ': 'Chiny', ' Dai;Qun ': 'Chiny', ' Lee;Hiro': 'Chiny', 'Zhang;Jin ': 'Chiny', 'Ante;Kovacevic': 'Croatia', 'Stjepan;Peric': 'Croatia', 'Goran;Dumjovic': 'Croatia', 'Branimir;Mesic': 'Croatia', 'Andrej;Lisak': 'Croatia', 'Kristijan;Matic': 'Croatia', 'Marko;Brlic': 'Croatia', 'Adam;Radecki': 'Czech Republic', 'Matyas;Babik': 'Czech Republic', 'Jan;Zelenka': 'Czech Republic', 'Jakub;Zima': 'Czech Republic', 'Marcus;Moller': 'Denmark', 'Andeas;Jensen': 'Denmark', 'Jakob;Sorensen': 'Denmark', 'Mathias;Andersen': 'Denmark', 'Liam;Christiansen': 'Denmark', 'Benjamin;Vad': 'Denmark', 'Anton;Hansen': 'Denmark', 'Philip;Johansen': 'Denmark', 'Simon;Nielsen': 'Denmark', 'Felix;Kristensen': 'Denmark', 'Ahmed;Mahmoud': 'Egypt', 'Moamen;Abdullah': 'Egypt', 'Hisham;Hussein': 'Egypt', 'Hasan;Ramadan': 'Egypt', 'Ismail;Adham': 'Egypt', 'Daniil;Raudsepp': 'Estonia', 'Yrjo;Ihalainen': 'Finland', 'Olavi;Koskinen': 'Finland', 'Ismo;Nurmi': 'Finland', 'Kalinikos;Doxaras': 'Greece', 'Archi;Zygomalas': 'Greece', 'Dias;Kypraios': 'Greece', 'Memnon;Karras': 'Greece', 'Iketas;Rentis': 'Greece', 'Mikheil;Kavatadze': 'Georgia', 'Paata;Mikeladze': 'Georgia', 'Gocha;Tvalavadze': 'Georgia', 'Oscar;Fernandez': 'Spain', 'Daniel;Jimenez': 'Spain', 'Carlos;Rodriguez': 'Spain', 'Mario;Diaz': 'Spain', 'Jose;Pastor': 'Spain', 'Marcos;Moreno': 'Spain', 'Tomas;Gomez': 'Spain', 'Mariano;Ortiz': 'Spain', 'Felipe;Ferrer': 'Spain', 'Luis;Mendez': 'Spain', 'Sergio;Munoz': 'Spain', 'Francisco;Ortega': 'Spain', 'Cesar;Lopez': 'Spain', 'Josep;Dominiguez': 'Spain', 'Martin;Ruiz': 'Spain', 'Manuel;Parra': 'Spain', 'Augustin;Rubio': 'Spain', 'Xavier;Suarez': 'Spain', 'Miguel;Delgado': 'Spain', 'Eduardo;Cortes': 'Spain', 'Ricardo;Carrasco': 'Spain', 'Victor;Marin': 'Spain', 'Felix;Torres': 'Spain', 'Georgio;Herrera': 'Spain', 'Pablo;Moya': 'Spain', 'Salvador;Carmona': 'Spain', 'Tomas;Fuentes': 'Spain', 'Miguel;Iglesias': 'Spain', 'Alex;Nieto': 'Spain', 'Rafael;Hidalgo': 'Spain', 'Diminigo;Blanco': 'Spain', 'Ramon;Pena': 'Spain', 'Juan;Vega': 'Spain', 'Rob;de Bruijn': 'Netherlands', 'Klaas;de Vos': 'Netherlands', ' Ido;van Veen': 'Netherlands', 'Huib;Peters': 'Netherlands', 'Sieb;van Dijk': 'Netherlands', 'Bart;Vermuelen': 'Netherlands', 'Stefan;Prins': 'Netherlands', 'Bas;van den Broek': 'Netherlands', 'Thijs;van Dam': 'Netherlands', 'Willem;Smits': 'Netherlands', 'Lars;de Boer': 'Netherlands', 'Teun;de Ruiter': 'Netherlands', 'Bas;van der Muelen': 'Netherlands', 'Luuk;Dekker': 'Netherlands', 'Valentijn;Bos': 'Netherlands', 'Vincent;Kok': 'Netherlands', 'Bart;van Beek': 'Netherlands', 'Gerard;Jacobs': 'Netherlands', 'Reyansh;Das': 'India', 'Aaryan;Patel': 'India', 'Aditya;Jayarman': 'India', 'Amit;Malhotra': 'India', 'Ajay;Banerjee': 'India', 'Arnav;Verma': 'India', 'Dani;Muhammad': 'Indonesia', 'Bagas;Fauziah': 'Indonesia', 'Bagas;Notonegoro': 'Indonesia', 'Ehsan;Sanayee': 'Iran', 'Ali;Reza Sanayi': 'Iran', 'Armin;Soltani': 'Iran', 'Sobhan;Zafari': 'Iran', 'Ilya;Niloufari': 'Iran', 'Arian;Nemati': 'Iran', 'Conor;Bryne': 'Ireland', 'Michael;Smith': 'Ireland', "Cian;O'Connor": 'Ireland', 'Luke;Murphy': 'Ireland', "Adam;O'Sullivan": 'Ireland', "Noah;O'Brien": 'Ireland', 'Michael;Kelly': 'Ireland', 'Daniel;Ryan': 'Ireland', 'Meir;Avraham': 'Israel', 'Izrael;Halperin': 'Israel', 'Yochai;Naftali': 'Israel', 'Meir;Levy': 'Israel', 'Lior;Pertez': 'Israel', 'Hashimoto;Kato': 'Japan', 'Diasuke;Aozora': 'Japan', 'Tatsuya;Hayashi': 'Japan', 'Koichi;Yamashita': 'Japan', 'Nakamura;Ota': 'Japan', 'Taiki;Nakagawa': 'Japan', 'Makoto;Ishikawa': 'Japan', 'Ysubasa;Kohei': 'Japan', 'Connor;Gauthier': 'Canada', 'Cooper;Boucher': 'Canada', 'Thomas;Anderson': 'Canada', 'Jack;Thompson': 'Canada', 'Ryan;Morin': 'Canada', 'Jorge;Fajarado': 'Colombia', 'Julio;Alvarez': 'Colombia', 'Jairo;Valencia': 'Colombia', 'Hernan;Salazar': 'Colombia', 'Oscar;Ortega': 'Colombia', 'Sergio;Restrepo': 'Colombia', 'Felipe;Velez': 'Colombia', 'Julian;Puerta': 'Colombia', 'Cesar;Pulgarin': 'Colombia', 'Fernando;Ospina': 'Colombia', 'Emilio;Fajardo': 'Colombia', 'Julio;Castano': 'Colombia', 'Humberto;Gil': 'Colombia', 'Byun;Jinho': 'South Korea', 'Yuk;Jeong-hoon': 'South Korea', ' Kim;Yeongsu': 'South Korea', ' Eun;Jin Woo': 'South Korea', 'Kang;Minjae': 'South Korea', 'Hyunwoo;Park': 'South Korea', 'Min;Seok Shim': 'South Korea', 'Eun;Jung Hoon': 'South Korea', 'Carlos;Chaves': 'Costa Rica', 'Roberto;Mora': 'Costa Rica', 'Adrian;Hernandez': 'Costa Rica', 'Gerarod;Vargas': 'Costa Rica', 'Zakaria;Acemrar': 'Morocco', 'Oussama;Acemar': 'Morocco', 'Hamza;Ahelluc': 'Morocco', 'Adil;Mezyan': 'Morocco', 'Ayoub;Amghar': 'Morocco', 'Brahim;Awragh': 'Morocco', 'Miguel;Olvera': 'Mexico', 'Manuel;del Angel': 'Mexico', 'Rodolfo;Camacho': 'Mexico', 'Rafael;Velazquez': 'Mexico', 'Martin;Salazar': 'Mexico', 'Tomas;Rubio': 'Mexico', 'Santiago;Escobar': 'Mexico', 'Jesus;Arredondo': 'Mexico', 'Juan;Zavala': 'Mexico', 'Isidro;Carmona': 'Mexico', 'Saul;Carbajal': 'Mexico', 'Ignacio;Roman': 'Mexico', 'Jesus;Rojas': 'Mexico', 'Benito;Arellano': 'Mexico', 'Jose;Leyva': 'Mexico', 'Edurado;Colin': 'Mexico', 'David;Mendoza': 'Mexico', 'Jorge;Varela': 'Mexico', 'Ruben;Angel': 'Mexico', 'Jose;Magana': 'Mexico', 'Joel;Ventura': 'Mexico', 'Jesus;Rivas': 'Mexico', 'Omar;Villegas': 'Mexico', 'Esteban;Baez': 'Mexico', 'Salahudeen;Bala': 'Nigeria', 'Bayo;Adegoke': 'Nigeria', 'Teslim;Oyleleke': 'Nigeria', 'Tosin;Dutse': 'Nigeria', 'Salahuedeen;Obi': 'Nigeria', 'Aanu;Ifedolapo': 'Nigeria', 'Bayo;Dan-Asebe': 'Nigeria', 'Muyiwa;Kuta': 'Nigeria', 'Salisu;Aladegbaiye': 'Nigeria', ' Per;Saether': 'Norway', 'Hakon;Naess': 'Norway', 'Fredrik;Vik ': 'Norway', 'Lars;Johanssen': 'Norway', 'Rune;Karlsen': 'Norway', 'Per;Henriksen': 'Norway', 'Jonas;Amundsen': 'Norway', 'Luke;Lacy': 'New Zealand', 'Alex;Ackroyd': 'New Zealand', 'Samuel;Burns': 'New Zealand', 'Lucas;Halliday': 'New Zealand', 'William;Harlen': 'New Zealand', 'Andrew;Marshall': 'New Zealand', 'Finn;Weastell': 'New Zealand', 'Bilal;Paracha': 'Pakistan', 'Arsalan;Siddiqui': 'Pakistan', 'Hasan;Bukhari': 'Pakistan', 'Kamil;Szymczak': 'Poland', 'Robert;Adamczyk': 'Poland', 'Antoni;Okulski': 'Poland', 'Wojciech;Wilk': 'Poland', 'Jacek;Koziej': 'Poland', 'Mateusz;Lasocki': 'Poland', 'Adam;Szczepaniak': 'Poland', 'Piotr;Kotecki': 'Poland', 'Sebastian;Grabski': 'Poland', 'Jan;Janik': 'Poland', 'Maciej;Mazurek': 'Poland', 'Jozef;Bielecki': 'Poland', 'Marek;Nowak': 'Poland', 'Lucas;Marques': 'Portugal', 'Andre;Lourenco': 'Portugal', 'Francisco;Vieira': 'Portugal', 'Duarte;Freitas': 'Portugal', 'Simao;Martins': 'Portugal', 'Miguel;Correia': 'Portugal', 'Afonso;Pereira': 'Portugal', 'David;Santos': 'Portugal', 'Tomas;Gomes': 'Portugal', 'Santiago;Jesus': 'Portugal', 'Santiago;Sousa': 'Portugal', 'Rafael;Azevedo': 'Portugal', 'Guilherme;Lopes': 'Portugal', 'Diogo;Carvalho': 'Portugal', 'Rodrigo;Araujo': 'Portugal', 'Andre;Reis': 'Portugal', 'Martim;Ferreira': 'Portugal', 'Eduard;Jurkov': 'Russia', 'Bogdan;Kovalev': 'Russia', 'Vladimir;Yashin': 'Russia', 'Nazar;Zhuravlev': 'Russia', 'Konstantin;Zukov': 'Russia', 'David;Solowow': 'Russia', 'Jurij;Chudyakow': 'Russia', 'Taras;Melnik': 'Russia', 'Todor;Livescu': 'Romania', 'Anghel;Rusu': 'Romania', 'Romeo;Filiotti': 'Romania', 'Basarab;Barca': 'Romania', 'Florea;Proca': 'Romania', 'Vaclav;Strba': 'Slovakia', 'Radomir;Vajda': 'Slovakia', 'Bouhmir;Peska': 'Slovakia', 'Pravoslav;Pauk': 'Slovakia', 'Tadeas;Simko': 'Slovakia', 'Blaz;Pirc': 'Slovenia', ' Rok;Bozic': 'Slovenia', 'Aljoz;Golob': 'Slovenia', 'Jan;Horvat': 'Slovenia', 'Jerry;Meyers': 'USA', 'Walter;Dean': 'USA', 'Randy;Adams': 'USA', 'William;Miller': 'USA', 'Howard;Valdez': 'USA', 'Dylan;Barnett': 'USA', 'Ronald;Brewer': 'USA', 'Dennis;Torres': 'USA', 'Gerald;Walker': 'USA', 'Peter;Baumann': 'Switzerland', 'Christian;Wyss': 'Switzerland', 'Andreas;Meyer': 'Switzerland', 'Daniel;Frei': 'Switzerland', ' Urs;Zimmermann': 'Switzerland', 'Andreas;Strand': 'Sweden', 'Jesper;Lijegren': 'Sweden', 'Erik;Wahlgren': 'Sweden', 'Arvid;Zetterberg': 'Sweden', 'Joel;Wissel': 'Sweden', 'Carl;Wiberg': 'Sweden', 'Wrik;Blomberg': 'Sweden', 'Cenk;Ayhan': 'Turkey', ' Cem;Citak': 'Turkey', 'Velit;Yazci': 'Turkey', 'Raman;Dereli': 'Turkey', 'Yousuf;Acar': 'Turkey', 'Fahir;Ozcan': 'Turkey', 'Memduh;Ozgur': 'Turkey', 'Vasil;Bondarenko': 'Ukraine', 'Mykola;Gritsenko': 'Ukraine', 'Igor;Zoshenko': 'Ukraine', 'Krill;Vinichenko': 'Ukraine', 'Scorba;Miklos': 'Hungary', 'Gellert;Tivadar': 'Hungary', 'Roka;Lazar': 'Hungary', 'Palotas;Oliver': 'Hungary', 'Redei;Elemer': 'Hungary', 'Juhos;Balazs': 'Hungary', 'Scoti;Kornel': 'Hungary' }
#384 names, 384 surnames

formation = [4,4,2]

fNums = [
[3,5,2],
[3,3,4],
[3,4,3],
[3,2,5],
[4,5,1],
[4,4,2],
[4,2,4],
[4,3,3],
[4,1,5],
[5,4,1],
[5,3,2],
[5,1,4],
[5,2,3]
    ]
fName = [

'352',
'352 offensive',
'343',
'343 offensive',
'451',
'442',
'442 offensive',
'433',
'433 offensive',
'541',
'532',
'532 offensive',
'523'
    ]

def printFormation(f):
    s = '     '
    p = ' ATK '
    print('','_'*31)
    print('|',s,s,s,s,s,'|')
    if f[2] == 1:
        print('|',s,s,p,s,s,'|')
        print('|',s,s,s,s,s,'|')
    elif f[2] == 2:
        print('|   ',s,p,p,s,'   |')
        print('|',s,s,s,s,s,'|')
    elif f[2] == 3:
        print('|',s,p,s,p,s,'|')
        print('|',s,s,p,s,s,'|')
    elif f[2] == 4:
        print('|   ',s,p,p,s,'   |')
        print('|',p,s,s,s,p,'|')
    elif f[2] == 5:
        iD = fNums.index(f)
        if fName[iD] == '433 offensive':
            print('|',p,s,p,s,p,'|')
            print('|',s,p,s,p,s,'|')
        else:
            print('|',s,p,s,p,s,'|')
            print('|',p,s,p,s,p,'|')
    p = ' MID '
    if f[1] == 1:
        print('|',s,s,s,s,s,'|')
        print('|',s,s,p,s,s,'|')
    elif f[1] == 2:
        print('|',s,s,s,s,s,'|')
        print('|   ',s,p,p,s,'   |')
    elif f[1] == 3:
        print('|',s,s,s,s,s,'|')
        print('|',s,p,p,p,s,'|')
    elif f[1] == 4:
        print('|',p,s,s,s,p,'|')
        print('|   ',s,p,p,s,'   |')
    elif f[1] == 5:
        print('|',p,s,s,s,p,'|')
        print('|',s,p,p,p,s,'|')
    p = ' DEF '
    if f[0] == 3:
        print('|',s,s,s,s,s,'|')
        print('|',s,p,p,p,s,'|')
    elif f[0] == 4:
        print('|',s,s,s,s,s,'|')
        print('|   ',p,p,p,p,'   |')
    elif f[0] == 5:
        print('|',p,s,s,s,p,'|')
        print('|',s,p,p,p,s,'|')

    print('|',s,s,s,s,s,'|')
    print('|',s,s,' GKP ',s,s,'|')
    print('','_'*31)

def printFirstTeam():
    s = '        '
    ps = []                             #FORWARDS
    for i in atackers:
        ps.append(i[2])

    for i, item in enumerate(ps):
        if len(item) == 4:
            ps[i] = '  '+item.upper()+'  '
        elif len(item) == 5:
            ps[i] = '  '+item.upper()+' '
        elif len(item) == 6:
            ps[i] = ' '+item.upper()+' '
        elif len(item) == 7:
            ps[i] = ' '+item.upper()
        else:
            ps[i] = item.upper()
        
    while len(ps) < formation[2]:
        ps.append(' forward')
    if len(ps) == 1:
        print()
        print (s,s,ps[0])
    if len(ps) == 2:
        print()
        print('    '+s,ps[0],ps[1])
    if len(ps) == 3:
        print(s,ps[0],s,ps[1])
        print(s,s,ps[2])
    if len(ps) == 4:
        print('    ',s,ps[0],ps[1])
        print(ps[2],s,s,s,ps[3])
    if len(ps) == 5:
        iD = fNums.index(formation)
        if fName[iD] == '433 offensive':
              print(ps[0],s,ps[1],s,ps[2])
              print(s,ps[3],s,ps[4])
        else:
            print(s,ps[0],s,ps[1])
            print(ps[2],s,ps[3],s,ps[4])
    print()
    
    ps = []                         #MIDFIELDERS
    for i in midfielders:
        ps.append(i[2])

    for i, item in enumerate(ps):
        if len(item) == 4:
            ps[i] = '  '+item.upper()+'  '
        elif len(item) == 5:
            ps[i] = '  '+item.upper()+' '
        elif len(item) == 6:
            ps[i] = ' '+item.upper()+' '
        elif len(item) == 7:
            ps[i] = ' '+item.upper()
        else:
            ps[i] = item.upper()
    
    while len(ps) < formation[1]:
        ps.append('midfield')
    if len(ps) == 1:
        print()
        print (s,s,ps[0])
    if len(ps) == 2:
        print()
        print('    '+s,ps[0],ps[1])
    if len(ps) == 3:
        print()
        print(s,ps[0],ps[1],ps[2])
    if len(ps) == 4:
        print(ps[0],s,s,s,ps[3])
        print('    ',s,ps[1],ps[2])
    if len(ps) == 5:
        print(ps[0],s,s,s,ps[4])
        print(s,ps[1],ps[2],ps[3])
    print ()

    ps = []                         #DEFENDERS
    for i in defenders:
        ps.append(i[2])

    for i, item in enumerate(ps):
        if len(item) == 4:
            ps[i] = '  '+item.upper()+'  '
        elif len(item) == 5:
            ps[i] = '  '+item.upper()+' '
        elif len(item) == 6:
            ps[i] = ' '+item.upper()+' '
        elif len(item) == 7:
            ps[i] = ' '+item.upper()
        else:
            ps[i] = item.upper()
            
    while len(ps) < formation[0]:
        ps.append('defender')
    if len(ps) == 3:
        print()
        print(s,ps[0],ps[1],ps[2])
    if len(ps) == 4:
        print()
        print('    ',ps[0],ps[1],ps[2],ps[3])
    if len(ps) == 5:
        print(ps[0],s,s,s,ps[4])
        print(s,ps[1],ps[2],ps[3])
    print ()

    ps = []                         #GOALKEEPER
    for i in goalkeeper:
        ps.append(i[2])

    for i, item in enumerate(ps):
        if len(item) == 4:
            ps[i] = '  '+item.upper()+'  '
        elif len(item) == 5:
            ps[i] = '  '+item.upper()+' '
        elif len(item) == 6:
            ps[i] = ' '+item.upper()+' '
        elif len(item) == 7:
            ps[i] = ' '+item.upper()
        else:
            ps[i] = item.upper()
            
    if len(ps) == 0:
        ps.append(' keeper ')
    print()
    print(s,s,ps[0])

premier_league = [ # 3 relegated
["Arsenal", 8.9],
["Aston Villa", 7.4],
["Bournemouth", 7.8],
["Brighton & Hove Albion", 8.1],
["Burnley", 8.4],
["Chelsea", 9.4],
["Crystal Palace", 8.5],
["Everton", 8.7],
["Leicester City", 9.0],
["Liverpool", 10],
["Manchester City", 9.8],
["Manchester United", 9.6],
["Newcastle United", 8.3],
["Norwich City", 7.5],
["Sheffield United", 8.6],
["Southampton", 8.3],
["Tottenham Hotspur", 9.2],
["Watford", 8.3],
["West Ham United", 8.2],
["Wolverhampton Wanderers", 8.8]
    ]
championship = [ # 3 relegated, 3 promotion (play-offs)
["Barnsley", 6.4],
["Birmingham City", 7.7],
["Blackburn Rovers", 7.5],
["Brentford London", 7.0],
["Bristol City", 6.8],
["Cardiff City", 7.6],
["Charlton Athletic", 6.5],
["Derby County", 6.7],
["Fulham London", 7.2],
["Huddersfield Town", 7.1],
["Hull City", 7.5],
["Leeds United", 7.1],
["Luton Town", 6.5],
["Middlesbrough", 7.4],
["Millwall", 6.7],
["Nottingham Forest", 6.9],
["Preston North End", 6.9],
["Queens Park Rangers", 7.4],
["Reading", 7.3],
["Sheffield Wednesday", 6.6],
["Stoke City", 8.2],
["Swansea City", 7.9],
["West Bromwich Albion", 8.0],
["Wigan Athletic", 7.8]
    ]
league_one = [ # 4 relegated, 3 promotion (play-offs)
["Accrington Stanley", 4.8],
["AFC Wimbledon", 4.7],
["Blackpool", 5.1],
["Bolton Wanderers", 4.5],
["Bristol Rovers", 5.0],
["Burton Albion", 5.2],
["Coventry City", 6.3],
["Doncaster Rovers", 5.5],
["Fleetwood Town", 5.8],
["Gillingham", 5.4],
["Ipswich Town", 5.3],
["Lincoln City", 4.9],
["Milton Keynes Dons", 4.7],
["Oxford United", 6.0],
["Peterborough United", 5.7],
["Portsmouth", 5.9],
["Rochdale", 4.8],
["Rotherham United", 6.2],
["Shrewsbury Town", 5.0],
["Southend United", 4.5],
["Sunderland", 5.6],
["Tranmere Rovers", 4.6],
["Wycombe Wanderers", 6.1],
["Swindon Town", 4.7]
    ]
league_two = [ # 2 relegated, 4 promotion (play-offs)
["Bradford City", 4.0],
["Carlisle United", 3.2],
["Cambridge United", 3.4],
["Cheltenham Town", 4.4],
["Colchester United", 4.2],
["Crawley Town", 3.6],
["Crewe Alexandra", 4.6],
["Exeter City", 4.3],
["Forest Green Rovers", 3.9],
["Grimsby Town", 3.5],
["Leyton Orient", 3.3],
["Macclesfield Town", 2.9],
["Mansfield Town", 3.0],
["Morecambe", 2.9],
["Newport County", 3.6],
["Northampton Town", 4.1],
["Oldham Athletic", 3.1],
["Plymouth Argyle", 4.5],
["Port Vale", 4.1],
["Salford City", 3.8],
["Scunthorpe United", 3.0],
["Stevenage", 2.8],
["Walsall", 3.7],
["Barrow", 2.5]
    ]

national_league = [ # 2 promotion
["Aldershot Town", 1.5],
["Barnet", 1.8],
["Boreham Wood", 2.1],
["Bromley", 1.7],
["Chesterfield", 1.4],
["Chorley", 1.1],
["Dagenham & Redbridge", 1.5],
["Dover Athletic", 1.8],
["Eastleigh", 1.5],
["Ebbsfleet United", 1.3],
["Fylde", 1.1],
["Halifax Town", 2.1],
["Harrogate Town", 2.4],
["Hartlepool United", 1.9],
["Maidenhead United", 1.2],
["Notts County", 2.3],
["Solihull Moors", 2.0],
["Stockport County", 2.0],
["Sutton United", 1.7],
["Torquay United", 1.6],
["Woking", 1.9],
["Wrexham", 1.3],
["Yeovil Town", 2.2],
['Braintree Town',1.1]
    ]

#kiedy bede robil rozgrywki miedzynarodowe to wystarczy ulozyc te kluby w
#kolejnosci jak sa dobre co juz jest prawie zrobione (trzeba dodac z Prem. League)
#i po prostu do Ligi Mistrzow brac iles pierwszych zespolow i losowac reszte tak
#im sa wyzej to wieksza szansa ze trafia
#lige europy analogicznie
world_teams = [         #mozna dodac po przecinku average sile zespolu
['Bayern Munchen'],
['Real Madrit FC'],
['FC Barcelona'],
['Atletico Madrit'],
['Paris Saint Germain'],
['Juventus Turin'],
['SSC Napoli'],
['AS Roma'],
['Inter Milan'],
['AC Milan'],
['Lazio Roma'],
['Borussia Dortmund'],
['AFC Ajaks'],
['FC Porto'],
['Sevilla FC'],
['SL Benifica'],
['Olympiqe Lyon'],
['AS Roma'],
['Sporting Lisbona'],
['RB Lepizg'],
# tu troche gorsze: (mniej wiecej od najlepszych do gorszych
['Atalanta BC'],
['CR Flamengo'],
['Atletico Mineiro'],
['Villarreal'],
['Bayer Leverkusen'],
['Red Bull Salzburg'],
['FK Red Star Belgrade'],
['Slavia Prague'],
['Real Soxiedad'],
['Al Ahly Kair'],
['CA River Plate'],
['Olympiacos SFP'],
['Eintracht Frankfurt'],
['Real Betis'],
['Borussia Monchengladbach'],
['Lille OSC'],
['Shakhtar Donetsk'],
['Olympique Lyon'],
['VfL Wolfsburg'],
['BSC Young Boys'],
['Rangers FC'],
['FC Sheriff'],
['Flora Tallinn'],
['PSV Eindhoven'],
['Zenit St. Petersburg'],
['Dynamo Kyiv'],
['Dinamo Zagreb'],
['Boca Juniors'],
['FC Union Berlin'],
['SC Freiburg'],
['Athletic Bilbao'],
['SE Palmeiras'],
['SC Internacional'],
['Monaco'],
['Partizan Beograd'],
['Valencia CF'],
['Club Brugge'],
['US Sassuolo Calcio'],
['Sparta Prague'],
['AZ Alkmaar'],
['Celta Vigo'],
['Sao Paulo FC'],
['ACF Fiorentina'],
['Feyenoord'],
['Hoffenheim'],
['FSV Mainz'],
['OGC Nice'],
['UC Sampdoria'],
['SC Corinthians'],
['SC Braga'],
['Olympique Marseille'],
['Celtic FC'],
['Besiktas JK'],
['Galatasaray SK'],
['Stade Rennais'],
['Lokomotiv Moskva'],
['VfB Stuttgart'],
['Fenerbahce SK'],
['FC Basel'],
['FC Koln'],
['Bologna FC'],
['FC Kobenhavn'],
['CSKA Moskva'],
['Santos FC'],
['Montpellier HSC'],
['Malmo FF'],
['Torino FC'],
['AEK Ateny'],
['Spartak Moskva'],
['FC Krasnodar'],
['Cadiz CF'],
['Fortuna Dusseldorf'],
['FC Nantes'],
['Hertha BSC'],
['Hamburger SV'],
['Empoli FC'],
['Getafe CF'],
['Legia Warszawa'],
['RSC Anderlecht'],
['Lech Poznan'],
['']
    ]

sponsorName = ['Odds And Ends', 'Handy Help', 'Knick Knacks', 'Nick’S Knacks', 'Here And There And Everywhere', 'Et Cetera Systems', 'Et Cetera', 'Et Cetera Solutions', 'Closet Of Choices', 'Random Reasoning', 'Random Assortment', 'Assorted Assets', 'Trusted Assortment', 'Applicable Assortment', 'Random Row', 'Random Reason', 'Random Riders', 'Random Repair', 'Random Resource', 'Resource Refresh', 'Random Refresh', 'The Source', 'Complete Collection', 'Sporadic Systems', 'Sufficient Support', 'Random Release', 'Random Report', 'Random Warehouse', 'Wanted Warehouse', 'Full Force', 'Complete Competition', 'Forge Ahead', 'Make It Count', 'Count Your Blessings', 'Creative Content', 'Content Construct', 'Clever Counts', 'Counted Moments', 'Make It Count', 'Random Wishes', 'Wishful Wants', 'Dream Collection', 'Contribution Collection', 'Rock And Random', 'Race To Random', 'Knick Knack Patty Wack', 'Trinkets And Toys', 'Terrific Tchotchkes', 'Close Crowds', 'Absent-Minded', 'Airhead', 'Accidental Kindness', 'Odd And Ends', 'X Marks The Spot', 'Adventures', 'Essentials', '23Rd Century', 'Spiritual Beings', 'Life Paths', 'Shady Bootz', 'Missed Opps', 'In A Pinch', 'Empty Particles', 'Tainted', 'Botched', 'Communities', 'Locations', 'Dirty Mirrors', 'Stitched', 'Sparkles', 'Splashfest', 'Besmirched', 'Seemusicplay', 'Finder’S Keepers', 'Calm Down', 'Turnt Up Tunes', 'Encountered', 'Located', 'Sighted', 'Ferrets Live', 'Calm Down', 'We Live Alive', 'Pointed Out', 'Working Girlz', 'Hook And Eye', 'Snapshot', 'Shotclock', 'Hidden Treasures', 'Fast And Fly', 'Wild Irish Flowers', 'Buckle Up Kids', 'Cleaner Days', 'Heavy Lives', 'appa Shop', 'Forel Library', 'Node Tech', 'PrimeHouse', 'DualLight', 'Voice Caption Center', 'FursKips', 'Limner Studio', 'XyloFurniture', 'Pop-Culture', 'Spray Shop', 'Find Agenda', 'CraftCreate', 'FirstVictory', 'MoonStore', 'Silence Center', 'WildWest', 'Heart Beat', 'Legend Soul', 'Winter Shop', 'TV-Partner', 'LiftCenter', 'Forest Shop', 'MusicMany', 'BreakDown', 'Lion Family', 'Level Travel', 'Ethnic Shop', 'Early Bird', 'Soprano House', 'Red Room', 'Novel Center', 'Modestico', 'First Award', 'Traffic Center', 'Ice Castle', 'KnowChance', 'XPand', 'NoWorries', 'Elegance', 'Win Ribbon', 'Rent Platform', 'ZeroClerk', 'ReactRegister', 'Paper City', 'Witch Union', 'Poem House', 'Graphic Master', 'ReadySketch', 'Live Symbol', 'Fresh Accent', 'Flash Illusion', 'Bluelake Realtors', 'Yummy Meals', 'Best Bytes', 'Kino Energy', 'Saturn Wipers', 'Poseidon’S Plates', 'Distinct Clips', 'Argo Energy', 'Arc Security', 'Fentech Batteries', 'Crystal Diner', 'Crwonville Hotels', 'Seaview Properties', 'Upsea Constructions', 'Maxx Dry-Cleaning', 'Rexx Energy', 'Yellow Essence', 'Natural Essentials', 'Castleview Hotels', 'Valleyview Diners', 'Atlas Stationary', '+Shops', 'Mindnsoles', 'Uniquetrac', 'Supremeboots', 'Ten Fold Security', 'Daily Rise', 'Aqua +', ',Blue Smoke', 'Chloe’S Corner', 'Midsummer Night Grill', 'Mulletmasters', 'Spicy Dinner', 'Supremeplanners', 'Crazy Chicken', 'Madmullet', 'Allyouneed', 'Weheartsandals', 'Sunrisescones', 'Clear Prints', 'Westend Schools', 'Tall Oaks Bamboo', 'Bluewhale Surfboards', 'Wavefest Surfboards', 'Unique Trends', 'For The Couture', 'Dynapower', 'Gravitywears', 'Better Leather', 'Gorgunderwears']
stadiumSponsored = 0


#FIRST TEAM PRINTED AS LIST:

#needPlayers = ''
#if len(data.goalkeeper) < 1:
#        needPlayers = '\t*PLAYERS NEEDED*'
#print ("\nGOALKEEPER",'\t',needPlayers)
#if data.goalkeeper:
#        for i in data.goalkeeper:
#                print ('\tskill ' + str(i[0]),'\t',data.GetName(i))
#needPlayers = ''
#if len(data.defenders) < data.formation[0]:
#        needPlayers = '\t*PLAYERS NEEDED*'
#print ("\nDEFENDERS ",' - ',data.formation[0],needPlayers)
#if data.defenders:
#        for i in data.defenders:
#                print ('\tskill ' + str(i[0]),'\t',data.GetName(i))
#needPlayers = ''
#if len(data.midfielders) < data.formation[1]:
#        needPlayers = '\t*PLAYERS NEEDED*'
#print ("\nMIDFIELDERS",'- ',data.formation[1],needPlayers)
#if data.midfielders:
#        for i in data.midfielders:
#                print ('\tskill ' + str(i[0]),'\t',data.GetName(i))
#needPlayers = ''
#if len(data.atackers) < data.formation[2]:
#        needPlayers = '\t*PLAYERS NEEDED*'
#print ("\nFORWARDS  ",' - ',data.formation[2],needPlayers)
#if data.atackers:
#        for i in data.atackers:
#                print ('\tskill ' + str(i[0]),'\t',data.GetName(i))
