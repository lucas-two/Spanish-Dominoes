from pyswip import Prolog

import random


class Player:
    def __init__(self, player, team):
        self._player = player
        self._team = team
        self._tiles = []

    @property
    def hand(self):
        return self._tiles

    @hand.setter
    def hand(self, value):
        self._tiles = value


class Game:
    def __init__(self):
        self._dominoes = [
            [0,0],
            [0,1],[1,1],
            [0,2],[1,2],[2,2],
            [0,3],[1,3],[2,3],[3,3],
            [0,4],[1,4],[2,4],[3,4],[4,4],
            [0,5],[1,5],[2,5],[3,5],[4,5],[5,5],
            [0,6],[1,6],[2,6],[3,6],[4,6],[5,6],[6,6]
        ]
        self.shuffle()

    @property
    def dominoes(self):
        return self._dominoes
    
    @dominoes.setter
    def dominoes(self, value):
        self._dominoes = value

    def shuffle(self, seed=1):
        """
        Shuffle the dominoes for a game
        """
        # NOTE: SEED is being used for testing purposes.
        random.seed(seed)
        random.shuffle(self.dominoes)


def main():

    # Declare our players
    p1 = Player('player_1', 1)
    p2 = Player('player_2', 1)
    p3 = Player('player_3', 2)
    p4 = Player('player_4', 2)

    players = [p1, p2, p3, p4]
    g = Game()
    

    print(g.dominoes)


    prolog = Prolog()
    prolog.assertz("father(michael,john)")
    prolog.assertz("father(michael,gina)")

    # for soln in prolog.query("father(X,Y)"):
    #     print(soln["X"], "is the father of", soln["Y"])

    # print("Hello world!")


if __name__ == '__main__':
    main()