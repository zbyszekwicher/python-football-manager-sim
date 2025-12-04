
"""
zrobic zeby symulowac wszystkie mecze ligi
+tabela ligi ze szczegolami kazdego klubu
+najpierw mozna losowo kazdy z kazdym na podstawie fixtures
+trzeba od fixtures odjac losowo jedna druzyne zeby bylo parzyscie
+informacja o tym kto przechodzi do wyzszej ligi + najslabsze pod wzgledem sily
    zespoly spadaja do tej ligi
+informacja o tym kto spada do nizszej ligi + najlepsze pod wzgledem sily
    zespoly awansuja do tej ligi

dodac wypozyczenia
    ze mozna w trakcie sezonu zaplacic i wypozyczyc pilkarza do konca sezonu
    tylko pilkarze o ocenie 5 lub mniej
    tylko pilkarze w wieku 16-21
    cena to lekko powiekszona pensja pilkarza
    w kazdym tygodniu mozna sprawdzac oferty

    jesli gracz ma malo pilkarzy na konretnej pozycji
    to moze dostac alert ze jest opcja wypozyczenia

    mozna rowniez dodac pilkarza do listy na wypozyczenie
    mozna otrzymac oferte i do konca sezonu pilkarz jest wypozyczony jesli sie
    gracz zgodzi
    cena - pensja pilkarza


dodac SKAUTOW zeby mozna bylo zatrudnic go i wskazac jakich pilkarzy sie szuka
    i on pokazuje takie oferty na okienku transferowym
    nowy plik - zatrudnianie i ustalanie preferencji skauta

    +placenie za skautow tam gdzie sie placi pilkarzom 1 000 za sezon
    +przypomnienie o zmianie preferencji kiedy sie zbliza okienko
    +1 000 kosztuje zatrudnienie i 1 000 kosztuje zwolnienie skauta
    +kazdy skaut pokazuje trzech pilkarzy w danej preferencji na okienku

    +po awansie do league one dostajesz info ze zarzad klubu zatrudnil skauta
        da sie go potem zwolnic ofc
        wiec z automatu gracz ma skauta

dodac styl gry pilkarza - osobne style gry na każdej pozycji
dodac taktyke - dla kazdej formacji mozliwy wybor konretnych taktyk ktore daja
    bonusy w zaleznosci od pilkarzy z konretnymi stylami gry

rozbudowac funkcje ogladania meczu - dokladny komentarz

"""


#OGOLNIE TO DZIALA.
#Mozna tylko zrobic zeby byl plik .exe i zrobione


import data
import PrintUsers

print("\n" * data.freeSpace)
if data.playerName == '':
    print("Hello in Football Manager!")
    print()
    us = PrintUsers.Users()
    if us:
        print('Users:')
        for i in us:
            print(i)
    else:
        print('There are no users yet')
    print()

    while data.playerName == '':
        print("Whats your nickname? Type it correctly, in other case you will not have access to your saved clubs")
        data.playerName = input()

exec(open("GameStarter.py").read())

# import os
# os.system("GameStarter.py")

# Enyoj
