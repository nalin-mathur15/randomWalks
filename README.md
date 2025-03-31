# 2D Random Walk Simulation

## Overview
This Python project simulates a 2-dimensional random walk on a square grid. The walk starts at the center of the grid and continues until either all grid cells have been visited or the user terminates the simulation.
## Features
- Interactive visualisation of the random walk process
- Adjustable grid size (N×N where N is user-specified)
- Real-time progress tracking (percentage of visited cells)
- Speed control slider to accelerate or slow down the simulation
- Visual distinction between visited (blue) and unvisited (white) cells
- Path tracking with a red line showing the walker's journey

## Requirements
- Python 3.x
- Matplotlib
- NumPy (installed automatically with Matplotlib)

## Installation
1. Clone this repository or download ``main.py``
2. Install required packages:
   ```bash
   pip install matplotlib
   ```

## Usage
1. Run the script:
   ```bash
   python main.py
   ```
2. When prompted, enter the grid size (e.g., 50 for a 50×50 grid)
3. The simulation window will appear with:
   - Grid visualisation
   - Speed control slider at the bottom
4. Control the simulation:
   - Use the slider to adjust speed (left=faster, right=slower)
   - Close the window to stop the simulation

## Output
- Console shows real-time progress (percentage of visited cells)
- Visual display shows:
  - Blue cells: Visited locations
  - White cells: Unvisited locations
  - Red line: Path taken by the walker
  - Red dot: Current position

## Notes
- For large grids (>50), visiting all cells may take extremely long
- The simulation becomes more interesting with larger grid sizes
- The walker moves only in cardinal directions (up/down/left/right)

## Example
```bash
$ python main.py
Enter the grid size (e.g., 50 for a 50x50 grid): 30
Starting 2D random walk simulation...
(close the window to stop the simulation)
Progress: 127/900 cells visited (14.11%)
```

Enjoy exploring random walks!