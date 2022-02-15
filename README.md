# Info

This app is coded in python 3.9.5
Developed by: Ghoul | @NotGhoull

## Code Example

### BotPlay

```python
from classes.player import Player
plr = Player(True)
plr.start()
```

### Humman play

```python
from classes.player import Player
plr = Player(False)
plr.start()
```

## functions

### Player() -> None

: Constructor for the Player class

### start() -> None

: starts the game

### botStart() -> None

: starts the game in bot mode skipping the start() function

### hummanStart() -> None

: Starts the game in humman mode skipping the start() function

### checkChoice(choice1:str, choice2:str) -> Bool

: Args: choice1 -> The choice for player 1 | choice2 -> the Choice for player 2 |
: description: checks the choice and see who wins using default rps rules |
: returns: This returns a True/False vlaue if True then ==choice1== was correct, if False then ==choice2== was correct.
