# connect-4-game

This is simple implementation of "4 in the row" game.

Command-line interface is pretty basic. Each turn you need to choose one of the available actions.

Initial state:
--------------

```
. . . . . . . 
. . . . . . . 
. . . . . . . 
. . . . . . . 
. . . . . . . 
. . . . . . . 
Available actions: [0, 1, 2, 3, 4, 5, 6]
Player #1 >
```

Winning conditions:
-------------------

You need to place 4 symbols in a row before your opponent does it!

For example, here Player #1 won:

```
. . . . . . . 
. . . . . . . 
. . . X . . . 
. . X O . . . 
. X O X . . . 
X O X O . . O 
player 1 won!
```
