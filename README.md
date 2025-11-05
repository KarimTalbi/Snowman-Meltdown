# ⛄️ Snowman-Meltdown

A simple, command-line word-guessing game where you try to save the snowman from melting by correctly guessing a secret word. Each incorrect guess moves the snowman to the next stage of melting, visualized through ASCII art.

## ✨ How to Play

The objective is to guess the hidden word one letter at a time before the snowman completely melts.

1.  The game selects a word at random from a predefined list (e.g., "python", "snowman", "meltdown").
2.  You are shown the current stage of the snowman and the hidden word with unguessed letters replaced by underscores.
3.  If you guess a letter correctly, it is revealed in the word.
4.  If you guess incorrectly, the snowman melts one stage further. The game uses 5 distinct stages of melting, from a full snowman to completely melted.
5.  **You Win:** If you guess the complete word before the snowman melts.
6.  **You Lose:** If the snowman melts entirely before you guess the word.

## ⚙️ Setup and Execution

### Prerequisites

You only need Python installed on your system.

### How to Run

1.  Navigate to the project's root directory in your terminal.
2.  Execute the main application file:

```bash
python snowman.py
````

3.  The game will start and prompt you to guess a letter. After each game, you will be asked if you wish to keep playing (`y/n`).

## 📂 Project Files

| File | Description |
| :--- | :--- |
| `snowman.py` | The main entry point of the application; starts the game. |
| `game_logic.py` | Contains the core game loop, input handling, and win/loss conditions. |
| `ascii_art.py` | Stores the ASCII art representations for the different melting stages of the snowman. |
