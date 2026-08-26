# Breakout

A classic Breakout (Arkanoid) game built in Python using the Pygame library, featuring a modern visual style with gradient backgrounds, rounded shapes, and a pixel-art font. This project was created as a practice exercise after completing a Python programming course.

## Features

- Smooth paddle control (arrow keys or A/D)
- 4 different level layouts (rectangle, pyramid, checkerboard, frame)
- Power-up system: wider paddle, slower ball, extra life
- Scoring system based on brick color/row
- Lives system
- Sound effects
- Pause functionality
- Start screen and game over screen with restart option
- Modern visual style: gradient background, rounded paddle/bricks/power-ups, paddle glow effect, pixel-art (retro-gaming) font

## Controls

| Key | Action |
|---|---|
| `Left Arrow` / `A` | Move paddle left |
| `Right Arrow` / `D` | Move paddle right |
| `SPACE` | Start game (from menu) |
| `P` / `ESC` | Pause / resume |
| `R` | Restart after game over |

## Installation and Usage

1. Clone the repository:
```bash
git clone https://github.com/maciek404/breakout-game.git
cd breakout
```

2. (Optional, but recommended) create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the game:
```bash
python main.py
```

## Project Structure

```
breakout/
├── main.py               # Main game loop and logic
├── settings.py            # Configuration (colors, sizes, speeds, fonts)
├── game_state.py           # Score, lives, and level management
├── sound_manager.py         # Sound effects management
├── sprites/
│   ├── paddle.py           # Paddle class
│   ├── ball.py             # Ball class and bounce physics
│   ├── brick.py             # Brick class
│   ├── powerup.py           # Power-up class
│   └── level.py             # Level layout definitions
├── assets/
│   ├── sounds/             # Sound effects
│   └── fonts/              # Pixel-art font (Press Start 2P)
├── requirements.txt
└── README.md
```

## Technologies

- Python 3
- [Pygame Community Edition](https://pyga.me/)
- [Press Start 2P](https://fonts.google.com/specimen/Press+Start+2P) font

## What I Learned

- Object-oriented programming (sprite classes inheriting from `pygame.sprite.Sprite`)
- Collision handling and basic game physics (vectors, angled bounces)
- Game state management (state machine: menu / playing / paused / game over)
- Real-time timers (`pygame.time.get_ticks()`)
- Sound handling in Pygame
- Basic visual polish techniques (gradient backgrounds, rounded shapes with `border_radius`, glow effects with alpha transparency)
- Debugging (including the difference between `is` and `in`, and audio mixer initialization issues)

## Possible Future Improvements

- High score saving
- Additional power-up types (multi-ball, laser)
- Particle effects when bricks are destroyed
- Level editor
