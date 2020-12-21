r = 0
for i in range(r):
    print(r)
ran = len(self.b_move_attack)
for i in range(ran):
    classes = len((self.b_move_attack[i]))
    for c in range(classes):
        ran2 = len((self.b_move_attack[i][c][1]))
        ran3 = len((self.b_move_attack[i][c][2]))
        for a in range(ran2):
            # moves
            point = 0
            move = (self.b_move_attack[i][c][1][a])
            if move[1] == 4:
                print("dw")
            self.b_move_attack[i][c][1][a].append(point)
        for b in range(ran3):
            # attacks
            point = 0
            attack = self.b_move_attack[i][c][2][b]
            if self.board[int(attack[0])][int(attack[1])].type1 == "pawnw":
                point += 2
            if self.board[int(attack[0])][int(attack[1])].type1 == "rookw":
                point += 5
            if self.board[int(attack[0])][int(attack[1])].type1 == "bishopw":
                point += 5
            if self.board[int(attack[0])][int(attack[1])].type1 == "queenw":
                point += 13
            if self.board[int(attack[0])][int(attack[1])].type1 == "kingw":
                point += 99999999999999999999999999999999999999999999
            self.b_move_attack[i][c][2][b].append(point)