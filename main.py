# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import numpy as np
import matplotlib.pyplot as plp

Lista = [i + 1 for i in range(100)]
def dzielniki(x):
    ### Funkcja podaje liste dzielników danej liczby ###
    dziel=[]
    if type(x) != int:
        print("Proszę podać liczbę całkowitą.")
    else:
        i = x
        while i >0:
            if x%i == 0:
                dziel.append(i)
            i=i-1
    return(dziel)
print("Jeśli chcesz grać z botem wciśnij 1, z drugim graczem wciśnij 2 a jeśli chcesz obejrzeć pojedynek botów, wciśnij 3.")
tryb_gry = int(input())
if tryb_gry == 2:
    print("Niech gracz 1 wybierze liczbę")
    a = int(input())
    print("Niech drugi gracz wybierze liczbę")
    b = int(input())
    if a == b:
        print("Obaj gracze wybrali taką samą liczbe")
        exit()
    i = 0
    x = 10
    y = 10
    while a in Lista and b in Lista:
        if i % 2 == 0:
            print("Niech gracz 1 wybierze liczbę do usunięcia")
            c = int(input())
            for j in dzielniki(c):
                Lista[j - 1] = 'x'

        else:
            print("Niech gracz 2 wybierze liczbę do usunięcia")
            c = int(input())
            for j in dzielniki(c):
                Lista[j - 1] = 'x'
        i = i + 1
        mlista = [Lista[j:j + 10] for j in range(0, len(Lista), 10)]
        for l in mlista:
            print(l)

    if a in Lista and b not in Lista:
        print("Gracz 1 wygrywa")
    elif b in Lista and a not in Lista:
        print("Gracz 2 wygrywa")
    else:
        print("Remis")
elif tryb_gry == 1:
    print("Wybierz liczbe")
    a = int(input())
    b = random.choice(Lista)
    if a == b:
        print("Gracz i bot wybrali liczbę ", a, "Należy rozpocząć nową grę.")
        exit()
    i = 0
    Lista2 = [i for i in range(1,100) if i != b]
    while a in Lista and b in Lista:
        if i % 2 == 0:
            print("Niech gracz wybierze liczbę do usunięcia")
            c = int(input())
            if c == a:
                print("Wybrałeś do usunięcia swoją liczbę. Proszę wybierz inną liczbe w następnej turze.")
            else:
                for j in dzielniki(c):
                    Lista[j - 1] = 'x'
                Lista2 = [i for i in Lista2 if not i in dzielniki(c)]



        else:
            c = random.choice(Lista2)
            print("Bot wybrał liczbę", c)
            for j in dzielniki(c):
                Lista[j - 1] = 'x'
            Lista2 = [i for i in Lista2 if not i in dzielniki(c)]
        i = i + 1
        mlista = [Lista[j:j + 10] for j in range(0, len(Lista), 10)]
        for l in mlista:
            print(l)
    if a in Lista and b not in Lista:
        print("Gracz 1 wygrywa, liczba bota to", b)
    elif b in Lista and a not in Lista:
        print("Bot wygrywa, liczba gracza to", a)
    else:
        print("Remis")
elif tryb_gry == 3:
    Lista1 = list(Lista)
    a = random.choice(Lista)
    print("Bot 1 wybrał liczbę ",a ,"jako swoją liczbę")
    Lista1.remove(a)
    Lista2 = list(Lista)
    b = random.choice(Lista2)
    print("Bot 2 wybrał liczbę ",b ,"jako swoją liczbę")
    Lista2.remove(b)
    i = 0
    while a in Lista and b in Lista:
        if i%2 == 0:
            c = random.choice(Lista1)
            print("Bot 1 wybrał liczbe ",c)
            Lista1 = [i for i in Lista1 if i not in dzielniki(c)]
            Lista2 = [i for i in Lista2 if i not in dzielniki(c)]
            for j in dzielniki(c):
                Lista[j-1] = 'x'
            i = i+1
            mlista = [Lista[j:j + 10] for j in range(0, len(Lista), 10)]
            for l in mlista:
                print(l)
        else:
            c = random.choice(Lista2)
            print("Bot 2 wybrał liczbe ", c)
            Lista1 = [i for i in Lista1 if i not in dzielniki(c)]
            Lista2 = [i for i in Lista2 if i not in dzielniki(c)]
            for j in dzielniki(c):
                Lista[j - 1] = 'x'
            i = i + 1
            mlista = [Lista[j:j + 10] for j in range(0, len(Lista), 10)]
            for l in mlista:
                print(l)
    if a in Lista:
        print("Bot 1 wygrał, jego liczba to ",a)
    else:
        print("Bot 2 wygrał, jego liczba to ",b)




else:
    print("Proszę wybrać 1, 2 lub 3")
    exit()

    #Dodaj różne strategie dla botów.
