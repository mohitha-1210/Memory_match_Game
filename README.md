# Memory Match - Python Edition

A classic 4x4 grid memory game(color) built as a technical demonstration of GUI development and game logic in Python.

## 🛠️ Technical Stack

* **Language:** Python 3.x
* **Library:** Pygame
* **Concepts:** Matrix manipulation, Event-driven programming, State Management.

## 🚀 Key Features

* **Randomized Board:** Uses the "random" library to ensure a unique puzzle every session.
* **Game Logic:** Implements a 1-second delay for non-matching pairs using `pygame.time.get_ticks()' to ensure a smooth user experience.
* **Interactive UI:** Responsive mouse-click detection and real-time score/win rendering.
* **Reset System:** Integrated 'R' key listener to re-initialize the game state without restarting the script.

## 🎮 How to Run

1. Ensure Python and Pygame are installed: `pip install pygame`
2. Run the script: `python memory_game.py`
3. Match all pairs to win! Press **'R'** at any time to reshuffle.
