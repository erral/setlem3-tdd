"""
Tenis jokoaren markadorea simulatu

Arauak:
0-0 - Love
1-0 - Fifteen - Love
2-0 - Thirty - Love
3-0 - Forty - Love
3-3 - Deuce
4-0 - Winner player1
4-3 - Advantage player
4-4 - Deuce

(has to win by two)

2-2 - Thirty All
1-1 - Fifteen All

"""

import pytest

SCORESTRINGS = {
    '0-0': 'Love',
    '1-0': 'Fifteen - Love',
    '2-0': 'Thirty - Love',
    '3-0': 'Forty - Love',
    '3-3': 'Deuce',
    # '4-0': 'Winner player1',
    # '4-3': 'Advantage player',
    # '4-4': 'Deuce',
    '2-2': 'Thirty All',
    '1-1': 'Fifteen All'
}


class InvalidGamePlay(Exception):
    """ Exception to raise when an invalid game is played """


class Player(object):
    def __init__(self, name):
        self.name = name
        self.score = 0


class Tenis(object):

    def __init__(self):
        self.player1 = Player(name='player1')
        self.player2 = Player(name='player2')

    def score(self):
        return '-'.join([str(self.player1.score), str(self.player2.score)])

    def result(self):
        if self.player1.score - self.player2.score >= 2 and self.player1.score >= 4:
            return 'Winner player1'
        elif self.player2.score - self.player1.score >= 2 and self.player2.score >= 4:
            return 'Winner player2'
        elif self.player1.score == self.player2.score and self.player1.score >= 3:
            return 'Deuce'
        elif self.player1.score == self.player2.score + 1 and self.player1.score >= 4:
            return 'Advantage player1'
        elif self.player2.score == self.player1.score + 1 and self.player2.score >= 4:
            return 'Advantage player2'

        return SCORESTRINGS.get(self.score())

    def wins_1(self):
        if self.is_valid_score(self.player1.score + 1, self.player2.score):
            self.player1.score += 1
        else:
            raise InvalidGamePlay()

    def wins_2(self):
        if self.is_valid_score(self.player2.score + 1, self.player1.score):
            self.player2.score += 1
        else:
            raise InvalidGamePlay()

    def is_valid_score(self, score1, score2):
        if score1 >= 4 or score2 >= 4:
            return abs(score1 - score2) <= 2
        else:
            return True


class TestTenis:

    def setup(self):
        self.t = Tenis()

    def test_tenis_exists(self):

        assert isinstance(self.t, Tenis)

    def test_initial_result(self):

        assert self.t.result() == 'Love'

    def test_15_love(self):

        self.t.wins_1()
        assert self.t.result() == 'Fifteen - Love'

    def test_30_love(self):

        self.t.wins_1()
        self.t.wins_1()
        assert self.t.result() == 'Thirty - Love'

    def test_40_love(self):

        self.t.wins_1()
        self.t.wins_1()
        self.t.wins_1()
        assert self.t.result() == 'Forty - Love'

    def test_deuce_3(self):

        self.t.wins_1()
        self.t.wins_1()
        self.t.wins_1()
        self.t.wins_2()
        self.t.wins_2()
        self.t.wins_2()
        assert self.t.result() == 'Deuce'

    def test_advantage_player_1_4_3(self):

        self.t.wins_1()
        self.t.wins_1()
        self.t.wins_1()
        self.t.wins_2()
        self.t.wins_2()
        self.t.wins_2()
        self.t.wins_1()
        assert self.t.result() == 'Advantage player1'

    def test_advantage_player_2_3_4(self):

        self.t.wins_1()
        self.t.wins_1()
        self.t.wins_1()
        self.t.wins_2()
        self.t.wins_2()
        self.t.wins_2()
        self.t.wins_2()
        assert self.t.result() == 'Advantage player2'

    def test_advantage_player_1_6_5(self):

        self.t.wins_1()
        self.t.wins_1()
        self.t.wins_1()
        self.t.wins_2()
        self.t.wins_2()
        self.t.wins_2()
        self.t.wins_1()
        self.t.wins_2()
        self.t.wins_1()
        self.t.wins_2()
        self.t.wins_1()

        assert self.t.result() == 'Advantage player1'

    def test_fifteen_all(self):

        self.t.wins_1()
        self.t.wins_2()
        assert self.t.result() == 'Fifteen All'

    def test_thirty_all(self):

        self.t.wins_1()
        self.t.wins_2()
        self.t.wins_1()
        self.t.wins_2()
        assert self.t.result() == 'Thirty All'

    def test_invalid_game_raises_exception(self):
        def invalid_game_function():
            self.t.wins_1()
            self.t.wins_1()
            self.t.wins_1()
            self.t.wins_1()
            self.t.wins_2()

        with pytest.raises(InvalidGamePlay):
            invalid_game_function()
