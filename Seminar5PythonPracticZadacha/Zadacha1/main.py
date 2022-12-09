#
# 1) Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# 2021 21 ---> 2000 бот4 -> 1996 .... бот --->29 --> 27 >> 2конф


from random import randint

def InputInt():
    while(True):
        try:
            return int(input("Введите целочисленное значение: "))
        except:
            print("Ошибка.")

def SaveStats():
    global save_numberOfCandies, save_takeMaximumCandy, save_players, save_count
    save_numberOfCandies = 120 # *40
    save_takeMaximumCandy = 28 # *10
    save_players = 2 # 4
    save_count = 0
    # save_players = [0 for i in range(save_players)]
    # save_players[-1] = 3
    # save_players[0] = 0
    # save_players = players

def StartStats():
    global numberOfCandies, takeMaximumCandy, players, count
    numberOfCandies = save_numberOfCandies
    takeMaximumCandy = save_takeMaximumCandy
    count = save_count
    players = save_players
    players = [randint(2,5) for i in range(players)]
    # players[-1] = 3
    players[0] = 1

def Statistics():
    global numberOfCandies, turns
    print(f"Ход {'игрока' if players[turns] in [0,1] else 'компьютера'}: {turns+1}. Колличество конфет: {numberOfCandies}.",end=" ")

def InputPlayers(player):
    global n, numberOfCandies, takeMaximumCandy, count, turns

    if players[player] == 0:
        n = InputInt()

    elif players[player] == 1:
        if count == 0:
            if numberOfCandies // takeMaximumCandy > takeMaximumCandy:
                print(f"Введите значение: {takeMaximumCandy}")
            elif numberOfCandies // takeMaximumCandy <= takeMaximumCandy:
                print(f"Введите значение: {numberOfCandies // takeMaximumCandy}")
        else:
            print(f"Введите значение: {takeMaximumCandy+1-nCandy}")
        n = InputInt()

    elif players[player] == 2:
        n = randint(1,min(takeMaximumCandy,numberOfCandies))

    elif players[player] == 3:
        if numberOfCandies <= takeMaximumCandy:
            n = numberOfCandies
        else:
            n = randint(1,min(takeMaximumCandy,numberOfCandies))

    elif players[player] == 4:
        if numberOfCandies <= takeMaximumCandy:
            n = numberOfCandies
        else:
            if count == 0:
                if numberOfCandies//takeMaximumCandy > takeMaximumCandy:
                    n = takeMaximumCandy
                elif numberOfCandies // takeMaximumCandy <= takeMaximumCandy:
                    n = numberOfCandies // takeMaximumCandy
                else:
                    n = randint(1,min(takeMaximumCandy,numberOfCandies))

            else:
                n = takeMaximumCandy+1-nCandy



    elif players[player] == 5:
        if numberOfCandies <= takeMaximumCandy:
            n = numberOfCandies
        else:
            if count == 0:
                if numberOfCandies // takeMaximumCandy > takeMaximumCandy:
                    n = takeMaximumCandy
                elif numberOfCandies // takeMaximumCandy <= takeMaximumCandy:
                    n = numberOfCandies // takeMaximumCandy
                else:
                    n = randint(1, min(takeMaximumCandy, numberOfCandies))

            else:
                if takeMaximumCandy * 2 > numberOfCandies:
                    n = min(takeMaximumCandy,numberOfCandies) + 1 - nCandy
                else:
                    n = takeMaximumCandy + 1 - nCandy



    else:
        n = randint(1, min(takeMaximumCandy, numberOfCandies))


def GetCandy(player):
    global numberOfCandies, takeMaximumCandy, n, nCandy
    InputPlayers(player)
    while(True):
        if 0 < n <= takeMaximumCandy:
            if n <= numberOfCandies:
                numberOfCandies -= n
                print(f"{'Игрок' if players[player] in [0,1] else 'Компьютер'} {turns+1}, взял конфет: {n}." if n > 0 else "")
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
        print(f"{'Игрок' if players[player] in [0,1] else 'Компьютер'} {turns + 1} победитель!")
    # print(nCandy)

def GamePlayRunCode():
    global turns, count
    StartStats()
    turns = 0
    while(numberOfCandies > 0):
        # print(f"Ход {turns+1} игрока.")
        Statistics()
        PlayerTurns(turns)
        if not gameRandomTurns:
            if len(players)-1>turns: turns += 1
            else: turns = 0
        else:
            turns = randint(0,len(players)-1)
        count += 1
        print(end="\n"*1)

def EditRunCode():
    global gameRandomTurns, save_numberOfCandies, save_takeMaximumCandy, save_players, save_count
    while (True):
        print(end="\n" * 1)
        inputStr = input(f"gameRandomTurns or garatu = {gameRandomTurns}"
                         f"\nnumberOfCandies  or noc = {save_numberOfCandies}"
                         f"\ntakeMaximumCandy  or tmc = {save_takeMaximumCandy}"
                         f"\nplayers or pl = {save_players}"
                         f"\nExit > q\nInput: ")
        try:
            if inputStr == "q":
                break
            elif inputStr.split(" ")[0].lower() in ["gamerandomturns","garatu"] and inputStr.split(" ")[1].lower() in ["true","false","0","1"]:
                gameRandomTurns = bool(inputStr.split(" ")[1])

            elif inputStr.split(" ")[0].lower() in ["numberofcandies","noc"] and type(int(inputStr.split(" ")[1].lower()) == int):
                save_numberOfCandies = int(inputStr.split(" ")[1])

            elif inputStr.split(" ")[0].lower() in ["takemaximumcandy","tmc"] and type(int(inputStr.split(" ")[1].lower()) == int):
                save_takeMaximumCandy = int(inputStr.split(" ")[1])

            elif inputStr.split(" ")[0].lower() in ["players","pl"] and type(int(inputStr.split(" ")[1].lower()) == int):
                save_players = int(inputStr.split(" ")[1])

        except:
            pass

def StartGame():
    global gameRandomTurns
    gameRandomTurns = False
    print("Start Game")
    SaveStats() # Сохранёные параметры, статистики, настройки
    while(True):
        print(end="\n"*1)
        inputStr = input("Start > Enter\nEdit > edit\nExit > q\nInput: ")
        if inputStr == "q":
            break
        elif inputStr == "":
            GamePlayRunCode()
            print(end="\n" * 2)
        elif inputStr == "edit":
            EditRunCode()
            print(end="\n" * 2)

StartGame()
