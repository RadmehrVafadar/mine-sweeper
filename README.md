# Mine Sweeper

A classic Minesweeper game implementation built with Python and pygame.

## Demo

![Minesweeper Demo](demo.gif)

## Description

This is a fully functional Minesweeper game featuring a 16x16 grid with 40 randomly placed mines. Players can reveal cells to find numbers indicating adjacent mines, or flag cells they suspect contain mines. The game includes hover effects, color-coded numbers, intuitive tool switching, flood-fill revealing, and complete win/lose functionality.

## Features

- **16x16 Game Board**: Classic minesweeper grid size with 40 mines
- **Dual Tool System**: Switch between mine detection and flag placement tools
- **Flood Fill Algorithm**: Automatically reveals connected empty areas when clicking empty cells
- **Game Over & Win Detection**: Complete game state management with proper win/lose conditions
- **Visual Feedback**: Hover effects and color-coded number display
- **Interactive Gameplay**: Left-click to reveal cells, switch tools to flag suspicious areas
- **Color-Coded Numbers**: Each number (1-8) has a unique color to indicate the number of adjacent mines
- **Restart Functionality**: Press 'R' to restart the game after winning or losing
- **Custom Sprites**: Beautiful custom artwork for different cell states

## Screenshots

The game includes various visual states:
- Normal land tiles
- Highlighted tiles on hover
- Revealed empty tiles with numbers
- Flagged tiles
- Bomb tiles (when revealed)

## Requirements

- Python 3.x
- pygame

## Installation

1. Clone this repository:
```bash
git clone https://github.com/RadmehrVafadar/mine-sweeper 
cd mine-sweeper
```

2. Install pygame:
```bash
pip install pygame
```

3. Run the game:
```bash
python main.py
```

## How to Play

1. **Start the Game**: Run `python main.py` to launch the game window
2. **Tool Selection**: Click the tool button in the bottom-right corner to switch between:
   - **Bomb Tool** (default): Click to reveal cells
   - **Flag Tool**: Click to place/remove flags on suspected mine locations
3. **Gameplay**:
   - Click on cells to reveal them
   - Numbers indicate how many mines are adjacent to that cell
   - Use flags to mark suspected mine locations
   - Avoid clicking on mines!

### Number Color Code

- **1**: Light Blue
- **2**: Green  
- **3**: Red
- **4**: Dark Blue
- **5**: Hot Pink
- **6**: Orange
- **7**: Yellow
- **8+**: Dark Pink

## Game Controls

- **Left Click**: Reveal cell (bomb tool) or place/remove flag (flag tool)
- **Tool Button**: Click to switch between bomb detection and flag placement
- **R Key**: Restart the game after game over or winning
- **Window Close**: Click the X button to exit

## Project Structure

```
mine-sweeper/
├── main.py              # Main game loop and initialization
├── my_module.py         # Button and ToggleButton classes
├── source/              # Game sprites and images
│   ├── Land.png         # Normal land tile
│   ├── land_bright.png  # Highlighted tile
│   ├── land_empty-V2.png # Revealed empty tile
│   ├── land_with_bomb-V2.png # Bomb tile
│   └── land_with_flag.png # Flagged tile
├── todo.txt            # Development roadmap
└── README.md           # This file
```

## Development Status

### Completed Features
- ✅ Basic minesweeper gameplay
- ✅ Random mine placement
- ✅ Adjacent mine counting
- ✅ Tool switching (bomb/flag)
- ✅ Visual feedback and hover effects
- ✅ Color-coded numbers
- ✅ Flag placement/removal
- ✅ Flood fill for revealing connected empty areas
- ✅ Game over detection and restart functionality
- ✅ Win condition detection
- ✅ Complete game state management

### Potential Future Enhancements
- 🔄 Center the game board in the window
- 🔄 Add difficulty levels (different grid sizes/mine counts)
- 🔄 Add timer and score tracking
- 🔄 Add sound effects
- 🔄 Add animations

## Technical Details

- **Language**: Python 3
- **Framework**: pygame
- **Grid Size**: 16x16 (640x640 pixels)
- **Mine Count**: 40
- **Window Size**: 700x700 pixels
- **Framerate**: 60 FPS

## Classes

### Button Class
Handles individual mine cells with states for:
- Normal, hover, clicked, flagged, bomb, and empty states
- Number display with color coding
- Event handling for mouse interactions

### ToggleButton Class
Manages the tool selection button:
- Toggles between bomb detection and flag placement tools
- Visual feedback showing current tool state

## Contributing

Feel free to contribute to this project by:
1. Implementing features from the todo list
2. Adding new game modes or difficulty levels
3. Improving the user interface
4. Adding sound effects or animations

## License

This project is open source and available under the [MIT License](LICENSE). 