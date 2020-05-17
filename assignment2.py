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
    
    def update_HT(self):
        self.H = self.board[0][0]
        self.T = self.board[len(self.board) - 1][1]

    
# TODO: Will convert to Game obj.
def get_board_head_tail(board):
    print("Getting H and T")

    head = board[0][0]
    tail = board[len(board) - 1][1]
    return head, tail


def clean_playable_tiles(playable_tiles):
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



def main():
    # TODO: Get a game to play
    # TODO: Prolog program to show which tile is played
    # TODO: Prolog program to show the new board
    # TODO: Create a Bayseian belief Representation

    # PROLOG
    prolog = Prolog()
    prolog.consult("dominoes.pl")

    """
    my_tiles = [[5,3],[3,2],[4,4],[2,1]]
    board = [[5,2],[2,2]]
    head = 5
    tail = 2

    # What are our playable tiles?
    playable_tiles = (list(prolog.query("can_play(%s,%s,%s,W)." % (head, tail, my_tiles))))

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

    # TODO: Apply logic that checks Head or Tail, then can see if it needs to flip it.

    print("SET",playable_tiles_set)

    h, t = get_board_head_tail(board)

    for tile in playable_tiles_set:
        low_flag = list(prolog.query("can_play_low_end(%s,%s,%s,W)." % (head, tail, [tile])))
        high_flag = list(prolog.query("can_play_high_end(%s,%s,%s,W)." % (head, tail, [tile])))
        print("working with",tile)

        # We are working with the Head <---
        if low_flag:
            print("I was low")

            if tile[1] != h:
                tile = list(reversed(tile))
            print(tile)
            # place tile
            # uptate head tail

        # WE are working with the tail --->
        if high_flag:
            print("I was high")
            if tile[0] != t:
                tile = list(reversed(tile))
            print(tile)
            # place tile
            # update head tail
            
    h, t = get_board_head_tail(board)
    print(h)
    print(t)
    """

        
    print("\nGame started!\n")
    g = Game()
    
    print("----------------")
    print("Tiles:")
    for p in g.players:
        print(p.name, p.tiles)
    print("---------------")

    # TEMP: Just using this as a base board 
    # g.place_tile([1,2])

    print("Board:", g.board)

    while True:
        print("Round %d\n" % g.round)

        for p in g.players:
            print("%s's turn" % p.name)
            # If our board is empty, place your first tile
            if not g.board:
                print("I placed %s in empty board.\n" % p.tiles[0])
                g.place_tile(p.tiles.pop())
                continue

            # What tiles can the player use?
            player_playable_tiles = (list(prolog.query("can_play(%s,%s,%s,W)." % (g.H, g.T, p.tiles))))
            playable_tiles_clean = clean_playable_tiles(player_playable_tiles)

            print("Playable Tiles:",playable_tiles_clean)

            # If we didn't have any tiles to play
            if not playable_tiles_clean:
                print("I can't play..\n")
                continue

            # If we do have tiles to play
            else:
                print("I can play!\n")

            
        g.round += 1
        break


if __name__ == '__main__':
    main()