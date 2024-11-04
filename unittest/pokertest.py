import unittest
from poker import isValidCard, validInput, transferPoint, justPoint, deal, winner, game

class TestCardGame(unittest.TestCase):
    def test_isValidCard(self):
        # Valid card tests
        self.assertTrue(isValidCard('A'))
        self.assertTrue(isValidCard('10'))
        self.assertTrue(isValidCard('K'))
        # Invalid card tests
        self.assertFalse(isValidCard('11'))
        self.assertFalse(isValidCard('Z'))

    def test_validInput(self):
        # Valid input list
        self.assertTrue(validInput(['A', '10', 'K']))
        # Invalid input list
        self.assertFalse(validInput(['A', '11', 'K']))
        
    def test_transferPoint(self):
        # Check points for cards
        self.assertEqual(transferPoint('A'), 1)
        self.assertEqual(transferPoint('10'), 10)
        self.assertEqual(transferPoint('K'), 0.5)
        
    def test_justPoint(self):
        # Within limits
        self.assertEqual(justPoint(10), 10)
        # Exceeding limit (bust)
        self.assertEqual(justPoint(10.6), 0)

    def test_deal(self):
        # Deal within limit
        self.assertEqual(deal(5, 'A'), 6)
        # Deal with bust
        self.assertEqual(deal(10, '2'), 0)

    def test_winner(self):
        # Player wins
        self.assertEqual(winner(9, 8), "player win 9 8")
        # Computer wins
        self.assertEqual(winner(8, 9), "computer win 8 9")
        # Tie
        self.assertEqual(winner(10, 10), "tie 10")

    def test_game_player_win(self):
        # Player wins with a higher score than computer
        result = game(['A', '9'], ['2', '5'])
        self.assertEqual(result, "player win 10 7")

    def test_game_computer_win(self):
        # Computer wins with a higher score than player
        result = game(['3', '4'], ['A', '9'])
        self.assertEqual(result, "computer win 7 10")

    def test_game_tie(self):
        # Tie scenario
        result = game(['A', '9'], ['10'])
        self.assertEqual(result, "tie 10")

    def test_game_bust(self):
        # Player busts
        result = game(['10', '4'], ['A', '8'])
        self.assertEqual(result, "computer win 0 9")
        
        # Computer busts
        result = game(['A', '8'], ['10', '4'])
        self.assertEqual(result, "player win 9 0")

    def test_game_invalid_input(self):
        # Invalid input test
        result = game(['A', '11'], ['10'])
        self.assertEqual(result, "Error input")

if __name__ == '__main__':
    unittest.main()
