# Checkers Game with AI

## Overview
This project, developed for an Artificial Intelligence (Spring 2024) course at FAST NUCES, is a Python-based implementation of the Checkers game. It allows a human player to compete against an AI opponent or observe two AI agents playing against each other. The AI employs the Minimax algorithm with Alpha-Beta pruning and a heuristic evaluation function to make strategic decisions.

## Features
- **Game Modes**:
  - **AI vs. Player**: Human player (Player 2) competes against the AI (Player 1).
  - **AI vs. AI**: Two AI agents play against each other.
- **AI Algorithms**:
  - **Minimax**: Recursively evaluates all possible moves, assuming optimal opponent play.
  - **Minimax with Alpha-Beta Pruning**: Optimizes Minimax by pruning branches that cannot improve outcomes.
- **Difficulty Levels**:
  - Easy (search depth 1)
  - Medium (search depth 3)
  - Hard (search depth 5)
- **Board Visualization**: Text-based 8x8 board with pieces ('O' for Player 1, 'X' for Player 2, 'K'/'k' for kings).
- **Game Mechanics**:
  - Diagonal movement (forward for normal pieces, forward/backward for kings).
  - Captures by jumping over opponent pieces.
  - King promotion upon reaching the opponent’s back row.
  - Draw detection via repeated board states.
- **State History**: Stores up to 10 board states to check for draws.

## Prerequisites
- Python 3.x
- No external dependencies required.

## Installation
1. Clone or download the repository.
2. Ensure Python 3.x is installed.
3. Navigate to the project directory.

## Usage
1. Run the game:
   ```bash
   python checkers.py
   ```
2. Select options via prompts:
   - **Game Mode**: 1 (AI vs. Player) or 2 (AI vs. AI).
   - **AI Algorithm**: 1 (Minimax) or 2 (Minimax with Alpha-Beta Pruning).
   - **Difficulty**: 1 (Easy), 2 (Medium), or 3 (Hard).
3. In **AI vs. Player** mode:
   - AI (Player 1) moves automatically.
   - Human (Player 2) enters start and end positions (row, col) from displayed valid moves.
4. Game ends with a win (all opponent pieces captured or no valid moves) or draw (same state repeats three times).

## File Structure
- `checkers.py`: Core script with game logic, AI algorithms, and gameplay loop.
- `Checkers Game Rules and AI Strategies.pptx`: Slides covering game rules and AI strategies.

## Game Rules
- Played on an 8x8 board with 12 pieces per player.
- Pieces move diagonally (forward for normal pieces, forward/backward for kings).
- Captures occur by jumping over an opponent’s piece to an empty square.
- Pieces reaching the opponent’s back row become kings.
- Game ends when:
  - One player captures all opponent pieces (win).
  - A player has no valid moves (loss).
  - Board state repeats three times (draw).

## AI Implementation
- **Minimax**: Evaluates moves to a set depth, assuming optimal opponent play.
- **Alpha-Beta Pruning**: Reduces computation by pruning non-optimal branches.
- **Heuristic Evaluation**: Scores board states by piece count difference (`X`/`k` - `O`/`K`).
- **Depth Levels**:
  - Easy: Depth 1 (fast, less strategic).
  - Medium: Depth 3 (balanced).
  - Hard: Depth 5 (strategic, slower).

## Limitations
- AI performance scales with search depth; higher depths slow down gameplay.
- Simple heuristic (piece count) could be improved with king count or positional factors.
- Terminal-based interface limits user experience.

## Future Improvements
- Add a GUI using Pygame or Tkinter.
- Enhance heuristic to include king count or board control.
- Support multiple jumps in one turn.
- Optimize AI with iterative deepening or transposition tables.

## Acknowledgments
Developed for the Artificial Intelligence course at FAST NUCES, based on standard Checkers rules and AI techniques.

## License
Licensed under the MIT License. Use, modify, and distribute as per the license terms.
