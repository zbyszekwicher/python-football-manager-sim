import data
for i in data.finances:
    if i == '':
        data.finances.remove('')

x = 1
while x == 1:
    print ("\n" * data.freeSpace)
    print ("FINANCES\n")
    print ('BUDGET: ',data.budget,'000')

    print('\n(DISABLED)')
    print ('1 - budget history')
    print ('2 - total incomings and spendings')#TO DO - this week/this season/all the time
    print ('0 - main menu')

    inp = input ('\nType number\n')


    while not inp in ('1','2','0'):
        inp = input ('Incorrect input\n')

    if inp == '0':
        exec(open("MainMenu.py").read())
    elif inp == '1':
        print ("\n" * data.freeSpace)
        print ('HISTORY OF INCOMINGS AND SPENDINGS\n')
        print (' income\t\t total\t\t  decsription')
        for i in data.finances:
            print (i)
        input('continue\n')
    elif inp == '2':
        """
        print ("\n" * data.freeSpace)
        income = 0
        spending = 0
        for i in data.finances[1:]:
            fin = i.split(' 000   \t')
            if fin[0][0] == '-':
                spending += int(fin[0])
            else:
                income += int(fin[0])
                
        print ('INCOMINGS')
        print ('\t ',income)
        print ('SPENDINGS')
        print ('\t',spending)
        print ('TOTAL')
        print ('\t',income+spending)
        """
        input ('\ncontinue\n')
