# Breakout Game

A simple Breakout arcade game built in Python using the built-in `turtle` graphics library.

The player controls a paddle at the bottom of the screen and tries to destroy all the blocks by bouncing the ball off the paddle and walls.

## Gameplay

The goal is simple:

* Control the paddle using the arrow keys.
* Keep the ball from falling below the paddle.
* Break as many blocks as possible.
* Earn points for every destroyed block.
* You have a limited number of lives.
* The game ends when you lose all your lives.

## Features

* Paddle controlled with the keyboard
* Ball movement and bouncing
* Multiple rows of colored blocks
* Custom color palette
* Score tracking
* Life system
* Game over state
* Built with Python's `turtle` module

## Technologies

* Python 3
* Turtle Graphics

No external libraries are required for the graphical interface.

## Project Structure

```text
breakout/
│
├── main.py
├── paddle.py
├── ball.py
├── block.py
├── scoreboard.py
├── README.md
└── .gitignore
```

### Files

| File            | Description                                           |
| --------------- | ----------------------------------------------------- |
| `main.py`       | Main game loop and game setup                         |
| `paddle.py`     | Handles the player's paddle and movement              |
| `ball.py`       | Controls the ball and its movement                    |
| `block.py`      | Defines the blocks that can be destroyed              |
| `scoreboard.py` | Handles score, lives and game-over state              |
| `README.md`     | Project documentation                                 |
| `.gitignore`    | Specifies files that should not be uploaded to GitHub |

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

### 2. Enter the project directory

```bash
cd YOUR-REPOSITORY
```

### 3. Run the game

```bash
python main.py
```

Depending on your Python installation, you may need to use:

```bash
python3 main.py
```

## Controls

| Key         | Action            |
| ----------- | ----------------- |
| Left Arrow  | Move paddle left  |
| Right Arrow | Move paddle right |

## Scoring

Each time the ball hits a block, the block disappears and the player's score increases.

The game also tracks the number of remaining lives.

## Game Window

The game uses a 1200 x 900 window with a black background.

The blocks are arranged in multiple rows using the following color palette:

```text
#590d22
#800f2f
#a4133c
#c9184a
#ff4d6d
#ff758f
#ff8fa3
#ffb3c1
#ffccd5
#fff0f3
```

## What I Learned

This project helped me practice:

* Object-oriented programming in Python
* Working with classes and modules
* Keyboard input handling
* Collision detection
* Game loops
* Basic game physics
* Managing game state
* Using the `turtle` graphics library

## Possible Improvements

Some ideas for future versions:

* Add different levels
* Add sound effects
* Add a start screen
* Add a pause button
* Add power-ups
* Add different types of blocks
* Add increasing ball speed
* Add a high-score system
* Improve collision detection
* Add a lives display on the screen

## License

This project is available for educational and personal use.
