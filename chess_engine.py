import re


class Chess:
    def __init__(self):
        self.board = [
            ['black_rook', 'black_knight', 'black_bishop', 'black_queen', 'black_king', 'black_bishop', 'black_knight',
             'black_rook'],
            ['black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn',
             'black_pawn'], ['_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_',
                                                       '_'],
            ['white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn',
             'white_pawn'],
            ['white_rook', 'white_knight', 'white_bishop', 'white_queen', 'white_king', 'white_bishop', 'white_knight',
             'white_rook']]
        self.move = self.make_move

    def has_moved(self, before_row, before_col):
        if self.board[before_row][before_col] == 'white_pawn':
            if before_row == 6:
                return False
        if self.board[before_row][before_col] == 'black_pawn':
            if before_row == 1:
                return False
        if 'king' in self.board[before_row][before_col]:
            if ((before_row == (0 or 7)) and (before_col == 4)):
                return False
        if 'rook' in self.board[before_row][before_col]:
            if ((before_row == (0 or 7)) and (before_col == (0 or 7))):
                return False
        return False

    def is_available_move(self, before_row, before_col, after_row, after_col):
        pass_variable = 0  # variable created to ontinue the code with the except
        col_available_move = []
        row_available_move = []
        piece = self.board[before_row][before_col]
        if 'pawn' in piece:  # PAWN
            if piece == 'black_pawn':
                if self.has_moved(before_row, before_col) is True:
                    try:
                        if self.board[before_row + 1][before_col] == '_':
                            row_available_move.append(before_row + 1)
                            col_available_move.append(before_col)
                    except:
                        pass_variable = 5
                else:  # here we dont do try and except cuz this means that pawn hasnt moved yet
                    if self.board[before_row + 1][before_col] == '_':
                        row_available_move.append(before_row + 1)
                        col_available_move.append(before_col)
                    if self.board[before_row + 2][before_col] == '_':
                        row_available_move.append(before_row + 2)
                        col_available_move.append(before_col)
                try:
                    if self.board[before_row + 1][before_col + 1] != '_':  # taking
                        row_available_move.append(before_row + 1)
                        col_available_move.append(before_col + 1)
                except:
                    pass_variable = 5
                try:
                    if self.board[before_row + 1][before_col - 1] != '_':
                        row_available_move.append(before_row + 1)
                        col_available_move.append(before_col - 1)
                except:
                    pass_variable = 5
            if piece == 'white_pawn':
                if self.has_moved(before_row, before_col) is True:
                    try:
                        if self.board[before_row - 1][before_col] == '_':
                            row_available_move.append(before_row - 1)
                            col_available_move.append(before_col)
                    except:
                        pass_variable = 5
                else:  # here we dont try except
                    if self.board[before_row - 1][before_col] == '_':
                        row_available_move.append(before_row - 1)
                        col_available_move.append(before_col)
                    if self.board[before_row - 2][before_col] == '_':
                        row_available_move.append(before_row - 2)
                        col_available_move.append(before_col)
                try:
                    if self.board[before_row - 1][before_col - 1] != '_':
                        row_available_move.append(before_row - 1)
                        col_available_move.append(before_col - 1)
                except:
                    pass_variable = 5
                try:
                    if self.board[before_row - 1][before_col + 1] != '_':
                        row_available_move.append(before_row - 1)
                        col_available_move.append(before_col + 1)
                except:
                    pass_variable = 5
        if 'king' in piece:  # KING
            for r in range(-1, 2):
                for c in range(-1, 2):
                    try:
                        col_available_move.append(before_col + c)
                        row_available_move.append(before_row + r)
                    except:
                        continue
        if 'rook' in piece:  # ROOK
            for r in range(1, 9):
                try:
                    if self.board[before_row + r][before_col] != '_':
                        row_available_move.append(before_row + r)
                        col_available_move.append(before_col)
                        break
                    row_available_move.append(before_row + r)
                    col_available_move.append(before_col)
                except:
                    pass_variable = 11
            for r in range(1, 9):
                try:
                    if self.board[before_row - r][before_col] != '_':
                        row_available_move.append(before_row - r)
                        col_available_move.append(before_col)
                        break
                    row_available_move.append(before_row - r)
                    col_available_move.append(before_col)
                except:
                    pass_variable = 1
            for c in range(1, 9):
                try:
                    if self.board[before_row][before_col + c] != '_':
                        col_available_move.append(before_col + c)
                        row_available_move.append(before_row)
                        break
                    col_available_move.append(before_col + c)
                    row_available_move.append(before_row)
                except:
                    pass_variable = 0
            for c in range(1, 9):
                try:
                    if self.board[before_row][before_col - c] != '_':
                        col_available_move.append(before_col - c)
                        row_available_move.append(before_row)
                        break
                    col_available_move.append(before_col - c)
                    row_available_move.append(before_row)
                except:
                    pass_variable = 1
        if 'bishop' in piece:  # BISHOP
            for r in range(-1, 2, 1):
                for c in range(-1, 2, 1):
                    try:
                        col_available_move.append(before_col + c)
                        row_available_move.append(before_row + r)
                    except:
                        pass_variable = 5
                    try:
                        if (c < 0) and (r < 0) and (self.board[before_row - 1][before_col - 1] == '_'):
                            for i in range(7):
                                if self.board[before_row + r - i][before_col + c - i] != '_':
                                    col_available_move.append(before_col + c - i)
                                    row_available_move.append(before_row + r - i)
                                    break
                                elif self.board[before_row + r - i][before_col + c - i] == '_':
                                    col_available_move.append(before_col + c - i)
                                    row_available_move.append(before_row + r - i)
                    except:
                        pass_variable = 5
                    try:
                        if (c < 0) and (r > 0) and (self.board[before_row + 1][before_col - 1] == '_'):
                            for i in range(7):
                                if self.board[before_row + r + i][before_col + c - i] != '_':
                                    col_available_move.append(before_col + c - i)
                                    row_available_move.append(before_row + r + i)
                                    break
                                elif self.board[before_row + r + i][before_col + c - i] == '_':
                                    col_available_move.append(before_col + c - i)
                                    row_available_move.append(before_row + r + i)
                    except:
                        pass_variable = 5
                    try:
                        if (c > 0) and (r > 0) and (self.board[before_row + 1][before_col + 1] == '_'):
                            for i in range(7):
                                if self.board[before_row + r + i][before_col + c + i] != '_':
                                    col_available_move.append(before_col + c + i)
                                    row_available_move.append(before_row + r + i)
                                    break
                                elif self.board[before_row + r + i][before_col + c + i] == '_':
                                    col_available_move.append(before_col + c + i)
                                    row_available_move.append(before_row + r + i)
                    except:
                        pass_variable = 5
                    try:
                        if (c > 0) and (r < 0) and (self.board[before_row - 1][before_col + 1] == '_'):
                            for i in range(7):
                                if self.board[before_row + r - i][before_col + c + i] != '_':
                                    col_available_move.append(before_col + c + i)
                                    row_available_move.append(before_row + r - i)
                                    break
                                elif self.board[before_row + r - i][before_col + c + i] == '_':
                                    col_available_move.append(before_col + c + i)
                                    row_available_move.append(before_row + r - i)
                    except:
                        pass_variable = 5
        if 'knight' in piece:  # KNIGHT
            try:
                self.board[before_row+1][before_col+2] = self.board[before_row+1][before_col+3]
                col_available_move.append(before_col + 2)  # la right or left
                row_available_move.append(before_row + 1)
            except:
                pass_variable = 2
            try:
                self.board[before_row - 1][before_col + 2] = self.board[before_row - 1][before_col + 3]
                col_available_move.append(before_col + 2)
                row_available_move.append(before_row - 1)
            except:
                pass_variable = 3
            try:
                self.board[before_row + 1][before_col - 2] = self.board[before_row + 1][before_col - 3]
                col_available_move.append(before_col - 2)
                row_available_move.append(before_row + 1)
            except:
                pass_variable = 4
            try:
                self.board[before_row - 1][before_col - 2] = self.board[before_row - 1][before_col - 3]
                col_available_move.append(before_col - 2)
                row_available_move.append(before_row - 1)
            except:
                pass_variable = 5
                # la fo2 w ta7et
            try:
                self.board[before_row + 2][before_col + 1] = self.board[before_row + 3][before_col + 1]
                col_available_move.append(before_col + 1)
                row_available_move.append(before_row + 2)
            except:
                pass_variable = 5
            try:
                self.board[before_row + 2][before_col - 1] = self.board[before_row + 3][before_col - 1]
                col_available_move.append(before_col - 1)
                row_available_move.append(before_row + 2)
            except:
                pass_variable = 5
            try:
                self.board[before_row - 2][before_col + 1] = self.board[before_row - 3][before_col + 1]
                col_available_move.append(before_col + 1)
                row_available_move.append(before_row - 2)
            except:
                pass_variable = 5
            try:
                self.board[before_row - 2][before_col - 1] = self.board[before_row - 3][before_col - 1]
                col_available_move.append(before_col - 1)
                row_available_move.append(before_row - 2)
            except:
                pass_variable = 5
        if 'queen' in piece:  # QUEEN IS COMBINATION ROOK AND BISHOP
            for r in range(1, 9):
                try:
                    if self.board[before_row + r][before_col] != '_':
                        row_available_move.append(before_row + r)
                        col_available_move.append(before_col)
                        break
                    row_available_move.append(before_row + r)
                    col_available_move.append(before_col)
                except:
                    pass_variable = 11
            for r in range(1, 9):
                try:
                    if self.board[before_row - r][before_col] != '_':
                        row_available_move.append(before_row - r)
                        col_available_move.append(before_col)
                        break
                    row_available_move.append(before_row - r)
                    col_available_move.append(before_col)
                except:
                    pass_variable = 1
            for c in range(1, 9):
                try:
                    if self.board[before_row][before_col + c] != '_':
                        col_available_move.append(before_col + c)
                        row_available_move.append(before_row)
                        break
                    col_available_move.append(before_col + c)
                    row_available_move.append(before_row)
                except:
                    pass_variable = 0
            for c in range(1, 9):
                try:
                    if self.board[before_row][before_col - c] != '_':
                        col_available_move.append(before_col - c)
                        row_available_move.append(before_row)
                        break
                    col_available_move.append(before_col - c)
                    row_available_move.append(before_row)
                except:
                    pass_variable = 1
            for r in range(-1, 2, 1):
                for c in range(-1, 2, 1):
                    try:
                        col_available_move.append(before_col + c)
                        row_available_move.append(before_row + r)
                    except:
                        pass_variable = 5
                    try:
                        if (c < 0) and (r < 0) and (self.board[before_row - 1][before_col - 1] == '_'):
                            for i in range(7):
                                if self.board[before_row + r - i][before_col + c - i] != '_':
                                    col_available_move.append(before_col + c - i)
                                    row_available_move.append(before_row + r - i)
                                    break
                                elif self.board[before_row + r - i][before_col + c - i] == '_':
                                    col_available_move.append(before_col + c - i)
                                    row_available_move.append(before_row + r - i)
                    except:
                        pass_variable = 5
                    try:
                        if (c < 0) and (r > 0) and (self.board[before_row + 1][before_col - 1] == '_'):
                            for i in range(7):
                                if self.board[before_row + r + i][before_col + c - i] != '_':
                                    col_available_move.append(before_col + c - i)
                                    row_available_move.append(before_row + r + i)
                                    break
                                elif self.board[before_row + r + i][before_col + c - i] == '_':
                                    col_available_move.append(before_col + c - i)
                                    row_available_move.append(before_row + r + i)
                    except:
                        pass_variable = 5
                    try:
                        if (c > 0) and (r > 0) and (self.board[before_row + 1][before_col + 1] == '_'):
                            for i in range(7):
                                if self.board[before_row + r + i][before_col + c + i] != '_':
                                    col_available_move.append(before_col + c + i)
                                    row_available_move.append(before_row + r + i)
                                    break
                                elif self.board[before_row + r + i][before_col + c + i] == '_':
                                    col_available_move.append(before_col + c + i)
                                    row_available_move.append(before_row + r + i)
                    except:
                        pass_variable = 5
                    try:
                        if (c > 0) and (r < 0) and (self.board[before_row - 1][before_col + 1] == '_'):
                            for i in range(7):
                                if self.board[before_row + r - i][before_col + c + i] != '_':
                                    col_available_move.append(before_col + c + i)
                                    row_available_move.append(before_row + r - i)
                                    break
                                elif self.board[before_row + r - i][before_col + c + i] == '_':
                                    col_available_move.append(before_col + c + i)
                                    row_available_move.append(before_row + r - i)
                    except:
                        pass_variable = 5
        available_moves = list(zip(row_available_move, col_available_move))
        if (after_row, after_col) in available_moves:
            return True
        return False

    def make_move(self):
        while True:  # white move
            print(self.board)
            try:
                white_user_input_before = re.split(',(\\s)*',input("Where is the piece you wanna move? Input as row,col: "))  # '0, 3'
                before_row, before_col = int(white_user_input_before[0]) - 1, int(white_user_input_before[-1]) - 1
                white_user_input_after = re.split(',(\\s)*',input("Where would you like to move? Input as row,col: "))  # '0, 3'
                after_row, after_col = int(white_user_input_after[0]) - 1, int(white_user_input_after[-1]) - 1
            except:
                print('Invalid input! Try inputting number, number')
            if ('white' in self.board[before_row][before_col]) and ('white' not in self.board[after_row][after_col]):
                if self.is_available_move(before_row, before_col, after_row, after_col) is True:
                    self.board[after_row][after_col] = self.board[before_row][before_col]
                    self.board[before_row][before_col] = '_'
                else:
                    print('Your move is not in the available_moves!')
                    print('Have another try')
                    continue
            else:
                print('It is whites turn')
                continue
            print(self.board)
            is_black_king_absent = 1
            for r in range(0, 8):
                for c in range(0, 8):
                    if self.board[r][c] == 'black_king':
                        is_black_king_absent = 0
                        break
            if is_black_king_absent == 1:
                print('Congrats! White has won the game!')
                quit()


            while True:#blacks move
                try:
                    black_user_input_before = re.split(',(\\s)*', input("Where is the piece you wanna move? Input as row,col: "))  # '0, 3'
                    before_row, before_col = int(black_user_input_before[0]) - 1, int(black_user_input_before[-1]) - 1
                    black_user_input_after = re.split(',(\\s)*', input("Where would you like to move? Input as row,col: "))  # '0, 3'
                    after_row, after_col = int(black_user_input_after[0]) - 1, int(black_user_input_after[-1]) - 1
                except:
                    print('Invalid input! Try inputting number, number')
                    continue
                if ('black' in self.board[before_row][before_col]) and ('black' not in self.board[after_row][after_col]):
                    if self.is_available_move(before_row, before_col, after_row, after_col) is True:
                        self.board[after_row][after_col] = self.board[before_row][before_col]
                        self.board[before_row][before_col] = '_'
                    else:
                        print('Your move is not in the available_moves!')
                        print('Have another try')
                        continue
                else:
                    print('It is blacks turn')
                    continue
                break
                is_white_king_absent = 1
                for r in range(8):
                    for c in range(8):
                        if self.board[r][c] == 'white_king':
                            is_white_king_absent = 0
                            break
                if is_white_king_absent == 1:
                    print('Congrats! Black has won the game!')
                    quit()


if __name__ == '__main__':
    play = Chess()
    play.make_move()


#AS OF 2/10/2023 , here the problems that need to be fixed
#Repair the check win functions idea: make in the input resign option DONE
#Sometimes the before rows and cols are out of the board and you get an error in the is_available_moves so fix it DONE
#FIX THE TURNS (BLACK AND WHITE EACH TURN BY TURN) DONE
#rook forward not working DONE
#knight not working DONE
#make it so you dont take ur own pieces with available moves DONE
#castling
#en passant
#pawn promotion
