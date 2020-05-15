from pyswip import Prolog

import random

class Player:
    def __init__(self, name, team):
        self._name = name
        self._team = team
        self._tiles = []

    @property
    def name(self):
        return self._name

    @property
    def team(self):
        return self._team

    @property
    def tiles(self):
        return self._tiles

    @tiles.setter
    def tiles(self, value):
        self._tiles = value

class Game:
    def __init__(self):
        self._players = [
            Player('player_1', 1),
            Player('player_2', 2),
            Player('player_1', 1),
            Player('player_2', 2),
        ]
        self._dominoes = [
            [0,0],
            [0,1],[1,1],
            [0,2],[1,2],[2,2],
            [0,3],[1,3],[2,3],[3,3],
            [0,4],[1,4],[2,4],[3,4],[4,4],
            [0,5],[1,5],[2,5],[3,5],[4,5],[5,5],
            [0,6],[1,6],[2,6],[3,6],[4,6],[5,6],[6,6]
        ]
        self._board = []
        self._round = 1
        self.shuffle()
        self.deal()

    @property
    def round(self):
        return self._round
    
    @round.setter
    def round(self, value):
        self._round = value

    @property
    def players(self):
        return self._players

    @property
    def dominoes(self):
        return self._dominoes
    
    @dominoes.setter
    def dominoes(self, value):
        self._dominoes = value

    @property
    def board(self):
        return self._board

    def place_tile(self, tile, side='r'):
        # Are we placing it on the left side?
        if side == 'l':
            self.board.insert(0,tile)
        # Or are we placing it on the right side?
        else:
            self.board.insert(len(self.board),tile)

    def shuffle(self, seed=1):
        """
        Shuffle the set of dominoes
        """
        # NOTE: SEED is being used for testing purposes.
        random.seed(seed)
        random.shuffle(self.dominoes)

    def deal(self):
        """
        Deal out 7 dominoes to each player
        """
        avalible_tiles = self.dominoes

        # For each player
        for player in self.players:
            # Deal the player 7 tiles
            player.tiles = avalible_tiles[:7]
            # Delete the tiles from the avalible tiles list
            del avalible_tiles[:7]

def main():
    # TODO: Get a game to play
    # TODO: Prolog program to show which tile is played
    # TODO: Prolog program to show the new board
    # TODO: Create a Bayseian belief Representation

    # PROLOG
    prolog = Prolog()
    prolog.consult("dominoes.pl")

    a = list(prolog.query("father(michael,X)"))
    print(a)


    print("\nGame started!\n")
    g = Game()
    
    print("----------------")
    print("Tiles:")
    for p in g.players:
        print(p.name, p.tiles)
    print("---------------")
    
    a = []
    if not a:
        print("NEW")

    while True:

        print("Round %d\n" % g.round)

        for p in g.players:

            # Check if the player can play
            # ....

            # If player CANNOT play...
            if not p.tiles:
                print("No tiles...")
                continue # Pass

            # If player CAN play...
            print("I can play!")
            g.place_tile(p.tiles.pop())
            print(g.board)

        g.round += 1

        break


if __name__ == '__main__':
    main()