from io import StringIO
from unittest.mock import patch

import pytest

from ..rock_paper_scissors.rps_game import Game, Participant


def test_single_round_draw():
    Participant('Player1')
    Participant('Player2')
    with patch('builtins.input', side_effect=['rock', 'rock', 'n']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            Game()
            output = mock_stdout.getvalue().strip()
            assert "It's a draw." in output


def test_single_round_player1_win():
    Participant('Player1')
    Participant('Player2')
    with patch('builtins.input', side_effect=['rock', 'scissors', 'n']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            Game()
            output = mock_stdout.getvalue().strip()
            assert 'Winner is Player1.' in output


def test_single_round_player2_win():
    Participant('Player1')
    Participant('Player2')
    with patch('builtins.input', side_effect=['paper', 'scissors', 'n']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            Game()
            output = mock_stdout.getvalue().strip()
            assert 'Winner is Player2.' in output


if __name__ == '__main__':
    pytest.main()
