import unittest

from connect4_game import Connect4State

class TestVerticalWinning(unittest.TestCase):

    def setUp(self) -> None:
        self.state = Connect4State()
        self.state.grid =  [[1, 0, 0, 0, 0, 0],
                            [1, 0, 0, 0, 0, 0],
                            [1, 0, 0, 0, 0, 0],
                            [1, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0]
                            ]

    def test_player1_won_vertical(self):
        self.assertTrue(self.state.is_game_over())
        self.assertEqual(self.state.player_won, 1)




class TestHorizontalWinning(unittest.TestCase):

    def setUp(self) -> None:
        self.state = Connect4State()
        self.state.grid = [[1, 1, 1, 1, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0]
                            ]

    def test_player1_won_horizontal(self):
        self.assertTrue(self.state.is_game_over())
        self.assertEqual(self.state.player_won, 1)

if __name__ == '__main__':
    unittest.main()
