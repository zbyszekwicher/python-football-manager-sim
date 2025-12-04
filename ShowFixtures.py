import data

print ("\n" * data.freeSpace)
print ("FIXTURES")
for i in data.fixtures:
    if len(i) < 3:
        print ('     \t'+i[0])
    else:
        print (i[2]+'\t'+i[0])

inp = input("\n0 - back\n")
correctAnswer = "0"

while inp != correctAnswer:
    inp = input("That is not a correct answer! Type number of option you want to chose\n")

if inp == "0":
    print ("wyszedlem")
    exec(open("FixturesAndLeague.py").read())
