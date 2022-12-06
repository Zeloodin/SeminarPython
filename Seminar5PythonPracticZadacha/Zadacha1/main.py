
# 1) Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# 2021 21 ---> 2000 бот4 -> 1996 .... бот --->29 --> 27 >> 2конф

# 4
# 29
# 28
# playe1 = 30
# 120 = 4 == 29

from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')




from random import randint

def InputInt():
    while(True):
        try:
            return int(input("Введите целочисленное значение: "))
        except:
            print("Ошибка.")

def SaveStats():
    global save_numberOfCandies, save_takeMaximumCandy, save_players, numberOfCandies, takeMaximumCandy, players
    save_numberOfCandies = 120
    save_takeMaximumCandy = 28
    save_players = 2
    # save_players = [0 for i in range(save_players)]
    # save_players[-1] = 3
    # save_players[0] = 0
    # save_players = players

def StartStats():
    global numberOfCandies, takeMaximumCandy, players
    numberOfCandies = save_numberOfCandies
    takeMaximumCandy = save_takeMaximumCandy
    players = save_players
    players = [0 for i in range(players)]
    players[-1] = 3
    players[0] = 0

def Statistics():
    global numberOfCandies, turns
    print(f"Колличество конфет: {numberOfCandies}. Ход {turns+1} {'игрока' if players[turns] == 0 else 'компьютера'}.")

def InputPlayers(player):
    global n, numberOfCandies, takeMaximumCandy
    if players[player] == 1:
        n = randint(1,min(takeMaximumCandy,numberOfCandies))

    elif players[player] == 2:
        if numberOfCandies <= takeMaximumCandy:
            n = numberOfCandies
        else:
            n = randint(1,min(takeMaximumCandy,numberOfCandies))

    elif players[player] == 3:
        if numberOfCandies <= takeMaximumCandy:
            n = numberOfCandies
        else:
            n = takeMaximumCandy+1-nCandy

    else:
        n = InputInt()

def GetCandy(player):
    global numberOfCandies, takeMaximumCandy, n, nCandy
    InputPlayers(player)
    while(True):
        if 0 < n <= takeMaximumCandy:
            if n <= numberOfCandies:
                numberOfCandies -= n
                print(f"Взял конфет:{n}. {turns+1} {'игрок' if players[player] == 0 else 'компьютер'}." if n > 0 else "")
                nCandy = n
                return n
            else:
                print(f"Взяли {n}, оно больше чем {numberOfCandies}. {numberOfCandies}-{n}={numberOfCandies-n}<0. Повторите ход.")
                InputPlayers(player)
        else:
            if 0 >= n:
                print(f"Невозможно брать в колличестве 0 конфет и ниже. Повторите ход.")
                InputPlayers(player)
            elif n > takeMaximumCandy:
                print(f"За ход, брать не больше {takeMaximumCandy}, взяли {n}. Повторите ход.")
                InputPlayers(player)

def PlayerTurns(player):
    global players, nCandy
    GetCandy(player)
    if numberOfCandies <= 0:
        print(f"{'Игрок' if players[player] == 0 else 'Компьютер'} {turns + 1} победитель!")
    # print(nCandy)

def GamePlayRunCode():
    StartStats()
    global turns
    turns = 0
    while(numberOfCandies > 0):
        # print(f"Ход {turns+1} игрока.")
        Statistics()
        PlayerTurns(turns)

        if len(players)-1>turns: turns += 1
        else: turns = 0


SaveStats()
while(True):
    GamePlayRunCode()
    if input() == "q":
        break