import unittest

from connect4_game import Connect4State

class TestVerticalWinning(unittest.TestCase):

    def setUp(self) -> None:
        self.state = Connect4State()
        self.state.grid =  [[1, 0, 0, 0, 0, 0, 0],
                            [1, 0, 0, 0, 0, 0, 0],
                            [1, 0, 0, 0, 0, 0, 0],
                            [1, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0]
                            ]

    def test_player1_won_vertical(self):
        self.assertTrue(self.state.is_game_over())
        self.assertEqual(self.state.player_won, 1)


class TestHorizontalWinning(unittest.TestCase):

    def setUp(self) -> None:
        self.state = Connect4State()
        self.state.grid = [[1, 1, 1, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0]
                            ]

    def test_player1_won_horizontal(self):
        self.assertTrue(self.state.is_game_over())
        self.assertEqual(self.state.player_won, 1)

class TestDiagWinning(unittest.TestCase):

    def setUp(self) -> None:
        self.state = Connect4State()
        self.state.grid =  [
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 1, 0, 0, 0, 0],
                            [0, 1, 0, 0, 0, 3, 2],
                            [1, 0, 0, 0, 3, 2, 0],
                            [0, 0, 0, 3, 2, 0, 0],
                            [0, 0, 0, 2, 0, 0, 0]
                            ]

    def test_player1_won_horizontal(self):
        self.assertTrue(self.state.is_game_over())
        self.assertEqual(self.state.player_won, 2)

class TestDiagWinning2(unittest.TestCase):

    def setUp(self) -> None:
        self.state = Connect4State()
        self.state.grid =  [
                            [0, 0, 0, 2, 0, 0, 0],
                            [0, 0, 0, 0, 2, 0, 0],
                            [1, 0, 0, 0, 0, 2, 0],
                            [0, 2, 0, 0, 0, 0, 2],
                            [0, 0, 2, 0, 0, 0, 0],
                            [0, 0, 0, 2, 0, 0, 0]
                            ]

    def test_player1_won_horizontal(self):
        self.assertTrue(self.state.is_game_over())
        self.assertEqual(self.state.player_won, 2)

if __name__ == '__main__':
    unittest.main()
