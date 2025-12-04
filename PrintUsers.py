import data
import os

directory = data.path+'\\saves\\'

def Users():
    userName = ''
    users = []
    for filename in os.listdir(directory):
        filePath = (os.path.join(directory+filename))
        try:
            file = open(filePath)
            try:
                all_lines = file.readlines()
                userName = all_lines[0].replace("\n", "")
            finally:
                file.close()

        except IOError:
            print("Opening files error")

        if not userName in users:
            users.append(userName)

    return(users)


