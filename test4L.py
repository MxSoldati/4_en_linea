
import unittest
from game4L import Game 

class TestInLine(unittest.TestCase):

    def test_board(self):
        board = Game()
        self.assertEqual(board.board,
        [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],]) 

    def test_first_player(self):
        space = Game()
        self.assertEqual(space.players,1)

    def test_view_row(self):
        space = Game()
        space.view_row(3)
        self.assertTrue(
        [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0]]
        )
   
    def test_add_token_to_board(self):
        space = Game()
        space.add_token_in_board(3)
        self.assertEqual(space.board, 
        [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0]]
        )

    def test_players_turn(self):
        turn = Game()
        turn.view_row(3) #player 1
        turn.add_token_in_board(3)
        turn.view_row(6)
        turn.add_token_in_board(6)
        turn.view_row(2)
        turn.add_token_in_board(2)
        turn.view_row(4)
        turn.add_token_in_board(4)
        self.assertEqual(turn.board,
        [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,1,1,2,0,2,0]] 
        )

    def test_generate_directions(self):
        g = Game
        winner_directions = g.generate_directions()
        self.assertEqual(
            winner_directions,
            [
                (-1, 1,),
                (0, 1,),
                (1, 1,),
                (1, 0,),
            ],
        )

    def test_winner_board_coord(self):
        g = Game
        winner_coord = g.generate_winner_coord(4, 4)
        self.assertEqual(
            winner_coord,
            [
                [(4, 4), (3, 5), (2, 6), (1, 7)],
                [(4, 4), (4, 5), (4, 6), (4, 7)],
                [(4, 4), (5, 5), (6, 6), (7, 7)],
                [(4, 4), (5, 4), (6, 4), (7, 4)],

            ],
        )

    def test_winner_board_coord_edge_empty(self):
        g = Game
        winner_coord = g.generate_winner_coord(6, 6)
        self.assertEqual(
            winner_coord,
            [],
        )

    def test_winner_board_coord_edge_not_empty(self):
        g = Game
        winner_coord = g.generate_winner_coord(4, 6)
        self.assertEqual(
            winner_coord,
            [
                [(4, 6), (5, 6), (6, 6), (7, 6)],
            ],
        )

    def test_winner_row_col(self):
        g = Game
        board =[
            [ 0 for _ in range(8) ]
            for _ in range(8)
        ]

        board[4][4] = 1
        board[4][5] = 1
        board[4][6] = 1
        board[4][7] = 1
        winner = g.has_winner(board, 4, 4)
        self.assertTrue(winner)

    def test_not_winner_row_col(self):
        g = Game
        board =[
            [ 0 for _ in range(8) ]
            for _ in range(8)
        ]

        board[4][4] = 1
        board[4][6] = 1
        board[4][7] = 1
        winner = g.has_winner(board, 4, 4)
        self.assertFalse(winner)

    def test_in_board(self):
        g = Game
        self.assertTrue(g.in_board(4, 4))
        self.assertTrue(g.in_board(0, 0))
        self.assertTrue(g.in_board(7, 7))

    def test_not_in_board(self):
        g = Game
        self.assertFalse(g.in_board(-1, -1))
        self.assertFalse(g.in_board(0, -1))
        self.assertFalse(g.in_board(8, 6))


if __name__ == '__main__':
    unittest.main()


   