# Battleship

### Description

Simple [Battleship game](https://en.wikipedia.org/wiki/Battleship_(game)) written in **Python 3.7**.

### Interface

```
Your field:
  A B C D E F G H I J
0 O O O O . . O . O .
1 . . . . . . . . . .
2 O O O . . . O . . .
3 . . . . O . . . . .
4 O O O . O . O . O .
5 . . . . . . . . . .
6 . . . . . . O . O .
7 . . . . . . . . . .
8 . . . . O . O . O .
9 . . . . . . . . . .

Enemy field:
  A B C D E F G H I J
0 . . . . . . . . . .
1 . . . . . . . . . .
2 . . . . . . . . . .
3 . . . . . . . . . .
4 . . . . . . . . . .
5 . . . . . . . . . .
6 . . . . . . . . . .
7 . . . . . . . . . .
8 . . . . . . . . . .
9 . . . . . . . . . .

Please, enter coordinates (ex. A 0):
```

### How to run

`python3.7 main.py`

### How to save

Press `Ctrl+C`, the game will suggest to save. During the next loading the game will suggest to load the save.

### How to set field size

`python3.7 main.py --width 5 --height 10`

### TODO

- remove unsafe pickle serialization
