from random import randrange,choice
import data

def CreateNewPlayer(howGood, position, nationality):
    if nationality == 'England':
        firstname = data.playerNameENG[randrange(len(data.playerNameENG))]
        surname = data.playerSurnameENG[randrange(len(data.playerSurnameENG))]
        used = []
        for i in data.playerTeam:
            used.append(i[2])
        while surname in used or surname == firstname:
            surname = data.playerSurnameITA[randrange(len(data.playerSurnameITA))]
    elif nationality == 'Italian':
        firstname = data.playerNameITA[randrange(len(data.playerNameITA))]
        surname = data.playerSurnameITA[randrange(len(data.playerSurnameITA))]
        used = []
        for i in data.playerTeam:
            used.append(i[2])
        while surname in used or surname == firstname:
            surname = data.playerSurnameITA[randrange(len(data.playerSurnameITA))]
    elif nationality == 'French':
        firstname = data.playerNameFRA[randrange(len(data.playerNameFRA))]
        surname = data.playerSurnameFRA[randrange(len(data.playerSurnameFRA))]
        used = []
        for i in data.playerTeam:
            used.append(i[2])
        while surname in used or surname == firstname:
            surname = data.playerSurnameFRA[randrange(len(data.playerSurnameFRA))]
    elif nationality == 'German':
        firstname = data.playerNameGER[randrange(len(data.playerNameGER))]
        surname = data.playerSurnameGER[randrange(len(data.playerSurnameGER))]
        used = []
        for i in data.playerTeam:
            used.append(i[2])
        while surname in used or surname == firstname:
            surname = data.playerSurnameGER[randrange(len(data.playerSurnameGER))]
    elif nationality == 'Other':
        if howGood > 7:
            howGood -= 1
        x = choice(list(data.playerNameREST.items()))
        surname = x[0].split(';')[1]
        used = []
        for i in data.playerTeam:
            used.append(i[2])
        while surname in used:
            x = choice(list(data.playerNameREST.items()))
            surname = x[0].split(';')[1]
        nationality = data.playerNameREST[x[0]]

        x = choice(list(data.playerNameREST.items()))
        while x[1] != nationality:
            x = choice(list(data.playerNameREST.items()))
            
        firstname = x[0].split(';')[0]
        
        
    age = randrange(16,35)

    if age <= 26:
        ageModifier = age/10
    elif age == 27:
        ageModifier = 2.4
    elif age == 28:
        ageModifier = 2.2
    elif age == 29:
        ageModifier = 2.0
    elif age == 30:
        ageModifier = 1.8
    elif age == 31:
        ageModifier = 1.6
    elif age == 32:
        ageModifier = 1.4
    elif age == 33:
        ageModifier = 1.2
    elif age == 34:
        ageModifier = 1.0
    else:
        ageModifier = 0.8

    if age >= 31:
        skill = howGood
    elif age >= 22:
        skill = howGood
    elif age >= 19:
        skill = howGood - 1
    else:
        skill = howGood - 2
    if skill < 1:
        skill = 1

    r = randrange(91, 110)
    marketValue = round(skill * skill * r * ageModifier)

    g = 0#goals     [9]
    a = 0#asists    [10]
    m = 0#matches   [8]
    defalut_stamina = 10
    
    return [skill, firstname, surname, position, age, marketValue, nationality, defalut_stamina, m, g, a]
