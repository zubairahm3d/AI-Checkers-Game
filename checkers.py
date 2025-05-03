import math
import time

class Checkers:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.states_history = [] 
        self.populate_board()
        self.current_player = 1

    def populate_board(self):
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.board[row][col] = 'O'

        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.board[row][col] = 'X'

    def print_board(self):
        print("      0  1  2  3  4  5  6  7")
        print("   ---------------------------")
        for i, row in enumerate(self.board):
            print(f" {i} |", end=' ')
            for j, square in enumerate(row):
                if (i + j) % 2 == 0:
                    print('\033[47m', end='')
                else:
                    print('\033[40m', end='')
                print(f" {square}",end=' ')
            print('\033[0m|',end=' ')
            print(f" {i}")
        print("   ---------------------------")
        print("      0  1  2  3  4  5  6  7")


    def update_states_history(self):
        self.states_history.append([row[:] for row in self.board])
        if len(self.states_history) > 10:
            self.states_history.pop(0)


    def is_valid_move(self, start, end):
        x1, y1 = start
        x2, y2 = end
        if self.board[x1][y1] == ' ' or self.board[x2][y2] != ' ':
            return False
        return True
        # if self.current_player == 1 and (self.board[start[0]][start[1]] == 'O' or self.board[start[0]][start[1]] == 'K'):
        #     return (abs(x2 - x1) == 1) and (abs(y2 - y1) == 1) and (self.board[x1][y1] == 'O') or \
        #         (abs(x2 - x1) == 2) and (abs(y2 - y1) == 2) and (self.board[(x1 + x2) // 2][(y1 + y2) // 2] == 'X')
        # elif self.current_player == 2 and (self.board[start[0]][start[1]] == 'X' or self.board[start[0]][start[1]] == 'k'):
        #     return (abs(x2 - x1) == 1) and (abs(y2 - y1) == 1) and (self.board[x1][y1] == 'X') or \
        #         (abs(x2 - x1) == 2) and (abs(y2 - y1) == 2) and (self.board[(x1 + x2) // 2][(y1 + y2) // 2] == 'O')


        

    def get_valid_moves(self, player):
        valid_moves = []
        # for row in range(8):
        #     for col in range(8):
        #         if (row + col) % 2 == 1 and self.board[row][col] != ' ':
        #             if (player == 1 and (self.board[row][col] == 'O' or self.board[row][col] == 'K')) or \
        #                     (player == 2 and (self.board[row][col] == 'X' or self.board[row][col] == 'k')):
        #                 if player == 1 or self.board[row][col] == 'K':
        #                     directions = [(1, 1), (1, -1)]
        #                 else:
        #                     directions = [(-1, 1), (-1, -1)]

        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 1 and self.board[row][col] != ' ':
                    if (player == 1 and (self.board[row][col] == 'O')) or \
                            (player == 2 and (self.board[row][col] == 'X')):
                        if player == 1:
                            directions = [(1, 1), (1, -1)]
                        else:
                            directions = [(-1, 1), (-1, -1)]

                        for dx, dy in directions:
                            if 0 <= row + dx < 8 and 0 <= col + dy < 8:
                                if self.board[row + dx][col + dy] == ' ':
                                    valid_moves.append(((row, col), (row + dx, col + dy)))
                                elif 0 <= row + 2 * dx < 8 and 0 <= col + 2 * dy < 8:
                                    if self.board[row + dx][col + dy] != self.board[row][col] \
                                            and self.board[row + 2 * dx][col + 2 * dy] == ' ':
                                        valid_moves.append(((row, col), (row + 2 * dx, col + 2 * dy)))
        


        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 1 and self.board[row][col] != ' ':
                    if (player == 1 and (self.board[row][col] == 'K')) or \
                            (player == 2 and (self.board[row][col] == 'k')):
                        if player == 1:
                            directions = [(1, 1), (1, -1),(-1, 1), (-1, -1)]
                        else:
                            directions = [(-1, 1), (-1, -1),(1, 1), (1, -1)]

                        for dx, dy in directions:
                            if 0 <= row + dx < 8 and 0 <= col + dy < 8:
                                if self.board[row + dx][col + dy] == ' ':
                                    valid_moves.append(((row, col), (row + dx, col + dy)))
                                elif 0 <= row + 2 * dx < 8 and 0 <= col + 2 * dy < 8:
                                    if self.board[row + dx][col + dy] != self.board[row][col] \
                                            and self.board[row + 2 * dx][col + 2 * dy] == ' ':
                                        valid_moves.append(((row, col), (row + 2 * dx, col + 2 * dy)))


                        
        return valid_moves
    
    # def get_valid_piece_moves(self, player):
    #     return

    # def get_valid_king_moves(self,player):
    #     return

    def make_move(self, start, end):
        x1, y1 = start
        x2, y2 = end
        if self.is_valid_move(start, end):
            self.board[x2][y2] = self.board[x1][y1]
            self.board[x1][y1] = ' '
            if abs(x2 - x1) == 2:
                self.board[(x1 + x2) // 2][(y1 + y2) // 2] = ' '
            if self.current_player == 1 and x2 == 7:
                self.board[x2][y2] = 'K'
            elif self.current_player == 2 and x2 == 0:
                self.board[x2][y2] = 'k'
            self.current_player = 3 - self.current_player
            self.update_states_history()  
        else:
            print("Invalid Move!")

    def get_winner(self):
        x_count = 0
        o_count = 0
        for row in self.board:
            for square in row:
                if square == 'X' or square == 'k':
                    x_count += 1
                elif square == 'O' or square == 'K':
                    o_count += 1
        if x_count == 0:#player 2 loses
            return 1
        elif o_count == 0:#player 1 loses
            return 2
        else:
            return 0

    def minimax(self, depth, maximizing_player):
        if depth == 0 or self.get_winner() != 0:
            return self.evaluate_board(), None
        
        valid_moves = self.get_valid_moves(self.current_player)
        # print("checking: ",valid_moves)
        if maximizing_player:
            max_eval = -math.inf
            # print("max eval",max_eval)
            best_move = None
            for move in valid_moves:
                clone = self.clone()
                clone.make_move(move[0], move[1])
                eval, _ = clone.minimax(depth - 1, False)
                # print("eval: ",eval)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
            # print(eval," ",max_eval)
            return max_eval, best_move
        else:
            min_eval = math.inf
            best_move = None
            for move in valid_moves:
                clone = self.clone()
                clone.make_move(move[0], move[1])
                eval, _ = clone.minimax(depth - 1, True)
                # print("eval: ",eval)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
            return min_eval, best_move

    def minimax_ab(self, depth, maximizing_player, alpha=-math.inf, beta=math.inf):
        if depth == 0 or self.get_winner() != 0:
            return self.evaluate_board(), None
        
        valid_moves = self.get_valid_moves(self.current_player)
        
        if maximizing_player:
            max_eval = -math.inf
            best_move = None
            for move in valid_moves:
                clone = self.clone()
                clone.make_move(move[0], move[1])
                eval, _ = clone.minimax_ab(depth - 1, False, alpha, beta)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break 
            return max_eval, best_move
        else:
            min_eval = math.inf
            best_move = None
            for move in valid_moves:
                clone = self.clone()
                clone.make_move(move[0], move[1])
                eval, _ = clone.minimax_ab(depth - 1, True, alpha, beta)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break 
            return min_eval, best_move

    def clone(self):
        clone = Checkers()
        clone.board = [row[:] for row in self.board]
        clone.current_player = self.current_player
        return clone

    def evaluate_board(self):
        x_count = 0
        o_count = 0
        for row in self.board:
            for square in row:
                if square == 'X' or square == 'k':
                    x_count += 1
                elif square == 'O' or square == 'K':
                    o_count += 1
        # print("X=",x_count,"O",o_count)
        return x_count - o_count
    
    def check_draw(self):
        if len(self.states_history) >= 10:
            latest_state = self.states_history[-1]
            count = 0
            for state in self.states_history[:-1]:
                if state == latest_state:
                    count += 1
                    if count >= 2:
                        return True
            return False
        else:
            return False


    def play_game(self):
        mode = int(input("1. AI vs Player\n2. AI vs AI\n"))
        algo_choice = int(input("Choose AI algorithm (1 for Minimax, 2 for Alpha-Beta): "))
        difficulty = int(input("Choose Difficulty \n1. Easy\n2.Medium\n3.Hard\n"))
        if difficulty == 1:
            difficulty = 1
        elif difficulty == 2:
            difficulty = 3
        elif difficulty == 3:
            difficulty = 5
        while self.get_winner() == 0:
            self.print_board()
            print(f"Player {self.current_player}'s turn:")
            if self.current_player == 1:
                if algo_choice == 1:
                    _, move = self.minimax(difficulty, True)
                elif algo_choice == 2:
                    _, move = self.minimax_ab(difficulty, True)
                if move is not None:
                    print("Chosen move:", move)
                    self.make_move(move[0], move[1])
                else:
                    print("No valid move found for Player 1 (AI)")
                    break

            else:
                if mode == 1:
                    valid_moves = self.get_valid_moves(self.current_player)
                    if len(valid_moves) == 0:
                        print("No valid moves.")
                        break
                        # self.current_player = 3 - self.current_player
                        # continue
                    print("Valid moves:", valid_moves)
                    start = tuple(map(int, input("Enter start position (row, col): ").split()))
                    end = tuple(map(int, input("Enter end position (row, col): ").split()))
                    if (start, end) in valid_moves:
                        self.make_move(start, end)
                    else:
                        # break
                        print("Invalid move. Try again.")
                else:
                    if algo_choice == 1:
                        _, move = self.minimax(difficulty, False)
                    elif algo_choice == 2:
                        _, move = self.minimax_ab(difficulty, False)
                    if move is not None:
                        print("Chosen move:", move)
                        self.make_move(move[0], move[1])
                    else:
                        print("No valid move found for Player 2 (AI)")
                        break
                # time.sleep(0.5)
                if self.check_draw():
                    print("Draw!. The same state has occured multiple times before.")
                    exit()

        self.print_board()
        winner = self.get_winner()
        if winner == 1:
            print("Player 1 (AI) wins!")
        elif winner == 2:
            if mode == 1:
                print("Player 2 wins!")
            else:
                print("Player 2 (AI) wins!")
        else:
            if(self.evaluate_board() > 0):
                print("Player 2 (AI) wins!")
            else:
                print("Player 1 (AI) wins!")

            

if __name__ == "__main__":
    game = Checkers()
    game.play_game()
