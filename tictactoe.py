# This is a game of tic tac toe.
# x | o | x
# x | o | x
# x | x | o
# x is the winner
player_1 = input("Player One, what is your name?: ")
player_2 = input("Player Two, what is your name? ")

player_1_xter = input("{player_1}, you go first. Choose between 'x' and 'o': ".format(player_1=player_1))

while player_1_xter not in ["x", "o"]:
    print ("You must pick one between 'x' and 'o' only.")
    player_1_xter = input("Choose one between 'x' and 'o': ")

if player_1_xter.lower() == "x":
    player_2_xter = "o"
    print("{player_2}, you go next. 'x' has been taken. Your player character is 'o'".format(player_2 = player_2))
else:
    player_2_xter = "x"
    print("{player_2}, you go next. 'o' has been taken. Your player character is 'x'".format(player_2=player_2))

# Game time
print("It's game time!! Are you ready???")

row_1 = [1,2,3]
row_2 = [4,5,6]
row_3 = [7,8,9]

available_slots = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

#Player 1 - play 1
player_1_position_1 = input("""{player_1}, your turn! Choose a position for your first play between positions 1 to 9: 
                                                 1 | 2 | 3
                                                 4 | 5 | 6
                                                 7 | 8 | 9
                            : """.format(player_1 = player_1))

while player_1_position_1 not in available_slots:
    player_1_position_1 = input("Choose a number between {available_slots}: ".format(available_slots = available_slots))

available_slots.remove(str(player_1_position_1))
# print(available_slots)    


if int(player_1_position_1) in row_1:
    index = row_1.index(int(player_1_position_1))
    row_1[index] = player_1_xter
elif int(player_1_position_1) in row_2:
    index = row_2.index(int(player_1_position_1))
    row_2[index] = player_1_xter
else:
    index = row_3.index(int(player_1_position_1))
    row_3[index] = player_1_xter

    
game_board = """                                                {a} | {b} | {c} 
                                                {d} | {e} | {f} 
                                                {g} | {h} | {i}
                """.format(a=row_1[0], b = row_1[1], c = row_1[2], d = row_2[0], e = row_2[1], f = row_2[2], g = row_3[0], h = row_3[1], i = row_3[2])

# print(game_board)

#Player 2 - play 1
player_2_position_1 = input("""{player_2}, Your turn! Choose a position for your first play between {available_slots}
{game_board}
                            : """.format(player_2 = player_2, available_slots = available_slots, game_board=game_board, nothing = " "))

while player_2_position_1 not in available_slots:
    player_2_position_1 = input("Choose a number between {available_slots}: ".format(available_slots = available_slots))

available_slots.remove(str(player_2_position_1))
# print(available_slots)   

if int(player_2_position_1) in row_1:
    index = row_1.index(int(player_2_position_1))
    row_1[index] = player_2_xter
elif int(player_2_position_1) in row_2:
    index = row_2.index(int(player_2_position_1))
    row_2[index] = player_2_xter
else:
    index = row_3.index(int(player_2_position_1))
    row_3[index] = player_2_xter

game_board = """                                                {a} | {b} | {c} 
                                                {d} | {e} | {f} 
                                                {g} | {h} | {i}
                """.format(a=row_1[0], b = row_1[1], c = row_1[2], d = row_2[0], e = row_2[1], f = row_2[2], g = row_3[0], h = row_3[1], i = row_3[2])

# print(game_board)

#Player 1 - play 2
player_1_position_2 = input("""{player_1}, your turn! Choose a position for your second play between {available_slots}
{game_board}
                            : """.format(player_1 = player_1, available_slots = available_slots, game_board = game_board))

while player_1_position_2 not in available_slots:
    player_1_position_2 = input("Choose a number between {available_slots}: ".format(available_slots = available_slots))

available_slots.remove(str(player_1_position_2))
# print(available_slots)    


if int(player_1_position_2) in row_1:
    index = row_1.index(int(player_1_position_2))
    row_1[index] = player_1_xter
elif int(player_1_position_2) in row_2:
    index = row_2.index(int(player_1_position_2))
    row_2[index] = player_1_xter
else:
    index = row_3.index(int(player_1_position_2))
    row_3[index] = player_1_xter


game_board = """                                                {a} | {b} | {c} 
                                                {d} | {e} | {f} 
                                                {g} | {h} | {i}
                """.format(a=row_1[0], b = row_1[1], c = row_1[2], d = row_2[0], e = row_2[1], f = row_2[2], g = row_3[0], h = row_3[1], i = row_3[2])

# print(game_board)

#Player 2 - play 2
player_2_position_2 = input("""{player_2}, Your turn! Choose a position for your second play between {available_slots}
{game_board} 
                            : """.format(player_2 = player_2, available_slots = available_slots, game_board = game_board))

while player_2_position_2 not in available_slots:
    player_2_position_2 = input("Choose a number between {available_slots}: ".format(available_slots = available_slots))

available_slots.remove(str(player_2_position_2))
# print(available_slots)   

if int(player_2_position_2) in row_1:
    index = row_1.index(int(player_2_position_2))
    row_1[index] = player_2_xter
elif int(player_2_position_2) in row_2:
    index = row_2.index(int(player_2_position_2))
    row_2[index] = player_2_xter
else:
    index = row_3.index(int(player_2_position_2))
    row_3[index] = player_2_xter

game_board = """                                                {a} | {b} | {c} 
                                                {d} | {e} | {f} 
                                                {g} | {h} | {i}
                """.format(a=row_1[0], b = row_1[1], c = row_1[2], d = row_2[0], e = row_2[1], f = row_2[2], g = row_3[0], h = row_3[1], i = row_3[2])

# print(game_board)

#Player 1 - play 3
player_1_position_3 = input("""{player_1}, your turn! Choose a position for your third play between {available_slots}: 
{game_board}
                            : """.format(player_1 = player_1, available_slots = available_slots, game_board = game_board))

while player_1_position_3 not in available_slots:
    player_1_position_3 = input("Choose a number between {available_slots}: ".format(available_slots = available_slots))

available_slots.remove(str(player_1_position_3))
# print(available_slots)    


if int(player_1_position_3) in row_1:
    index = row_1.index(int(player_1_position_3))
    row_1[index] = player_1_xter
elif int(player_1_position_3) in row_2:
    index = row_2.index(int(player_1_position_3))
    row_2[index] = player_1_xter
else:
    index = row_3.index(int(player_1_position_3))
    row_3[index] = player_1_xter


game_board = """                                                {a} | {b} | {c} 
                                                {d} | {e} | {f} 
                                                {g} | {h} | {i}
                """.format(a=row_1[0], b = row_1[1], c = row_1[2], d = row_2[0], e = row_2[1], f = row_2[2], g = row_3[0], h = row_3[1], i = row_3[2])

# print(game_board)

#Player 2 - play 3
player_2_position_3 = input("""{player_2}, Your turn! Choose a position for your third play between {available_slots}
{game_board}
                            : """.format(player_2 = player_2, available_slots = available_slots, game_board = game_board))

while player_2_position_3 not in available_slots:
    player_2_position_3 = input("Choose a number between {available_slots}: ".format(available_slots = available_slots))

available_slots.remove(str(player_2_position_3))
# print(available_slots)   

if int(player_2_position_3) in row_1:
    index = row_1.index(int(player_2_position_3))
    row_1[index] = player_2_xter
elif int(player_2_position_3) in row_2:
    index = row_2.index(int(player_2_position_3))
    row_2[index] = player_2_xter
else:
    index = row_3.index(int(player_2_position_3))
    row_3[index] = player_2_xter

game_board = """                                                {a} | {b} | {c} 
                                                {d} | {e} | {f} 
                                                {g} | {h} | {i}
                """.format(a=row_1[0], b = row_1[1], c = row_1[2], d = row_2[0], e = row_2[1], f = row_2[2], g = row_3[0], h = row_3[1], i = row_3[2])

# print(game_board)

#Player 1 - play 4
player_1_position_4 = input("""{player_1}, your turn! Choose a position for your fourth play between {available_slots}: 
{game_board}
                            : """.format(player_1 = player_1, available_slots = available_slots, game_board = game_board))

while player_1_position_4 not in available_slots:
    player_1_position_4 = input("Choose a number between {available_slots}: ".format(available_slots = available_slots))

available_slots.remove(str(player_1_position_4))
# print(available_slots)    


if int(player_1_position_4) in row_1:
    index = row_1.index(int(player_1_position_4))
    row_1[index] = player_1_xter
elif int(player_1_position_4) in row_2:
    index = row_2.index(int(player_1_position_4))
    row_2[index] = player_1_xter
else:
    index = row_3.index(int(player_1_position_4))
    row_3[index] = player_1_xter


game_board = """                                                {a} | {b} | {c} 
                                                {d} | {e} | {f} 
                                                {g} | {h} | {i}
                """.format(a=row_1[0], b = row_1[1], c = row_1[2], d = row_2[0], e = row_2[1], f = row_2[2], g = row_3[0], h = row_3[1], i = row_3[2])

# print(game_board)

#Player 2 - play 4
player_2_position_4 = input("""{player_2}, Your turn! Choose a position for your final play between {available_slots}
{game_board}
                            : """.format(player_2 = player_2, available_slots = available_slots, game_board = game_board))

while player_2_position_4 not in available_slots:
    player_2_position_4 = input("Choose a number between {available_slots}: ".format(available_slots = available_slots))

available_slots.remove(str(player_2_position_4))
# print(available_slots)   

if int(player_2_position_4) in row_1:
    index = row_1.index(int(player_2_position_4))
    row_1[index] = player_2_xter
elif int(player_2_position_4) in row_2:
    index = row_2.index(int(player_2_position_4))
    row_2[index] = player_2_xter
else:
    index = row_3.index(int(player_2_position_4))
    row_3[index] = player_2_xter

game_board = """                                                {a} | {b} | {c} 
                                                {d} | {e} | {f} 
                                                {g} | {h} | {i}
                """.format(a=row_1[0], b = row_1[1], c = row_1[2], d = row_2[0], e = row_2[1], f = row_2[2], g = row_3[0], h = row_3[1], i = row_3[2])

# print(game_board)

#Player 1 - play 5
player_1_position_5 = input("""{player_1}, your turn! Choose a position for your final play between {available_slots}: 
{game_board}
                            : """.format(player_1 = player_1, available_slots = available_slots, game_board = game_board))

while player_1_position_5 not in available_slots:
    player_1_position_5 = input("Choose a number between {available_slots}: ".format(available_slots = available_slots))

available_slots.remove(str(player_1_position_5))
# print(available_slots)    


if int(player_1_position_5) in row_1:
    index = row_1.index(int(player_1_position_5))
    row_1[index] = player_1_xter
elif int(player_1_position_5) in row_2:
    index = row_2.index(int(player_1_position_5))
    row_2[index] = player_1_xter
else:
    index = row_3.index(int(player_1_position_5))
    row_3[index] = player_1_xter


game_board = """                                                {a} | {b} | {c} 
                                                {d} | {e} | {f} 
                                                {g} | {h} | {i}
                """.format(a=row_1[0], b = row_1[1], c = row_1[2], d = row_2[0], e = row_2[1], f = row_2[2], g = row_3[0], h = row_3[1], i = row_3[2])

# print(game_board)

player_1_positions = [player_1_position_1, player_1_position_2,player_1_position_3,player_1_position_4,player_1_position_5]
player_2_positions = [player_2_position_1, player_2_position_2, player_2_position_3, player_2_position_4]

#Top row horizontal win
if row_1[0] == row_1[1] and row_1[1] == row_1[2]:
    if row_1[0] == player_1_xter:
        print("And the winer is... Player 1! Congratualtions, {player_1}!!!".format(player_1 = player_1))
    else:
        print("And the winer is... Player 2! Congratualtions, {player_2}!!!".format(player_2 = player_2))
#Middle row horizontal win
elif row_2[0] == row_2[1] and row_2[1] == row_2[2]:
    if row_2[0] == player_1_xter:
         print("And the winer is... Player 1! Congratualtions, {player_1}!!!".format(player_1 = player_1))
    else:
         print("And the winer is... Player 2! Congratualtions, {player_2}!!!".format(player_2 = player_2))
#Third row horizontal win
elif row_3[0] == row_3[1] and row_3[1] == row_3[2]:
    if row_3[0] == player_1_xter:
        print("And the winer is... Player 1! Congratualtions, {player_1}!!!".format(player_1 = player_1))
    else:
         print("And the winer is... Player 2! Congratualtions, {player_2}!!!".format(player_2 = player_2))
#First column vertical win
elif row_1[0] == row_2[0] and row_2[0] == row_3[0]:
    if row_1[0] == player_1_xter:
        print("And the winer is... Player 1! Congratualtions, {player_1}!!!".format(player_1 = player_1))
    else:
         print("And the winer is... Player 2! Congratualtions, {player_2}!!!".format(player_2 = player_2))
#Second column vertical win
elif row_1[1] == row_2[1] and row_2[1] == row_3[1]:
    if row_1[1] == player_1_xter:
        print("And the winer is... Player 1! Congratualtions, {player_1}!!!".format(player_1 = player_1))
    else:
         print("And the winer is... Player 2! Congratualtions, {player_2}!!!".format(player_2 = player_2))
#Third column vertical win
elif row_1[2] == row_2[2] and row_2[2] == row_3[2]:
    if row_1[2] == player_1_xter:
        print("And the winer is... Player 1! Congratualtions, {player_1}!!!".format(player_1 = player_1))
    else:
         print("And the winer is... Player 2! Congratualtions, {player_2}!!!".format(player_2 = player_2))
#left-top to right-bottom diagonal win
elif row_1[0] == row_2[1] and row_2[1] == row_3[2]:
    if row_1[0] == player_1_xter:
        print("And the winer is... Player 1! Congratualtions, {player_1}!!!".format(player_1 = player_1))
    else:
         print("And the winer is... Player 2! Congratualtions, {player_2}!!!".format(player_2 = player_2))
#right-top to left-bottom diagonal win
elif row_1[2] == row_2[1] and row_2[1] == row_3[0]:
    if row_1[2] == player_1_xter:
        print("And the winer is... Player 1! Congratualtions, {player_1}!!!".format(player_1 = player_1))
    else:
         print("And the winer is... Player 2! Congratualtions, {player_2}!!!".format(player_2 = player_2))
#A draw!
else:
    print("This was a tough match. You both win! Congratulations {player_1} and {player_2}!!".format(player_1=player_1, player_2=player_2))