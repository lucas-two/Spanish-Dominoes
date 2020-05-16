

% Can play on end with value X the tile [X,Y]
tile_playable_on_end( X, [X,Y]).
tile_playable_on_end( Y, [X,Y]).

% Can play on end with value X with a tile on the list that starts
% with a tile the given tile
can_play_on_end(X , [T | R],T) :-  tile_playable_on_end( X, T).
can_play_on_end(X , [T | R],O) :-  can_play_on_end( X, R, O).

% can the player with hold H play on a chain with ends X and Y the tile T

% which side of the dominoe can we play?
can_play_low_end( X ,  Y , H, T) :-   can_play_on_end( X, H, T).
can_play_high_end( Y ,  X , H, T) :-   can_play_on_end( X, H, T).

can_play( X ,  Y , H, T) :-   can_play_low_end( X ,  Y , H, T) .
can_play( X ,  Y , H, T) :-    can_play_high_end( X ,  Y , H, T) .


same_orientation(S,X,Y) :- ==(S, X).


% tests
% can_play( 5,4, [ [3,6], [2,0], [1,2]],W).
% can_play( 5,1, [ [3,6], [2,0], [1,2]],W).
% can_play( 1,1, [ [3,6], [2,0], [1,2]],W).
% can_play( 2,1, [ [3,6], [2,0], [1,2]],W).
