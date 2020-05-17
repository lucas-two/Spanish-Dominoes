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
            Player('Mark', 'RED'),
            Player('John', 'BLUE'),
            Player('Luke', 'RED'),
            Player('Matt', 'BLUE'),
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
        self._H = None
        self._T = None
        self._board = []
        self._round = 1
        self.shuffle()
        self.deal()

    @property
    def H(self):
        return self._H
    
    @H.setter
    def H(self, value):
        self._H = value

    @property
    def T(self):
        return self._T

    @T.setter
    def T(self, value):
        self._T = value

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

    def place_tile(self, tile, side='t'):
        # Are we placing it on the left side?
        if side == 'h':
            self.board.insert(0,tile)
        # Or are we placing it on the right side?
        else:
            self.board.insert(len(self.board),tile)
        # Update the Head and Tail
        self.update_HT()

    def shuffle(self, seed=3):
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
    
    def update_HT(self):
        """
        Update the head and tail value of board
        """
        self.H = self.board[0][0]
        self.T = self.board[len(self.board) - 1][1]



def get_playable_tiles(prolog, head, tail, tiles):
    """
    Gets playable tiles of player
    """
    # Query prolog for the playable tiles
    playable_tiles = (list(prolog.query("can_play(%s,%s,%s,W)." % (head, tail, tiles))))
    # Convert tiles to tuples so we can use them as a key
    for tile in playable_tiles:
        tile['W'] = tuple(tile['W'])

    # Add tiles into a set
    playable_tiles_set = []
    for tile in playable_tiles:
        playable_tiles_set.append(tile['W'])
    # Remove duplicates
    playable_tiles_set = list(dict.fromkeys(playable_tiles_set))
    
    # Convert tiles back into list
    for tile in playable_tiles_set:
        tile = list(tile)
    
    # Convert tiles back into lists
    playable_tiles_set = [list(tile) for tile in playable_tiles_set]

    return playable_tiles_set

def place_tile(g, prolog, tile):
    """
    Places a tile on the board with the correct oreitation
    """

    head = g.H
    tail = g.T

    # Query prolog wheather the tile fits on the low end or high end
    low_flag = list(prolog.query("can_play_low_end(%s,%s,%s,W)." % (head, tail, [tile])))
    high_flag = list(prolog.query("can_play_high_end(%s,%s,%s,W)." % (head, tail, [tile])))

    # We are working with the Head [<---]
    if low_flag:
        if tile[1] != head:
            tile = list(reversed(tile))
        # Place tile on the head
        g.place_tile(tile,'h')

    # Or we are working with the tail [--->]
    elif high_flag:
        if tile[0] != tail:
            tile = list(reversed(tile))
        # Place tile on the tail
        g.place_tile(tile,'t')


def main():
    # TODO: Get a game to play
    # TODO: Prolog program to show which tile is played
    # TODO: Prolog program to show the new board
    # TODO: Create a Bayseian belief Representation

    # PROLOG
    prolog = Prolog()
    prolog.consult("dominoes.pl")
            
    g = Game()
    print("\nSTART!\n")

    while True:
        print("|------------ Round %d ------------ |\n" % g.round)
        winner_found = False
        winning_player = ""
        winning_team = ""

        for p in g.players:
            print("(%s TEAM) %s's turn" % (p.team, p.name))

            print("- Tiles:", p.tiles)
            # If our board is empty, place your first tile
            if not g.board:
                print("- Playing %s on empty board\n" % p.tiles[0])
                g.place_tile(p.tiles.pop(0))
                continue

            # What tiles can the player use?
            playable_tiles = get_playable_tiles(prolog, g.H, g.T, p.tiles)
            print("- Can play:", playable_tiles)

            # If we didn't have any tiles to play
            if not playable_tiles:
                print("- Pass\n")
                continue

            # If we do have tiles to play
            tile_to_play = playable_tiles.pop(0)
            p.tiles.remove(tile_to_play)
            print("- Playing:", tile_to_play)
            place_tile(g, prolog, tile_to_play)
            print("- New board:", g.board, "\n")

            # If the player has no more tiles (won)
            if not p.tiles:
                winner_found = True
                winning_player = p.name
                winning_team = p.team
                break
            
        if winner_found:
            print("GAMEOVER!")
            print("%s has won the game." % winning_player)
            print("%s team wins.\n" % winning_team)
            break
            
        g.round += 1

if __name__ == '__main__':
    main()