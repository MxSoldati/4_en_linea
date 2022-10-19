class Game:
    def __init__(self):
        self.board = [[0 for column in range(8)]for row in range(8)]
        self.players = 1

    def view_row(self,colum):
        for row in range(7,0,-1):
            if self.board [row][colum] == 0:    # ver la excepcion de la columna entera
                return row

    def add_token_in_board(self,colum):
        self.board [self.view_row(colum)][colum] = self.players
        self.players_turn()

    def players_turn(self):
        if self.players == 1:
            self.players = 2
        else:
            self.players = 1

    def generate_directions():
        return [(-1, 1),(0, 1),(1, 1),(1, 0)]
    
    
    def in_board(row, col):
        return (
            row >= 0 and
            row <= 7 and
            col >= 0 and
            col <= 7
        )
    
    
    def generate_winner_coord(row, col):
        winner_directions = Game.generate_directions()
        winner_coord = []
        for row_delta, col_delta in winner_directions:
            winner_coord_direction = []
            for delta in range(4):
                if Game.in_board(row + (row_delta * delta), col + (col_delta * delta)):
                    winner_coord_direction.append(
                        (
                            row + (row_delta * delta),
                            col + (col_delta * delta),
                        )
                    )
                else:
                    break
            if len(winner_coord_direction) == 4:
                winner_coord.append(winner_coord_direction)
    
        return winner_coord
    
    
    def has_winner(board, row, col):
        search = board[row][col]
        winner_coord = Game.generate_winner_coord(row, col)
        for winner_coord_direction in winner_coord:
            count = 0
            for coord_direction_row, coord_direction_col in winner_coord_direction:
                if board[coord_direction_row][coord_direction_col] == search:
                    count += 1
            if count == 4:
                return True
        return False
    