# # 2) Создайте программу для игры в ""Крестики-нолики"".
#
#
# Она не работает. Баг на баге.
# код Аи Компьютера, не правильно работает. До изменения, ходы выполнялись правильно.
# Все условия обрабатываются. Но не правильно. Визуально победил первый игрок, победил другой.
# Код не разборчивый. Не понятный. С проблемами в коде.
# С каждым изменением кода, есть большая вероятность повредить код. Не стал трогать.
# Код хранится в комментарии. К плачевному состоянию, код не будет улучшаться.
#
# Название Tic Tac Toe Крестики Нолики
#
# from random import randint
#
# def IfWinHodGrid(grid3,ticTacToe):
#     global players, i
#     if grid3[0] == ticTacToe[i] and grid3[1] == ticTacToe[i] and grid3[2] == ticTacToe[i] or \
#        grid3[3] == ticTacToe[i] and grid3[4] == ticTacToe[i] and grid3[5] == ticTacToe[i] or \
#        grid3[6] == ticTacToe[i] and grid3[7] == ticTacToe[i] and grid3[8] == ticTacToe[i] or \
#        grid3[0] == ticTacToe[i] and grid3[3] == ticTacToe[i] and grid3[6] == ticTacToe[i] or \
#        grid3[1] == ticTacToe[i] and grid3[4] == ticTacToe[i] and grid3[7] == ticTacToe[i] or \
#        grid3[2] == ticTacToe[i] and grid3[5] == ticTacToe[i] and grid3[8] == ticTacToe[i] or \
#        grid3[0] == ticTacToe[i] and grid3[4] == ticTacToe[i] and grid3[8] == ticTacToe[i] or \
#        grid3[2] == ticTacToe[i] and grid3[4] == ticTacToe[i] and grid3[6] == ticTacToe[i]:
#         print(f"Win {players[i]}")
#         return i
#     else:
#         return ""
#
# def ShowGrid():
#     for i in range(1,len(grid3)):
#         print("|", end="")
#         print(grid3[i],end="")
#         print("|",end="")
#         if i % 3 == 0: print()
#
#
#
#
# grid3 = [f"{i}" for i in range(0,10)]
# players = ['Крестик','Нолик']
# ticTacToe = ["X","O"]
# hods = [i for i in range(len(players))]
#
# def ControlPlayers(i):
#     global isWin
#     if i == 0:
#         while (not isWin):
#             try:
#                 while (not isWin):
#                     print(f"Ваш ход: {players[0]}.")
#                     inputHod = int(input("Введите число:"))
#                     if not grid3[inputHod] in ticTacToe:
#                         grid3[inputHod] = ticTacToe[0]
#                         if IsWinner():
#                             isWin = True
#                             return 0
#                         break
#                     else:
#                         print(
#                             f"Вы не можете поставить {ticTacToe[0]} на клетку, она занята. Пожалуйста выберите другую.")
#                 break
#             except:
#                 pass
#     elif i == 1:
#         print(f"Ход компьютера: {players[1]}.")
#         while (not isWin):
#             try:
#                 inputHod = int(grid3[randint(0, len(grid3))])
#                 if not grid3[inputHod] in ticTacToe:
#                     grid3[inputHod] = ticTacToe[1]
#                     if IsWinner():
#                         isWin = True
#                         return 1
#                     break
#                 else:
#                     print(f"Вы не можете поставить {ticTacToe[1]} на клетку, она занята. Пожалуйста выберите другую.")
#             except:
#                 pass
#
# def IsWinner():
#     global i
#     if type(IfWinHodGrid(grid3,ticTacToe)) == int:
#         print(f"Победитель! {players[i]}")
#         return True
# isWin = False
# i = 0
# while(not isWin):
#     ShowGrid()
#     print()
#     ControlPlayers(i)
#
#     if i == 0:
#         i = 1
#     else:
#         i = 0
#
#
# IsWinner()
#
